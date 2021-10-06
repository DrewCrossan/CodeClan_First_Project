from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_blueprint = Blueprint("cities", __name__)

# INDEX
# Get '/cities'
@city_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

# NEW
# GET '/cities/new'
@city_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)

# CREATE
# POST '/cities'
@city_blueprint.route("/cities",  methods=['POST'])
def create_city():
    name = request.form['city_name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect('/cities')

# SHOW
# GET '/cities/<id>'
@city_blueprint.route("/cities/<id>")
def show_city(id):
    # country = country_repository.select(id)
    city = city_repository.select(id)
    sights = city_repository.sights(city)
    return render_template('cities/show.html', city=city, all_sights=sights)

# EDIT
# GET '/cities/<id>/edit'
@city_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city = city, all_countries = countries)

# UPDATE
# PUT '/cities/<id>'
@city_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['city_name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect('/cities')

# DELETE
# DELETE '/cities/<id>'
@city_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

