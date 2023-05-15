import dash
from dash import html
from dash import dcc
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
# import ast

# from flask import Flask
# from flask_ngrok import run_with_ngrok

df = pd.read_excel('datasets/master_fajas.xlsx')

df['COM_CH_LN_PZ'] = df['NOM_LINEA'] + '-'+ df['NUM_NUM_POZA'].astype(str)
df['DESC_LINEA_AUTO_BLOQUEAD'] = df['DESC_LINEA_AUTO_BLOQUEAD'].apply(lambda x: x[1:-1].split(','))
comb_ch_ln_pz = sorted(list(df['COM_CH_LN_PZ'].unique()))
# print(df.head())

# server = Flask(__name__)
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# run_with_ngrok(server)

app.layout = html.Div([
    dbc.Card([
    html.H1('Implementación de Lógica de Fajas - Chimbote', style={"textAlign": "center","font-weight":"bold"}),

    html.Br(),
    html.H2('Se está descargando actualmente en las siguientes pozas:', style={"font-weight":"bold"}),
    html.Div(
        dcc.Checklist(
            id='checkboxes_poza',
            options=[
                {'label': 'Poza 1', 'value': 1},
                {'label': 'Poza 2', 'value': 2},
                {'label': 'Poza 3', 'value': 3},
                {'label': 'Poza 4', 'value': 4},
                {'label': 'Poza 5', 'value': 5},
                {'label': 'Poza 6', 'value': 6},
                {'label': 'Poza 7', 'value': 7},
                {'label': 'Poza 8', 'value': 8}
            ],
            value=[1]
        ),
        style={'columnCount': 2, 'marginBottom': 20}
    ),
    # html.Div([
    #     dcc.Slider( id="volumen_poza_1", value=0, min=0, max=350, step=25),
    #     dcc.Slider( id="volumen_poza_2", value=0, min=0, max=350, step=25),
    #     dcc.Slider( id="volumen_poza_3", value=0, min=0, max=350, step=25),
    #     dcc.Slider( id="volumen_poza_4", value=0, min=0, max=350, step=25),
    #     dcc.Slider( id="volumen_poza_5", value=0, min=0, max=350, step=25),
    #     dcc.Slider( id="volumen_poza_6", value=0, min=0, max=350, step=25),
    #     dcc.Slider( id="volumen_poza_7", value=0, min=0, max=350, step=25),
    #     dcc.Slider( id="volumen_poza_8", value=0, min=0, max=250, step=25),
    #             ]
    # ),

    dbc.Card(
        [
            dbc.Row([
                dbc.Col([
                        html.H2('VOLUMEN DE POZAS'),
                        html.Hr(),
                        html.H6('Poza 1'),
                        dcc.Slider( id="volumen_poza_1", value=0, min=0, max=350, step=25),
                        html.H6('Poza 2'),
                        dcc.Slider( id="volumen_poza_2", value=0, min=0, max=350, step=25),
                        html.H6('Poza 3'),
                        dcc.Slider( id="volumen_poza_3", value=0, min=0, max=350, step=25),
                        html.H6('Poza 4'),
                        dcc.Slider( id="volumen_poza_4", value=0, min=0, max=350, step=25),
                        html.H6('Poza 5'),
                        dcc.Slider( id="volumen_poza_5", value=0, min=0, max=350, step=25),
                        html.H6('Poza 6'),
                        dcc.Slider( id="volumen_poza_6", value=0, min=0, max=350, step=25),
                        html.H6('Poza 7'),
                        dcc.Slider( id="volumen_poza_7", value=0, min=0, max=350, step=25),
                        html.H6('Poza 8'),
                        dcc.Slider( id="volumen_poza_8", value=0, min=0, max=250, step=25),]
                ),
                dbc.Col([
                        html.H2('MINUTOS EN QUE TERMINARÁ LA DESCARGA'),
                        html.Hr(),
                        html.H6('Poza 1'),
                        dcc.Slider( id="horas_poza_1", value=0, min=0, max=200, step=15),
                        html.H6('Poza 2'),
                        dcc.Slider( id="horas_poza_2", value=0, min=0, max=200, step=15),
                        html.H6('Poza 3'),
                        dcc.Slider( id="horas_poza_3", value=0, min=0, max=200, step=15),
                        html.H6('Poza 4'),
                        dcc.Slider( id="horas_poza_4", value=0, min=0, max=200, step=15),
                        html.H6('Poza 5'),
                        dcc.Slider( id="horas_poza_5", value=0, min=0, max=200, step=15),
                        html.H6('Poza 6'),
                        dcc.Slider( id="horas_poza_6", value=0, min=0, max=200, step=15),
                        html.H6('Poza 7'),
                        dcc.Slider( id="horas_poza_7", value=0, min=0, max=200, step=15),
                        html.H6('Poza 8'),
                        dcc.Slider( id="horas_poza_8", value=0, min=0, max=150, step=15), ]                   
                ),
            ])
        ]
    ),
    html.Br(),
    html.H2('Ocupación de Líneas Actual', style={"font-weight":"bold"}),
    html.Div(
        dcc.Checklist(
            id='checkboxes_linea',
            options=[
                {'label': 'Línea 1', 'value': 'TAMAKUN-S'},
                {'label': 'Línea 2', 'value': 'TAMAKUN-N'},
                {'label': 'Línea 3', 'value': 'TANGARARA-S'},
                {'label': 'Línea 4', 'value': 'TANGARARA-N'},
            ],
            value=['TAMAKUN-S']
        ),
        style={'columnCount': 2, 'marginBottom': 20}
    ),
    html.Br(),
    html.H2('Combinación de Chata-Línea-Poza a Asignar', style={"font-weight":"bold"}),

    dbc.Card([
        dbc.Row([
            dbc.Col([
                    dcc.Dropdown(
        id='dropdown',
        searchable=False,
        # options=[
        #     {'label': '1', 'value': 'opcion1'},
        #     {'label': '2', 'value': 'opcion2'},
        #     {'label': '3', 'value': 'opcion3'}
        # ],
        options=[{'label':f'{i}', 'value':f'{i}'} for i in comb_ch_ln_pz],
        # value='opcion1'
    ),
            ]),
            dbc.Col([
                html.Div(id='resultado'),
                html.Br(),
                html.Div(id='resultado2'),
            ]),
        ]),
    ], body=True,),

    html.Br(),
    ],  body=True,)
]
)

