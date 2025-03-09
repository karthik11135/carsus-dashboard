# To see the dashboard run "python3 index.py"
# If you want to use the actual atomic file, follow the steps in the comments. 

from flask import render_template, Flask
import pandas as pd
from carsus.io.nist import NISTWeightsComp, NISTIonizationEnergies
from carsus.io.kurucz import GFALLReader
from carsus.io.zeta import KnoxLongZeta
from carsus.io.output import TARDISAtomData

zeta_data = KnoxLongZeta()

ionization_energies = NISTIonizationEnergies('H-Zn')
atomic_weights = NISTWeightsComp()

gfall_reader = GFALLReader('H-Zn',
                           '/tmp/gfall.dat')

atom_data = TARDISAtomData(atomic_weights,
                           ionization_energies,
                           gfall_reader,
                           zeta_data,)


app = Flask(__name__)

lines_data = atom_data.lines_all.reset_index()[:50]
levels_data = atom_data.levels_all.reset_index()[:50]


lines_arr = []
levels_arr = []

for index, row in lines_data.iterrows():
    obj = {
        'line_id': row['line_id'],
        'lower_level_id': row['lower_level_id'],
        'upper_level_id': row['upper_level_id'],
        'wavelength': row['wavelength'],
        'gf': row['gf'],
        'loggf': row['loggf'],
        'ds_id': row['ds_id'],
        # 'level_number_upper': row['level_number_upper'],
        # 'wavelength': row['wavelength'],
        # 'f_ul': row['f_ul'],
        # 'f_lu': row['f_lu'],
        # 'nu': row['nu'],
        # 'B_lu': row['B_lu'],
        # 'B_ul': row['B_ul'], 
        # 'A_ul': row['A_ul'],   
    } 
    lines_arr.append(obj)

for index, row in levels_data.iterrows():
    obj = {
        'index': row['index'],
        'level_id': row['level_id'],
        'atomic_number': row['atomic_number'],
        'ion_number': row['ion_number'],
        'g': row['g'],
        'energy': row['energy'],
        # 'metastable': row['metastable'],
        'ds_id': row['ds_id'],
    } 
    levels_arr.append(obj)


@app.route("/")
def index():
    return render_template("atomic_data.html", levels_arr=levels_arr, lines_arr=lines_arr)

if __name__ == "__main__":
    app.run(debug=True)
