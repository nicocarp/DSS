import numpy as np
import pickle

CLASES = {
    0: "T-shirt/top",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle boot"
}

MODELOS = [
    {
        "nombre": 'SVC',
        "path":'modelos/SVM.pickle',
        "instancia":None
    },{
        "nombre": 'DummyClassifier',
        "path":'modelos/CLF.pickle',
        "instancia":None
    },{
        "nombre": 'RandomForestClassifier',
        "path":'modelos/Randomforest.pickle',
        "instancia":None
    },
   # {
   #     "nombre": 'CNN',
   #     "path":'modelos/clasificadorNET-Damian1-score(0.9).pickle',
   #     "instancia":None
   # }
]

class AdjustVariable(object):

    """
    Used to decreases linearly the learning rate with the number of epochs,
    while we the momentum increase.
    """
    def __init__(self, name, start=0.01, stop=0.001):
        self.name = name
        self.start, self.stop = start, stop
        self.ls = None

    def __call__(self, nn, train_history):
        if self.ls is None:
            self.ls = np.linspace(self.start, self.stop, nn.max_epochs)

        epoch = train_history[-1]['epoch']
        new_value = np.float32(self.ls[epoch - 1])
        getattr(nn, self.name).set_value(new_value)

class Predictor:

    error = ""

    def __init__(self, modelo_predictor = None):
        self._modelos_cargados = self.__cargar_modelos__()      
        
    def __cargar_modelos__(self):        
        for modelo in MODELOS:
            with open(modelo.get('path'), 'rb') as f:
                modelo['instancia'] = pickle.load(f)
        return True

    def predecir(self, np_array):
        if not self._modelos_cargados:
            return {
                "estado": -1,
                "result":"Error: Los modelos no fueron cargados" 
            }
            
        if np_array.shape != (28,28):
            return {"estado": -2,
                    "result": "Error: Imagen debe ser 28*28 NO "+str(np_array.shape)
            }
            
        a = np_array.reshape( 1, 784)
        result = []
        for modelo in MODELOS:
            if modelo['nombre'] == 'CNN':
                a = a.reshape(-1, 1, 28,28)
            _prediccion = modelo.get('instancia').predict(a)[0]
            result.append({
                "nombre_modelo": modelo.get('nombre'),
                "label": CLASES[_prediccion]
            })

        return {
            "estado": 1,
            "result":result
        }