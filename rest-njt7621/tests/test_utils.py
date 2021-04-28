import requests
import json
from psycopg2.extras import execute_values
from src.db.swen344_db_utils import *

def insert_test_data():
    exec_sql_file('data/schema.sql')
    with open("data/bechdel_test_movies.json", "r") as json_file:
        data = json.load(json_file)
    list_of_tuples = []
    for movie in data:
        list_of_tuples.append((
            movie['id'],
            movie['imdbid'],
            movie['rating'],
            movie['title'],
            movie['year']))
    conn = connect()
    cur = conn.cursor()
    sql = "INSERT INTO movies(id, imdbid, rating, title, year) VALUES %s"
    execute_values(cur, sql, list_of_tuples)
    conn.commit()
    conn.close()

def assert_sql_count(test, sql, n,
                     msg = 'Expected row count did not match query'):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    test.assertEqual(n, cur.rowcount, msg)
    conn.close()

def get_rest_call(test, url, params = {}, expected_code = 200):
    response = requests.get(url, params)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def post_rest_call(test, url, params = {}, expected_code = 200):
    response = requests.post(url, params)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()
