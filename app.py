# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State, Event
import json

app = dash.Dash()
server = app.server

app.config.supress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')])

field_options = [
    {'label': 'mpid', 'value': 'material_id'},
    {'label': 'formula', 'value': 'pretty_formula'},
    {'label': 'anonymous formula', 'value': 'snl_final.anonymized_formula'},
    {'label': 'chemical formula', 'value': 'pretty_formula'},
    {'label': 'bulk modulus (Reuss)', 'value': 'elasticity.K_Voigt'},
    {'label': 'bulk modulus (Voigt)', 'value': 'elasticity.K_Reuss'},
    {'label': 'bulk modulus (VRH)', 'value': 'elasticity.K_VRH'},
    {'label': 'bulk modulus (Voigt Reuss Hill)', 'value': 'elasticity.K_Voigt_Reuss_Hill'},
    {'label': 'shear modulus (Reuss)', 'value': 'elasticity.G_Voigt'},
    {'label': 'shear modulus (Voigt)', 'value': 'elasticity.G_Reuss'},
    {'label': 'shear modulus (VRH)', 'value': 'elasticity.G_VRH'},
    {'label': 'shear modulus (Voigt Reuss Hill)', 'value': 'elasticity.G_Voigt_Reuss_Hill'},
    {'label': 'stability (e_above_hull < 25 meV)', 'value': 'e_above_hull'},
    {'label': 'energy above hull', 'value': 'e_above_hull'},
    {'label': 'bravais lattice', 'value': 'spacegroup.crystal_system'},
    {'label': 'crystal system', 'value': 'spacegroup.crystal_system'},
]

# TODO: add logic for filling out questions like is_metal, tetragonal, etc

mapidoc = json.load(open("mapidoc.json"))

for entry in mapidoc:
    if entry is not None and len(entry) > 0 and "@" not in entry:
        entry = entry.replace("/", ".")
        field_options.append({'label': entry, 'value': entry})

value_options = []
operators = ["$lt", "$gt", "$lte", "$gte", "True", "False", "$in", "$nin"]
for entry in operators:
    if entry is not None and len(entry) > 0:
        value_options.append({'label': entry, 'value': entry})


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def generate_layout(url):
    return html.Div([
        html.Label('Welcome to A Query Home Companion. Build a query below.', style={"font-size": "20px"}),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    options=field_options,
                    value=None,
                    multi=True,
                    id='field',
                    placeholder="Field (start typing to narrow results)"
                )], style={"width": "30%", "paddingBottom": "10px", "paddingTop": "10px"}),
            html.Div([
                dcc.Dropdown(
                    options=value_options,
                    value=None,
                    multi=True,
                    id='value',
                )], style={"width": "30%", "paddingBottom": "10px"}),
            html.Div(id='output', style={"font-size": "20px"})
        ], className='two columns')
    ])


@app.callback(Output('output', 'children'), [Input('field', 'value'), Input('value', 'value')])
def display_output(field, value):
    if field is None:
        return 'Your query should be: {}'
    else:
        query_string = ['"'"{}"'":<thing_to_match>'.format(entry) for entry in field]
        query_string = ", ".join(query_string)
        query_string = "{" + query_string + "}"
        return 'Your query should be: ' + query_string


### CSS settings ###
BACKGROUND = 'rgb(230, 230, 230)'
COLORSCALE = [[0, "rgb(244,236,21)"], [0.3, "rgb(249,210,41)"], [0.4, "rgb(134,191,118)"],
              [0.5, "rgb(37,180,167)"], [0.65, "rgb(17,123,215)"], [1, "rgb(54,50,153)"]]

# loading css files
css_files = ["dash_extra.css", "skeleton.min.css",
             "googleapis.raleway.css", "googleapis.dosis.css",
             "webstract.css", "annotation_styles.css"]

stylesheets_links = []
for css in css_files:
    stylesheets_links.append(html.Link(
        rel='stylesheet',
        href='/static/css/' + css
    ))

if __name__ == '__main__':
    print("starting...")
    app.run_server(debug=True)
