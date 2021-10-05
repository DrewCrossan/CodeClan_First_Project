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
country3 = Country("Australia", "Oceania", True)
country_repository.save(country3)
country4 = Country("Italy", "Europe", False)
country_repository.save(country4)
country5 = Country("USA", "North America", True)
country_repository.save(country5)
country6 = Country("Peru", "South America", False)
country_repository.save(country6)
country7 = Country("Eygpt", "Africa", False)
country_repository.save(country7)


city1 = City("Edinburgh", country1, True)
city_repository.save(city1)
city2 = City("Mumbai", country2, False)
city_repository.save(city2)
city3 = City("Glasgow", country1, True)
city_repository.save(city3)
city4 = City("New Delhi", country2, False)
city_repository.save(city4)
city5 = City("Melbourne", country3, True)
city_repository.save(city5)
city6 = City("Sydney", country3, True)
city_repository.save(city6)
city7 = City("Rome", country4, False)
city_repository.save(city7)
city8 = City("Bologna", country4, False)
city_repository.save(city8)
city9 = City("Orlando", country5, True)
city_repository.save(city9)
city10 = City("Las Vegas", country5, False)
city_repository.save(city10)
city11 = City("Lima", country6, False)
city_repository.save(city11)
city12 = City("Cusco", country6, False)
city_repository.save(city12)
city13 = City("Cairo", country7, False)
city_repository.save(city13)
city14 = City("Giza", country7, False)
city_repository.save(city14)




sight1 = Sight("Edinburgh Castle", city1, "Old historic castle at the heart of Edinburgh", True)
sight_repository.save(sight1)
sight2 = Sight("Taj Mahal", city2, "Beautiful white temple made of marble. Built hundreds of years ago.", False)
sight_repository.save(sight2)
sight3 = Sight("Kelvingrove Art Gallery and Museum", city3, "Free Entry. Kelvingrove Art Gallery and Mu​seum is Scotland's most visited free attraction.​ With 22 themed, state-of-the-art galleries displaying an astonishing 8000 objects, the collections are extensive, wide-ranging and internationally-significant.", False)
sight_repository.save(sight3)
sight4 = Sight("Swaminarayan Akshardham", city4, "Fantastic site to visit - unimaginable architechture, great theme show, diaorama and I max presentation. If any tourist, irresepctive of his religion or creed, has half a day to spare, this is a must see. It is one man's creation in five years totally with voluntary support. A monument which makes every indian proud!", False)
sight_repository.save(sight4)
sight5 = Sight("Royal Botanic Gardens Victoria", city5, "Over 10,000 plant species from around the world are presented in a kaleidoscope of colour and texture. Sweeping lawns, tranquil lakes and majestic trees are home to an amazing range of wildlife.", True)
sight_repository.save(sight5)
sight6 = Sight("Sydney Opera House", city6, "One of the most iconic buildings in the world – the Sydney Opera House is an architectural masterpiece and vibrant performance space.", True)
sight_repository.save(sight6)
sight7 = Sight("Pantheon", city7, "Dedicated to the seven planetary divinities and featuring an interior of gorgeous marble, the Pantheon is one of the most impressive monuments of Augustan Rome.", False)
sight_repository.save(sight7)
sight8 = Sight("Piazza Maggiore", city8, "The Centre of Bologna to meet or stroll or sit with drink or visit many of the historic sites surrounding The Piazza. Should be first stop when you arrive for first time.", False)
sight_repository.save(sight8)
sight9 = Sight("Disney Land", city9, "Covering nearly 47 square-miles, the Walt Disney World Resort features four theme parks: Epcot, Magic Kingdom Park, Disney’s Animal Kingdom Park and Disney's Hollywood Studios, two water parks: Disney's Blizzard Beach and Disney's Typhoon Lagoon and over 20 resort hotels.", True)
sight_repository.save(sight9)
sight10 = Sight("The Strip", city10, "Main city strip. Lots to see.", False)
sight_repository.save(sight10)
sight11 = Sight("Museo Larco", city11, "The Museo Larco is housed in an exquisite 18th century vice-royal mansion, built over a 7th century pre-Columbian pyramid and surrounded by beautiful gardens.", False)
sight_repository.save(sight11)
sight12 = Sight("Sacsayhuaman", city12, "Fascinating rock walls built by Inca people just outside of Cusco. Tour guides are available at the entrance, but you can do a self-guided tour as well. There is a breathtaking view of Cusco as well from this high vantage point.", False)
sight_repository.save(sight12)
sight13 = Sight("The Museum of Egyptian Antiquities", city13, "This famous museum houses the world’s largest collection of ancient Egyption artifacts (more than 120,000 items on display) featuring the famous Tutankhamun collection with its beautiful gold death mask and sarcophagus and the royal Mummy room, which houses an additional eleven Pharaonic dignitaries.", False)
sight_repository.save(sight13)
sight14 = Sight("Pyramids of Giza", city14, "Perhaps the most recognizable among the Seven Wonders of the World, the exact origin of these majestic pyramids continues to spark debate.", False)
sight_repository.save(sight14)

pdb.set_trace