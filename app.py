from utils import occupation
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return "This be my homepage xd"


@app.route("/occupations")
def table():
    return render_template('table.html', title = 'Table of Occupations', collection = occupation.getDict(), randocc = occupation.randomOcc())    

if __name__ == '__main__':
    app.debug = True
    app.run()
    
