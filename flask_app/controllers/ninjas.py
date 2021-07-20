from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos = dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/ninjas')

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all_dojos()
    for dojo in dojos:
        print(dojo.id)
    return render_template("dojos.html", dojos = dojos)

@app.route('/dojos/<int:dojo_id>/show')
def show_one_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.show_one_dojo(data)
    ninjas = Ninja.get_ninjas_by_dojo(data)
    return render_template('show_dojo.html', dojo = dojo, ninjas = ninjas)


@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')