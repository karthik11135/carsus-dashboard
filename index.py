from flask import render_template, Flask
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
        'ds_id': row['ds_id'],
    } 
    levels_arr.append(obj)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("atomic_data.html", levels_arr=levels_arr, lines_arr=lines_arr)

if __name__ == "__main__":
    app.run(debug=True)
