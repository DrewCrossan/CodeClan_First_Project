class Sight:
    def __init__(self, sight_name, city, description, visited=False, id=None):
        self.sight_name= sight_name
        self.city = city
        self.description = description
        self.visited = visited
        self.id = id

    def mark_visted(self):
        self.visited = True