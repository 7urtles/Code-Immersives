from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

with open('/Users/charlesparmley/Documents/PY-122--Django_Flask/class_5--Dynamic_HTML/nato.txt') as f:
    nato_text = f.readlines()

with open('/Users/charlesparmley/Documents/PY-122--Django_Flask/class_5--Dynamic_HTML/countries.txt') as f:
    country_text = f.readlines()
country_text = [line.strip().replace("'",'').split('|') for line in country_text]


@app.route('/')
def dynamic_content():
    name = 'Charles'
    # Flask expects html templates in 'current_app_directory'/templates/
    # In the html, variables go inside a jinja template tag like so:
    #   from the desired route, return the template, and content arguments.
    return render_template('index.html', name=name)


@app.route('/nato')
def nato():
    return render_template('nato.html', lines=nato)


"""
Using countries.txt
Create a database with a table named country_info
Fill the table with data from countries.txt

Create an endpoint called '/getData/Currency' 
- print "The currency of XX is YYYY"
- print "The country XX was not not found"

Create an endpoint called '/getData/Capitals'
- print "The capital of XX is YY"
- print "The capital for XX was not found"
"""


@app.route('/countries')
def countries():
    return render_template('countries.html', countries=country_text)


# Store all the countries from text file into the countries database
@app.route('/store_countries')
def data():
    connection = sqlite3.connect('countries.db')
    cursor = connection.cursor()
    cursor.execute('create table if not exists data (country text, capital text, currency text)')
    for country in country_text:
        cursor.execute('insert into data values(?,?,?)', country)
    connection.commit()
    connection.close()
    return 'True'


# look up a country via url query
@app.route('/find_country/<country>')
def find_country(country):
    connection = sqlite3.connect('countries.db')
    cursor = connection.cursor()
    result = list(cursor.execute('select * from data where country = ?', (country,)).fetchall()[0])
    connection.close()

    if len(result) == 3:
        html_response = f"The currency of {result[0]} is the {result[2]}<br><br>The capital of {result[0]} is {result[1]}"
    else:
        html_response = f"Country {country} not found." 
    return html_response


# display all countries stored in database
@app.route('/show/countries')
def show_country_db():
    connection = sqlite3.connect('countries.db')
    cursor = connection.cursor()
    data = ''
    for row in cursor.execute('select * from data'):
        data += str(row)+ '<br>'
    connection.close()
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)