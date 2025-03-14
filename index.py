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

df1 = atom_data.lines_prepared.reset_index()
df2 = atom_data.levels_prepared.reset_index()

lines_data = df1[df1["atomic_number"] == 14].iloc[:50]
levels_data = df2[df2["atomic_number"] == 14].iloc[:50]

lines_arr = []
levels_arr = []

for index, row in lines_data.iterrows():
    obj = {
        'atomic_number': row['atomic_number'],
        'ion_number': row['ion_number'],
        'level_number_lower': row['level_number_lower'],
        'level_number_upper': row['level_number_upper'],
        'line_id': row['line_id'],
        'wavelength': row['wavelength'],
        'f_ul': row['f_ul'],
        'f_lu': row['f_lu'],
        'nu': row['nu'],
        'B_ul': row['B_ul'],
        'B_lu': row['B_lu'],
        'A_ul': row['A_ul'],
    } 
    lines_arr.append(obj)

for index, row in levels_data.iterrows():
    obj = {
        'atomic_number': row['atomic_number'],
        'ion_number': row['ion_number'],
        'level_number': row['level_number'],
        'energy': row['energy'],
        'g': row['g'],
        'metastable': row['metastable'],
    } 
    levels_arr.append(obj)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("atomic_data.html", levels_arr=levels_arr, lines_arr=lines_arr)

if __name__ == "__main__":
    app.run(debug=True)
