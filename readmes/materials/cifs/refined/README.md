The refined, aka "symmetrized" structure, is a modification of the conventional standard cell to express detected symmetry. Sites are moved relative to the energy-relaxed conventional standard cell. Some theorists prefer this form for "cleaner" band structure calculations.

Uses [pymatgen](http://pymatgen.org/)'s `pymatgen.symmetry.analyzer.SpacegroupAnalyzer` via `pymatgen.io.cifio.CifWriter` (with `symprec=0.1`).

## Example response in JSON

```json
"#\\#CIF1.1\n##########################################################################\n#               Crystallographic Information Format file \n#               Produced by PyCifRW module\n# \n#  This is a CIF file.  CIF has been adopted by the International\n#  Union of Crystallography as the standard for data archiving and \n#  transmission.\n#\n#  For information on this file format, follow the CIF links at\n#  http://www.iucr.org\n##########################################################################\n\ndata_LuAl2\n_symmetry_space_group_name_H-M          'P 1'\n_cell_length_a                          7.76224920492\n_cell_length_b                          7.76224920492\n_cell_length_c                          7.76224920492\n_cell_angle_alpha                       90.0\n_cell_angle_beta                        90.0\n_cell_angle_gamma                       90.0\n_chemical_name_systematic               'Generated by pymatgen'\n_symmetry_Int_Tables_number             1\n_chemical_formula_structural            LuAl2\n_chemical_formula_sum                   'Lu8 Al16'\n_cell_volume                            467.69501895\n_cell_formula_units_Z                   8\nloop_\n  _symmetry_equiv_pos_site_id\n  _symmetry_equiv_pos_as_xyz\n   1  'x, y, z'\n \nloop_\n  _atom_site_type_symbol\n  _atom_site_label\n  _atom_site_symmetry_multiplicity\n  _atom_site_fract_x\n  _atom_site_fract_y\n  _atom_site_fract_z\n  _atom_site_attached_hydrogens\n  _atom_site_B_iso_or_equiv\n  _atom_site_occupancy\n   Lu  Lu1  1  0.125000  0.625000  0.625000  0  .  1\n   Lu  Lu2  1  0.875000  0.875000  0.875000  0  .  1\n   Lu  Lu3  1  0.125000  0.125000  0.125000  0  .  1\n   Lu  Lu4  1  0.875000  0.375000  0.375000  0  .  1\n   Lu  Lu5  1  0.625000  0.625000  0.125000  0  .  1\n   Lu  Lu6  1  0.375000  0.875000  0.375000  0  .  1\n   Lu  Lu7  1  0.625000  0.125000  0.625000  0  .  1\n   Lu  Lu8  1  0.375000  0.375000  0.875000  0  .  1\n   Al  Al9  1  0.500000  0.750000  0.750000  0  .  1\n   Al  Al10  1  0.500000  0.500000  0.500000  0  .  1\n   Al  Al11  1  0.250000  0.000000  0.750000  0  .  1\n   Al  Al12  1  0.250000  0.750000  0.000000  0  .  1\n   Al  Al13  1  0.500000  0.250000  0.250000  0  .  1\n   Al  Al14  1  0.500000  0.000000  0.000000  0  .  1\n   Al  Al15  1  0.250000  0.500000  0.250000  0  .  1\n   Al  Al16  1  0.250000  0.250000  0.500000  0  .  1\n   Al  Al17  1  0.000000  0.750000  0.250000  0  .  1\n   Al  Al18  1  0.000000  0.500000  0.000000  0  .  1\n   Al  Al19  1  0.750000  0.000000  0.250000  0  .  1\n   Al  Al20  1  0.750000  0.750000  0.500000  0  .  1\n   Al  Al21  1  0.000000  0.250000  0.750000  0  .  1\n   Al  Al22  1  0.000000  0.000000  0.500000  0  .  1\n   Al  Al23  1  0.750000  0.500000  0.750000  0  .  1\n   Al  Al24  1  0.750000  0.250000  0.000000  0  .  1\n \n"
```
