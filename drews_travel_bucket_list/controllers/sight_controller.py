from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.sight import Sight
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

sight_blueprint = Blueprint("sights", __name__)

# INDEX
# Get '/cities'
@sight_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", all_sights = sights)