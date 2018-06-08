import dash
import dash_html_components as html
import dash_core_components as dcc
import json


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
    {'label': 'bandgap', 'value': 'band_gap'},
]

# TODO: add logic for filling out questions like is_metal, tetragonal, etc

def initialize_options():
    mapidoc = json.load(open("mapidoc.json"))

    for entry in mapidoc:
        if entry is not None and len(entry) > 0 and "@" not in entry:
            entry = entry.replace("/", ".")
            field_options.append({'label': entry, 'value': entry})

    operator_options = []
    operators = ["$lt", "$gt", "$lte", "$gte", "$in", "$nin"]
    for entry in operators:
        if entry is not None and len(entry) > 0:
            operator_options.append({'label': entry, 'value': entry})

    value_options = [{'label': "True", 'value': True}, {'label': "False", 'value': False}]

    return field_options, operator_options, value_options


def format_query_string(field, operation, value):
    query_string = ['"'"{}"'":{}'.format(entry, value) for entry in field]
    query_string = ", ".join(query_string)
    query_string = "{" + query_string + "}"
    return query_string