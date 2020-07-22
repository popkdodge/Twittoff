from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3
app = Flask(__name__)

#Configuration moving debug from the bottom.
app.config['DEBUG'] = True
#Cookie
app.config['SECRET_KEY'] = 'Thisisasecret!'

# Connect to database
def connect_db():
    sql = sqlite3.connect('intro_data.sqlite3')
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#close the database
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# App.route is a function of Flask that will run the underlying function when parameter is called.
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={"name":"User"})
@app.route('/home/<name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    db = get_db()
    select = """
    SELECT ID, name, location from name
    """
    cur = db.execute(select)
    results = cur.fetchall()

    return render_template('home.html', name=name, display=True, mylist=['one', 'two', 'three', 'four'], listofdictionaries=[{'name': 'Zach'}, {'name': 'Zoe'}], results = results)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'Not in session!'
    return jsonify({"key": "value", "key2":[1,2,3,4], 'name': name})

# This will return query for ie. website/query?name={name}&location={location}
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f"<h1> Hi {name}. You are from {location}.You are on the query page! </h1>"

# This will return a form that will also POST form.
@app.route('/theform', methods=['GET', 'POST'])
def theform():
    
    if request.method == 'GET':
        return render_template('form.html') 
    else:
        name = request.form['name']
        location = request.form['location']
        db = get_db()
        insert = f"""
        INSERT into name (name, location)
        VALUES (?, ?)
        """
        db.execute(insert, [name, location])
        db.commit()
        #return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)
        return redirect(url_for('home', name=name, Location=location))
    
# This will take a JSON process and will respond
@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['location']
    location = data['randomlist']

    return jsonify({'result': 'Success', 'name': name, 'location': location, 'randomkeyinlist': randomlist[1]})
# This will show result of my database
@app.route('/viewresults')
def viewresults():
    db = get_db()
    select_query = """
    SELECT *
    FROM name
    """
    cur = db.execute(select_query)
    results = cur.fetchall()
    return f"<h1>{results[0][4]} is from {results[0][4]}.</h1>"

if __name__ == "__main__":
    app.run()