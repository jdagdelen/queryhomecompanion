from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html


def get_readme(option):
    if option is None:
        return ""
    path = "mapidoc/materials/" + option.replace(".", "/") +"/README.md"
    with open(path, 'r') as file:
        readme = file.read()
    return html.Div([html.H2(option, style={"color":"teal"}), dcc.Markdown(readme)])

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