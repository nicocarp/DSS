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
    #{
    #    "nombre": 'RedNeuronal',
    #    "path":'modelos/clasificadorNET-Damian1-score(0.9).pickle',
    #    "instancia":None
    #}
]

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
                    "result": "Error: Imagen debe ser 28*28"            
            }
            
        a = np_array.reshape( 1, 784)
        result = []
        for modelo in MODELOS:
            result.append({
                "nombre_modelo": modelo.get('nombre'),
                "label": CLASES[modelo.get('instancia').predict(a)[0]]
            })

        return {
            "estado": 1,
            "result":result
        }