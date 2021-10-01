from db.run_sql import run_sql

from models.country import Country
from models.city import City
from models.sight import Sight

import repositories.city_repository as city_repository


def save(sight):
    sql = "INSERT INTO sights (sight_name, city_id, description, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [sight.sight_name, sight.city.id, sight.description, sight.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight


def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['sight_name'], city, row['description'], row['visited'], row['id'])
        sights.append(sight)
    return sights


def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        sight = Sight(result['sight_name'], city, result['description'], result['visited'], result['id'])
    return sight


def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(sight):
    sql = "UPDATE sights SET (sight_name, city_id, description, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [sight.sight_name, sight.city.id, sight.description, sight.visited, sight.id]
    run_sql(sql, values)

