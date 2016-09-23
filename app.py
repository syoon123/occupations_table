import csv
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return "This be my homepage xd"

d = {}
with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if (row[0] != "Job Class" and row[0] != "Total"):
            d[row[0]] = row[1]

@app.route("/occupations")
def table():
    return render_template('table.html', title = 'Table of Occupations', collection = d)

if __name__ == '__main__':
    app.debug = True
    app.run()
    
