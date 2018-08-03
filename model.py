import json

############# Fields ###############


custom_fields = {
    "mpid": "material_id", "structure": "structure", "pretty_formula (i.e. formula, chemical formula)": "pretty_formula",
    "anonymous formula": "snl_final.anonymized_formula", "bulk modulus (Voigt)": "elasticity.K_Voigt",
    "bulk modulus (Reuss)": "elasticity.K_Reuss", "bulk modulus (VRH)": "elasticity.K_VRH",
    "bulk modulus (Voigt Reuss Hill)": "elasticity.K_Voigt_Reuss_Hill",
    'shear modulus (Reuss)': 'elasticity.G_Reuss', 'shear modulus (Voigt)': 'elasticity.G_Voigt',
    'shear modulus (VRH)': 'elasticity.G_VRH', 'shear modulus (Voigt Reuss Hill)': 'elasticity.G_Voigt_Reuss_Hill',
    'e_above_hull (i.e. stability, energy above hull)': 'e_above_hull', "energy above hull": "e_above_hull",
    'spacegroup.crystal_system (bravais lattice, crystal system)': "spacegroup.crystal_system",
    "band_gap (i.e. bandgap)": "band_gap", "band_structure (i.e. electronic structure)": "band_structure",
    "snl.reduced_cell_formula_abc (alphabetized formula)": 'snl.reduced_cell_formula_abc',
    "dos (i.e. density of states, electronic structure)": "dos",
}


def initialize_field_options(fields=custom_fields):
    """ initializes the directory of options that should be displayed for field. """

    mapidoc = json.load(open("mapidoc.json"))

    field_options = [{"label": key, "value": fields[key]} for key in fields]
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
