import os 
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from flask_migrate import Migrate
from forms import AddForm, AddOwnerForm, DelForm
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import MetaData

Base = declarative_base()
#metadata = MetaData()
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1A2s3D4f5G6h7J8k9L0z1Z2x3C4v5B6n7M@localhost/adoption'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)
#####################################

rel_table = db.Table('rel_table', 
        # db.Column('id', db.Integer, primary_key = True),
        db.Column('pup_id', db.Integer, db.ForeignKey('puppies.pup_id', primary_key = True)),
        db.Column('owner_id', db.Integer, db.ForeignKey('owners.owner_id'))
        )


class Puppy(db.Model):

    __tablename__ = 'puppies'

    pup_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    breed = db.Column(db.Text, nullable = False)
    owner_id = db.relationship('Owner', backref = 'owner')
    following = db.relationship('Owner', secondary = rel_table, backref = 'followers')


    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        if self.owner_id:
            return f"Puppy {self.name} is a {self.breed} that is {self.age} year/s old and their owner is {self.owner_id}"
        else:
            return f"Puppy {self.name} is a {self.breed} that is {self.age} year/s old and they have no owner yet! Their ID is {self.pup_id}"


class Owner(db.Model):

    __tablename__ = 'owners'

    owner_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.pup_id'))
    #following = db.relationship('Puppy', secondary = rel_table, backref = 'followers')

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Owner Name: {self.name}, Owner ID: {self.owner_id}'


db.create_all()
# VIEW FUNCTIONS 

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods = ['GET','POST'])
def add_pup():

    form=AddForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        breed = form.breed.data
        # toy = form.breed.data
        new_pup = Puppy(name, age, breed)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('add.html', form = form)

@app.route('/add_owner', methods = ['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('owner_list'))
    
    return render_template('add_owner.html', form=form)

@app.route('/list')
def list_pup():
    
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods = ['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form = form)

@app.route('/owner_list')
def owner_list():

    owners = Owner.query.all()
    return render_template('owner_list.html', owners=owners)

# @app.route('/add_toys', methods = ['GET', 'POST'])
# def add_toy():

#     form = AddPupsToys()

#     if form.validate_on_submit():
#         item_name = form.item_name.data
#         pup_id = form.pup_id.data
#         new_toy = Toy(item_name, pup_id)
#         db.session.add(new_toy)
#         db.session.commit()

#         return redirect(url_for('list_pup'))
    
#     return render_template('add_toy.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)