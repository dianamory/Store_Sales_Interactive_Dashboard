import plotly.express as px
import pandas as pd

def crear_grafico(df):
    # Creación del dataframe mapa
    df['valor_total'] = df['valor_total']/1000000
    df_mapa = df.groupby(['ciudad','latitud','longitud'])['valor_total'].sum().sort_values(ascending=False).reset_index()

    # Grafica del mapa
    fig = px.scatter_geo(df_mapa, 
                            lat='latitud', 
                            lon='longitud', 
                            scope='south america', 
                            template='seaborn', 
                            size='valor_total',
                            hover_name='ciudad',
                            hover_data={'latitud':False, 'longitud':False},
                            width=1000,  # Ajusta el ancho del mapa
                            height=450
                            )
    
    fig.update_layout(
    margin=dict(l=0, r=100, t=80, b=50),  # Ajusta los márgenes izquierdo, derecho, superior e inferior
    )
    fig.update_traces(
    hovertemplate='<b>%{hovertext}</b><br>Total de ingresos: %{marker.size:$,.2f}M<extra></extra>'
   
    )
    
    

    fig.update_layout(
    title={
        'text': 'Ingreso por Estado',
        'y':0.95,
        'x':0.15,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'color': 'gold',
            'size': 16
        }
    }
    )
    
 
    return fig

