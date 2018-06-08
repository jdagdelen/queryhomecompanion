# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State, Event
import json
from model import format_query_string, initialize_options

app = dash.Dash()
server = app.server

app.config.supress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')])


# TODO: add logic for filling out questions like is_metal, tetragonal, etc

(field_options, operator_options, value_options) = initialize_options()

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
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
                )], style={"width": "40%", "paddingBottom": "10px", "paddingTop": "10px"}, className="six columns"),
            html.Div([
                dcc.Dropdown(
                    options=operator_options,
                    value=None,
                    multi=True,
                    id='operator',
                )], style={"width": "10%", "paddingBottom": "10px", "paddingTop": "10px"}, className="six columns"),
            html.Div([
                dcc.Dropdown(
                    options=value_options,
                    value=None,
                    multi=True,
                    id='value',
                )], style={"width": "40%", "paddingBottom": "10px", "paddingTop": "10px"}, className="six columns"),
        ]),
        html.Div([
            html.Label('Your query should be: ', style={"font-size": "20px"}),
            html.Div(id='output', style={"font-size": "20px"})
        ], className="four columns")
    ])

#
# @app.callback(
#     [Input('field', 'value'), Input('field', 'value'), Input('value', 'value')]
# )
# def update_options(field, operator, value):
#     if operator:
#         return None
#     else:
#         return format_query_string(field, operator, value)

@app.callback(
    Output('output', 'children'),
    [Input('field', 'value'), Input('field', 'value'), Input('value', 'value')]
)
def display_output(field, operator, value):
    if field is None:
        return '{}'
    else:
        return format_query_string(field, operator, value)


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

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    print("starting...")
    app.run_server(debug=True)
