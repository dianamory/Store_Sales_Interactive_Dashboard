import pandas as pd
import plotly.express as px

def crear_grafico(df):
    df = df.groupby('producto')['ingreso_neto'].sum().sort_values(ascending = True).reset_index()
    
    # Se crea la grafica
    fig = px.bar(df.tail(10),
                 x = 'ingreso_neto',
                 y = 'producto',
                 text = 'ingreso_neto',
              )
    
    fig.update_layout(yaxis_title = 'Productos', xaxis_title = 'Ingresos ($)', showlegend = False)
    fig.update_traces(texttemplate = '%{text:.3s}')
    
    fig.update_layout(
    title={
        'text': 'Top de productos que generan mas ingresos ($)',
        'y':0.95,
        'x':0.34,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'color': 'gold',
            'size': 16
        }
    }
    )
    return fig