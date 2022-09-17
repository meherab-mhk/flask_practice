from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/stdinfo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secrect_key = 'secret'

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    roll = db.Column(db.String(255), nullable=False)
    section = db.Column(db.Integer(), nullable=0)
    intake = db.Column(db.Integer(), nullable=0)
    department = db.Column(db.String(10), nullable=False)

    def __init__(self, name, roll, section, intake, department):
        self.name = name
        self.roll = roll
        self.section = section
        self.intake = intake
        self.department = department


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/addstudent")
def addstudent():
    return render_template("form.html")


@app.route("/studentadd", methods=['POST'])
def studentadd():
    name = request.form["name"]
    roll = request.form["roll"]
    section = request.form["section"]
    intake = request.form["intake"]
    department = request.form["department"]
    entry = People(name, roll, section, intake, department)
    db.session.add(entry)
    db.session.commit()

    return render_template("success.html")

if __name__ == '__main__':
    db.create_all()
    app.run()