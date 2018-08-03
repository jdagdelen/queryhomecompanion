from Old_app.view import make_advanced_query
import json

############# Fields ###############


custom_fields = {
    "mpid":"material_id", "formula": "pretty_formula", "anonymous formula": "snl_final.anonymized_formula",
    "chemical formula": "pretty_formula", "bulk modulus (Voigt)": "elasticity.K_Voigt",
    "bulk modulus (Reuss)": "elasticity.K_Reuss", "bulk modulus (VRH)": "elasticity.K_VRH",
    "bulk modulus (Voigt Reuss Hill)": "elasticity.K_Voigt_Reuss_Hill",
    'shear modulus (Reuss)': 'elasticity.G_Reuss', 'shear modulus (Voigt)': 'elasticity.G_Voigt',
    'shear modulus (VRH)': 'elasticity.G_VRH', 'shear modulus (Voigt Reuss Hill)': 'elasticity.G_Voigt_Reuss_Hill',
    'stability': 'e_above_hull', "energy above hull":"e_above_hull", 'bravais lattice': "spacegroup.crystal_system",
    'crystal system': 'spacegroup.crystal_system', "bandgap": "band_gap",
    "alphabetied formula": 'snl.reduced_cell_formula_abc',
}

#
#
# custom_fields = [
#     {'label': 'mpid', 'value': 'material_id'},
#     {'label': 'formula', 'value': 'pretty_formula'},
#     {'label': 'anonymous formula', 'value': 'snl_final.anonymized_formula'},
#     {'label': 'chemical formula', 'value': 'pretty_formula'},
#     {'label': 'bulk modulus (Voigt)', 'value': 'elasticity.K_Voigt'},
#     {'label': 'bulk modulus (Reuss)', 'value': 'elasticity.K_Reuss'},
#     {'label': 'bulk modulus (VRH)', 'value': 'elasticity.K_VRH'},
#     {'label': 'bulk modulus (Voigt Reuss Hill)', 'value': 'elasticity.K_Voigt_Reuss_Hill'},
#     {'label': 'shear modulus (Reuss)', 'value': 'elasticity.G_Reuss'},
#     {'label': 'shear modulus (Voigt)', 'value': 'elasticity.G_Voigt'},
#     {'label': 'shear modulus (VRH)', 'value': 'elasticity.G_VRH'},
#     {'label': 'shear modulus (Voigt Reuss Hill)', 'value': 'elasticity.G_Voigt_Reuss_Hill'},
#     {'label': 'stability (e_above_hull < 25 meV)', 'value': 'e_above_hull'},
#     {'label': 'energy above hull', 'value': 'e_above_hull'},
#     {'label': 'bravais lattice', 'value': 'spacegroup.crystal_system'},
#     {'label': 'crystal system', 'value': 'spacegroup.crystal_system'},
#     {'label': 'bandgap', 'value': 'band_gap'},
#     {'label': 'alphabetized formula', 'value': 'snl.reduced_cell_formula_abc'},
# ]


def initialize_field_options(fields=custom_fields):
    """ initializes the directory of options that should be displayed for field. """

    mapidoc = json.load(open("mapidoc.json"))

    field_options = [{"label":key, "value":fields[key]} for key in fields]
    for entry in mapidoc:
        if entry is not None and len(entry) > 0 and "@" not in entry:
            entry = entry.replace("/", ".")
            field_options.append({'label': entry, 'value': entry})

    return field_options


def initialize_value_options():
    """ initializes the directory of options that should be displayed for value. """

    value_options = [{'label': "True", 'value': True}, {'label': "False", 'value': False}]
    return value_options

def initialize_operator_options():
    """ initializes the directory of options that should be displayed for operator. """

    operator_options = []
    operators = ["$lt", "$gt", "$lte", "$gte", "$in", "$nin"]
    for entry in operators:
        if entry is not None and len(entry) > 0:
            operator_options.append({'label': entry, 'value': entry})
    return operator_options


# TODO: add logic for filling out questions like is_metal, tetragonal, etc

def create_option_subset(superset, subset):
    """ returns a formatted dropdown options list made up of only allowed options"""
    return None


################## Query Types ####################

query_options = [
    {'label': 'include elements', 'value': 'include_elements'},
    {'label': 'exclude elements', 'value': 'exclude_element'},
    {'label': 'stochiometry is', 'value': 'stoichiometry'},
    {'label': 'chemical formula is', 'value': 'formula'},
    {'label': 'property', 'value': 'property'},
    {'label': 'cystal system (cubic, tetragonal, etc)', 'value': 'cyrstal_stystem'},
    {'label': 'advanced', 'value': 'advanced'},
]


def generate_new_query(query_type):
    """
    Generates a new query element to be added to the query stack.

    Args:
        query_type: (str) type of query. Default is "advanced"

    Returns:
        html.div element for app layout.

    """
    print("query type is", query_type)

    if not query_type:
        return []
    elif query_type == "advanced":
        return make_advanced_query(fields=initialize_field_options(), operators=initialize_operator_options())



# TODO: add logic for filling out questions like is_metal, tetragonal, etc


############# Query String Logic ###############


def format_query_string(field, operation, value):
    query_string = ['"'"{}"'":{}'.format(entry, value) for entry in field]
    query_string = ", ".join(query_string)
    query_string = "{" + query_string + "}"
    return query_string
