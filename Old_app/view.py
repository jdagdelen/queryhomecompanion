import dash_html_components as html
import dash_core_components as dcc




def make_advanced_query(fields, operators):
    return html.Div([
        html.Div([
            dcc.Dropdown(
                options=fields,
                value=None,
                multi=False,
                id='field',
                placeholder="Field (start typing to narrow results)"
            )], style={"paddingBottom": "10px", "paddingTop": "10px"},
            className="twelve columns"),
        html.Div([
            dcc.Dropdown(
                options=operators,
                value=None,
                multi=False,
                id='operator',
                placeholder="Operator (i.e. greater than, $gt, etc)"
            )], style={"paddingBottom": "10px", "paddingTop": "10px"},
            className="twelve columns"),
        html.Div([
            dcc.Input(
                value=None,
                type="text",
                id='value',
                placeholder="Value to be compared to."
            )], style={'display': 'inline-block', "paddingBottom": "10px", "paddingTop": "10px"},
            className="twelve columns"),
    ], className="twelve columns")



elements_query = html.Div([
    html.Label("Filter by elements:"),
    html.Div([
        dcc.Input(
            type="text",
            value="elements",
            id='field',
            disabled=True),
    ],
        style={"paddingBottom": "10px", "paddingTop": "10px"},
        className="two columns"),
    html.Div([
        dcc.Dropdown(
            options=[{"label": "contains", "value": "$all"},
                     {"label": "does not contain", "value": "$not:{\"$in\":"}],
            placeholder="contains/does not contain",
            id='operator',
            disabled=False,
            multi=False
        )
    ],
        style={"paddingBottom": "10px", "paddingTop": "10px"},
        className="two columns"),
    html.Div([
        dcc.Input(
            type="text",
            id='value',
            placeholder="Enter elements separated by spaces.",
            autofocus=True,
            style={"width": "300%"})
    ],
        style={"paddingBottom": "10px", "paddingTop": "10px"},
        className="two columns"),
], className="twelve columns")


stoichiometry_query = html.Div([
    html.Label("Filter by stoichiometry:"),
    html.Div([
        dcc.Input(
            id='field',
            type="text",
            value="anonymous_formula",
            disabled=True)
    ],
        style={"width": "40%", "paddingBottom": "10px", "paddingTop": "10px"},
        className="six columns"),
    html.Div([
        dcc.Dropdown(
            id='operator',
            options=[{"label": "is", "value": None},
                     {"label": "any of", "value": "$in"},
                     {"label": "none of", "value": "$not:{\"$in\":"}],
            placeholder="contains/does not contain",
            disabled=False,
            multi=False
        )
    ],
        style={"width": "10%", "paddingBottom": "10px", "paddingTop": "10px"},
        className="six columns"),
    html.Div([
        dcc.Input(
            id='value',
            type="text",
            value="$all",
            placeholder="Enter stoichiometry (i.e. A:1, B:1, C:3)",
            autofocus=True)
    ],
        style={"width": "40%", "paddingBottom": "10px", "paddingTop": "10px"},
        className="six columns"),
], className="three columns")