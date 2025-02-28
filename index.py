# To see the dashboard run "python3 index.py"
# If you want to use the actual atomic file, follow the steps in the comments. 

from flask import render_template, Flask
import pandas as pd

app = Flask(__name__)

path_to_atomic_file = './kurucz_cd23_chianti_Si.h5' # path of the atomic file goes here (can be found in tardis regression data)

# Change the values to empty df when using atomic file
lines_data = pd.read_csv("./lines_df.csv")
levels_data = pd.read_csv("./levels_df.csv")

# Uncomment this once, you've set your path
# with pd.HDFStore(path_to_atomic_file, mode='a') as store:
#     line_df = store.select('/lines_data')
#     line_df = line_df.reset_index()
#     lines_data = line_df.iloc[:50]

#     level_df = store.select('/levels_data')
#     level_df = level_df.reset_index()
#     levels_data = level_df.iloc[:50]


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
        'B_lu': row['B_lu'],
        'B_ul': row['B_ul'], 
        'A_ul': row['A_ul'], 
    } 
    lines_arr.append(obj)

for index, row in levels_data.iterrows():
    obj = {
        'atomic_number': row['atomic_number'],
        'ion_number': row['ion_number'],
        'level_number': row['level_number'],
        'g': row['g'],
        'energy': row['energy'],
        'metastable': row['metastable'],
    } 
    levels_arr.append(obj)


@app.route("/")
def index():
    return render_template("atomic_data.html", lines_arr = lines_arr, levels_arr=levels_arr)


if __name__ == "__main__":
    app.run(debug=True)
