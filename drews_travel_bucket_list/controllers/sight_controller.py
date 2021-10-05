from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.sight import Sight
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

sight_blueprint = Blueprint("sights", __name__)

# INDEX
# Get '/sights'
@sight_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", all_sights = sights)

# NEW
# GET '/sights/new'
@sight_blueprint.route("/sights/new", methods=['GET'])
def new_sight():
    cities = city_repository.select_all()
    return render_template("sights/new.html", all_cities = cities)

# CREATE
# POST '/sights'
@sight_blueprint.route("/sights",  methods=['POST'])
def create_sight():
    name = request.form['sight_name']
    city_id = request.form['city_id']
    description = request.form['description']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    sight = Sight(name, city, description, visited)
    sight_repository.save(sight)
    return redirect('/sights')

# SHOW
# GET '/sights/<id>'
@sight_blueprint.route("/sights/<id>")
def show_sight(id):
    sight = sight_repository.select(id)
    return render_template('sights/show.html', sight=sight)

# EDIT
# GET '/sights/<id>/edit'
@sight_blueprint.route("/sights/<id>/edit", methods=['GET'])
def edit_sight(id):
    sight = sight_repository.select(id)
    cities = city_repository.select_all()
    return render_template('sights/edit.html', sight = sight, all_cities = cities)

# UPDATE
# PUT '/sights/<id>'
@sight_blueprint.route("/sights/<id>", methods=['POST'])
def update_sight(id):
    name = request.form['sight_name']
    city_id = request.form['city_id']
    description = request.form['description']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    sight = Sight(name, city, description, visited, id)
    sight_repository.update(sight)
    return redirect('/sights')

# DELETE
# DELETE '/sights/<id>'
@sight_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sights(id):
    sight_repository.delete(id)
    return redirect('/sights')