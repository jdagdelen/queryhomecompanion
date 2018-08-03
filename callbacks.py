from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import json
import os
import errno

def get_readme(option):
    if option is None:
        return ""
    path = "readmes/materials/" + option.replace(".", "/") +"/README.md"
    with open(path, 'r') as file:
        readme = file.read()
    return html.Div([html.H2(option, style={"color":"teal"}), dcc.Markdown(readme)])

def make_readmes():
    mapidoc = json.load(open("mapidoc.json"))
    for path in mapidoc:
        if path == 'mapidoc/materials':
            continue
        path = "mapidoc/materials/" + path.replace(".", "/")
        if path + "/README.md" == 'mapidoc/materials//README.md':
            continue
        newpath = "copy_" + path
        if not os.path.exists(os.path.dirname(newpath)):
            os.makedirs(os.path.dirname(newpath))
            print("making", newpath)
        with open(path + "/README.md", 'r') as orig:
            with open(newpath + "/README.md", 'w') as file:
                file.write(orig.read())
                print(newpath)


def bind(app):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname'), Input('options_selection', 'value')])
    def update_layout(url, option):
        """
        Generates initial layout for app.

        Args:
            url:
            option:

        Returns:

        """
        print("updating layout with {}".format(option))
        return get_readme(option)

    # @app.callback(
    #     Output('output', 'children'),
    #     [Input('field', 'value'), Input('operator', 'value'), Input('value', 'value')])
    # def display_output(field, operator, value):
    #     if field is None:
    #         return '{}'
    #     else:
    #         return format_query_string(field, operator, value)