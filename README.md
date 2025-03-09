## GSOC First Objective task
Objective : Use Jinja2 to generate an HTML Report that investigates an atomic file. Display top 50 rows of levels and lines dataframes from the atomic file for Silicon

Using jinja2 I displayed the required tables.
When you run `python3 index.py` and go to http://127.0.0.1:5000/, you'll be able to see the top 50 levels and lines atomic data for Silicon atom. 

If you do not have the gfall.dt file, install it using
`wget -qO /tmp/gfall.dat https://media.githubusercontent.com/media/tardis-sn/carsus-db/master/gfall/gfall_latest.dat`

