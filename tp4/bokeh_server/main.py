from bokeh.plotting import figure, curdoc
from bokeh.layouts import layout, widgetbox
from bokeh.models import ColumnDataSource, HoverTool, Div
from bokeh.models.widgets import Slider, TextInput, DatePicker, RadioGroup
import pandas as pd
import datetime

desc = Div(text=open( "description.html").read(), width=800)

f_ini = datetime.datetime.strptime('2010-01-01', '%Y-%m-%d').date()
f_hasta = datetime.datetime.today().date()

input_fecha_desde = DatePicker(title="Fecha desde", value=f_ini)
input_fecha_hasta = DatePicker(title="Fecha hasta", value=f_hasta)
input_cant_likes = Slider(title="Minimo likes", value=0, start=0, end=300, step=1)
input_texto = TextInput(title="Palabra a buscar en textos")
input_con_retweets =  RadioGroup(labels=["Tweets", "Retweets"], active=0)

# Create Column Data Source that will be used by the plot
source = ColumnDataSource(data=dict(x=[], y=[], likes=[], texto=[]))
hover = HoverTool(tooltips=[
    ("Texto", "@text"),
    ("Likes", "@likes")
])

p = figure(plot_height=500, plot_width=700, title="Titulo", tools=[hover, 'box_zoom','reset'] ,y_axis_type='datetime')

p.circle(x="x", y="y", source=source, size=10, color="black", line_color=None )
p.xaxis.axis_label = "Likes"
p.yaxis.axis_label = "Fecha"

controls = [input_cant_likes, input_fecha_desde, input_fecha_hasta, input_texto, input_con_retweets]

def get_datos():
    todos_tweets = pd.read_json("datos/todos_los_tweets.json")
    if input_con_retweets.active == 1:
        todos_tweets = pd.concat([todos_tweets, pd.read_json("datos/todos_los_retweets.json")])    
    todos_tweets = todos_tweets[
                        (todos_tweets['favorite_count'] >= input_cant_likes.value) &
                        (todos_tweets['created_at'] > input_fecha_desde.value) & 
                        (todos_tweets['created_at'] <=  input_fecha_hasta.value) &
                        (todos_tweets['text'].str.contains(input_texto.value, case=False))
                    ]
    return todos_tweets    

def update():
    datos = get_datos()
    p.title.text = "%d Tweets" % len(datos)
    source.data = dict(
        x=datos['favorite_count'],
        y=datos['created_at'],
        likes=datos['favorite_count'],
        text=datos['text']        
    )

for control in controls:
    try:
        control.on_change('value', lambda attr, old, new: update())
    except:
        control.on_change('active', lambda attr, old, new: update())

sizing_mode = 'fixed'  # 'scale_width' also looks nice with this example

inputs = widgetbox(*controls, sizing_mode=sizing_mode)
l = layout([
    [desc],
    [inputs, p],
], sizing_mode=sizing_mode)

update()  # initial load of the data

curdoc().add_root(l)
curdoc().title = "Tweets"
