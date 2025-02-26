#########################################
######### Importing Lib and Modules #####
#########################################
import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import ADDForm, DelForm
from hidden_info import *

#########################################
######### Flask App Configuration #######
#########################################

db = SQLAlchemy(app)

#########################################
############## Models ###################
#########################################

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Puppy Name: {self.name}'


#########################################
######## VIEWS FUNCTIONS - HAVE FORMS ####
#########################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_form():
    form = ADDForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        
        if pup:  # Ensure the puppy exists before deleting
            db.session.delete(pup)
            db.session.commit()
        else:
            return "Puppy not found!", 404  # Return a proper response
        
        return redirect(url_for('list_pup'))

    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
