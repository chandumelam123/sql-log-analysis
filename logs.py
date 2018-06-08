#! /usr/bin/env python

import psycopg2

database = "news"

# Query for top articles
query1 = """
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
"""

# Query for top authors
query2 = """
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 4;
    """
# Query for errors
query3 = """
        SELECT total.day,
        ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
"""


def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    db = psycopg2.connect('dbname=' + database)
    connect = db.cursor()
    connect.execute(query)
    rows = connect.fetchall()
    db.close()
    return rows

# returns top three articles of all time


def top_articles():
    # Stores Query results in query_result object
    query_result = run_query(query1)

# Print Results
    print('\nTop 3 articles of all time')
    count = 1
    for x in query_result:
        number = '(' + str(count) + ') "'
        title_of_article = x[0]
        views = '" --- ' + str(x[1]) + " views"
        print(number + title_of_article + views)
        count += 1

# returns top three authors of all time


def top_authors():
    query_result = run_query(query2)

# Print Results
    print('\nTop authors of all time')
    count = 1
    for y in query_result:
        print('(' + str(count) + ') ' + y[0] + ' --- ' + str(y[1]) + " views")
        count += 1

# returns days with more than 1% error


def days_with_errors():
    query_result = run_query(query3)

# Print Results
    print('\nDays with more than one percentage of bad requests')
    for z in query_result:
        date_of_error = z[0].strftime('%B %d, %Y')
        errors = str(round(z[1]*100, 1)) + "%" + " errors"
        print(date_of_error + " -- " + errors)

top_articles()
top_authors()
days_with_errors()
