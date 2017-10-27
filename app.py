import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from graphs import graphs, texts


# create application

app = dash.Dash()

app.layout = html.Div(children=[

    html.H1(children='Studenti středních škol - životní styl'),

    # TODO??? I don't know why multiline string does not work 
    dcc.Markdown(children='Data z [www.kaggle.com](http://www.kaggle.com): [Student alcohol consumption](https://www.kaggle.com/uciml/student-alcohol-consumption).'),

    
    dcc.Dropdown(
        options=[
            {'label': 'Histogram rozdělení věku - chlapci, dívky', 'value': 'hist_age'},
            {'label': 'Konzumace alkoholu dle věku - chlapci, dívky (bar plot)', 'value': 'alcohol_bar'},
            {'label': 'Konzumace alkoholu dle věku (box plot)', 'value': 'alcohol_box'},
            {'label': 'Rodinné zázemí a alkohol', 'value': 'alcohol_family'},
            {'label': 'Internet doma a životní styl', 'value': 'internet_lifestyle'},
            {'label': 'Vztahy a věk', 'value': 'relationship_age'},
            {'label': 'Matka v domácnosti a rodinné zázemí (boxplot)', 'value': 'mother_box'},
            {'label': 'Matka v domácnosti a rodinné zázemí (histogram)', 'value': 'mother_hist'}
        ],
        value='hist_age',
        id='dropdown'
    ),

    dcc.Graph(
        id='main_graph',
    ),

    html.H3(children='Kód:'),
    
    dcc.Markdown(
        id='code', children=''
    )

])

@app.callback(
    Output(component_id='main_graph', component_property='figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_figure(plot_type):
    # return selected figure 
    return graphs[plot_type]()

@app.callback(
    Output(component_id='code', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_code(plot_type):
    # return corresponding string with code 
    return texts[plot_type]



import os
server = app.server
server.secret_key = os.environ.get('SECRET_KEY', '1234321')


if __name__ == '__main__':
    app.run_server()