@app.callback(
    dash.dependencies.Output('resultado', 'children'),
    dash.dependencies.Output('dropdown', 'options'),
    dash.dependencies.Output('resultado2', 'children'),
    [
    # dash.dependencies.Input('dropdown', 'value'),
     dash.dependencies.Input('checkboxes_poza', 'value'),
     dash.dependencies.Input('checkboxes_linea', 'value'),
     dash.dependencies.Input('volumen_poza_1', 'value'),
     dash.dependencies.Input('volumen_poza_2', 'value'),
     dash.dependencies.Input('volumen_poza_3', 'value'),
     dash.dependencies.Input('volumen_poza_4', 'value'),
     dash.dependencies.Input('volumen_poza_5', 'value'),
     dash.dependencies.Input('volumen_poza_6', 'value'),
     dash.dependencies.Input('volumen_poza_7', 'value'),
     dash.dependencies.Input('volumen_poza_8', 'value'),
     dash.dependencies.Input('horas_poza_1', 'value'),
     dash.dependencies.Input('horas_poza_2', 'value'),
     dash.dependencies.Input('horas_poza_3', 'value'),
     dash.dependencies.Input('horas_poza_4', 'value'),
     dash.dependencies.Input('horas_poza_5', 'value'),
     dash.dependencies.Input('horas_poza_6', 'value'),
     dash.dependencies.Input('horas_poza_7', 'value'),
     dash.dependencies.Input('horas_poza_8', 'value'),
     ])
def actualizar_resultado(checkboxes_poza_values, checkboxes_linea_values, vol_1, vol_2, vol_3, vol_4, vol_5, vol_6, vol_7, vol_8, time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8 ):
    # resultado = f'Se seleccionó la opción  las casillas: {", ".join(checkboxes_poza_values)}' + ' y ' + f'{"".join(checkboxes_linea_values)}'
    # print(checkboxes_poza_values)
    # print(checkboxes_linea_values)
    df_current = df.copy()

    if vol_1 > 300:
        mask = df_current['NUM_NUM_POZA'] == 1
        df_current = df_current[~mask]

    if vol_2 > 300:
        mask = df_current['NUM_NUM_POZA'] == 2
        df_current = df_current[~mask]

    if vol_3 > 300:
        mask = df_current['NUM_NUM_POZA'] == 3
        df_current = df_current[~mask]

    if vol_4 > 300:
        mask = df_current['NUM_NUM_POZA'] == 4
        df_current = df_current[~mask]

    if vol_5 > 300:
        mask = df_current['NUM_NUM_POZA'] == 5
        df_current = df_current[~mask]

    if vol_6 > 300:
        mask = df_current['NUM_NUM_POZA'] == 6
        df_current = df_current[~mask]

    if vol_7 > 300:
        mask = df_current['NUM_NUM_POZA'] == 7
        df_current = df_current[~mask]

    if vol_8 > 200:
        mask = df_current['NUM_NUM_POZA'] == 8
        df_current = df_current[~mask]

    resultado = 'Las Pozas ' + str(checkboxes_poza_values) + ' y las Líneas '  + str(checkboxes_linea_values) + ' se encuentran ocupadas.'
    

    all_combs = set(df_current['COM_CH_LN_PZ'].unique())
    mask =  (df_current['NUM_NUM_POZA'].isin(checkboxes_poza_values)) & (df_current['NOM_LINEA'].isin(checkboxes_linea_values))
    
    # lineas_bloqueadas = list(df_current.loc[mask, 'DESC_LINEA_AUTO_BLOQUEAD'])
    set_auto = set(df_current.loc[mask, 'DESC_LINEA_AUTO_BLOQUEAD'].explode())

    
    # print('-------------------------')
    # print(df_filtered.head())
    # print(df_filtered.head())
    resultado2 = 'Las Combinaciones:  ' + str(sorted(list(set_auto))) + ' se encuentran autobloquedas por fajas'
    # print(resultado2)
    return resultado, sorted(list(all_combs - set_auto)), resultado2

if __name__ == '__main__':
    app.run_server(debug=True)
