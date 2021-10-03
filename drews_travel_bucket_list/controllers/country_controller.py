from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_blueprint = Blueprint("countries", __name__)

# INDEX
# Get Countries
@country_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)

# SHOW
# GET '/countries/<id>'
@country_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country=country)

# DELETE
# DELETE '/countries/<id>'
@country_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')