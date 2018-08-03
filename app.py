# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
import callbacks
from model import initialize_field_options

app = dash.Dash()
server = app.server

app.config.supress_callback_exceptions = True
app.title = "A Query Home Companion"


###### Page Header #######

header = html.Div([
    html.Label('Welcome to A Query Home Companion. Explore the searchable fields below.',
               style={"font-size": "20px"}),
])


###### Query Area #######

query = html.Div([], id='page-content')

options_dropdown = html.Div(
    dcc.Dropdown(
        options=initialize_field_options(),
        value=None,
        multi=False,
        id='options_selection',
        placeholder="What would you like to search?"
    )
)
#
#
# ###### Buttons #######
# buttons = html.Div([
#     html.Button("AND",
#                 id="button_add_query",
#                 className="button-primary"),
# ], className="four columns")


###### Results #######
# results = html.Div([
#     html.Label('Your query should be: ', style={"font-size": "20px"}),
#     html.Div(id='output', style={"font-size": "20px"})
# ])
results = html.Div(callbacks.get_readme(None))

###### Main layout #######
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    header,
    html.Div(style={"paddingTop": "10px", "paddingBottom": "10px"}),
    html.Div(options_dropdown, className="twelve columns"),
    html.Div([
        results
    ], style={"paddingTop": "50px", "paddingBottom": "10px"}, id="page-content")
], className="container main-container")

callbacks.bind(app)


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


####### Main Loop ########
if __name__ == '__main__':
    print("starting...")
    app.run_server(debug=True)
