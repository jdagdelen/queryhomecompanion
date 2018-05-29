# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State, Event

app = dash.Dash()
server = app.server

app.config.supress_callback_exceptions=True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')])

@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')])
def generate_layout(url):
    return html.Div([
        html.Label('Welcome to A Query Home Companion. Build a query below.'), 
        dcc.Dropdown(
            options=[
                {'label': 'structure', 'value': 'structure'},
                {'label': 'material_id', 'value': 'material_id'},
				{'label': 'mpid', 'value': 'material_id'},
                {'label': 'pretty_formula', 'value': 'pretty_formula'},
				{'label': 'formula', 'value': 'pretty_formula'},
				{'label': 'chemical formula', 'value': 'pretty_formula'},
				{'label': 'structure.sites', 'value': 'structure.sites'},
				{'label': 'structure.lattice', 'value': 'structure.lattice'},
				{'label': 'structure.lattice.a', 'value': 'structure.lattice.a'},
				{'label': 'structure.lattice.b', 'value': 'structure.lattice.b'},
				{'label': 'structure.lattice.c', 'value': 'structure.lattice.c'},
				{'label': 'structure.lattice.alpha', 'value': 'structure.lattice.alpha'},
				{'label': 'structure.lattice.beta', 'value': 'structure.lattice.beta'},
				{'label': 'structure.lattice.gamma', 'value': 'structure.lattice.gamma'},
				{'label': 'structure.lattice.volume', 'value': 'structure.lattice.volume'},
				{'label': 'structure.lattice.matrix', 'value': 'structure.lattice.matrix'},
            ],
            value=None,
            multi=True,
            id='input'
        ),
        html.Div(id='output')
    ])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    if value is None:
	    return 'Your query should be: {}'
    else:
        query_string = ['"'"{}"'":<thing_to_match>'.format(entry) for entry in value]
        query_string = ", ".join(query_string)
        query_string = "{" + query_string + "}"
        return 'Your query should be: ' + query_string

if __name__ == '__main__':
    print("starting...")
    app.run_server(debug=True)
