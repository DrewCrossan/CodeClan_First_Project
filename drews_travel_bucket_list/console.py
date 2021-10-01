import pdb
from models.sight import Sight
from models.city import City
from models.country import Country

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

sight_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Scotland", "Europe", True)
country_repository.save(country1)
country2 = Country("India", "Asia", False)
country_repository.save(country2)

city1 = City("Edinburgh", country1, True)
city_repository.save(city1)
city2 = City("Mumbai", country2, False)
city_repository.save(city2)

sight1 = Sight("Edinburgh Castle", city1, "Old historic castle at the heart of Edinburgh", True)
sight_repository.save(sight1)
sight2 = Sight("Taj Mahal", city2, "Beautiful white temple made of marble. Built hundreds of years ago.", False)
sight_repository.save(sight2)

pdb.set_trace