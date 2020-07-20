from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)

#Configuration moving debug from the bottom.
app.config['DEBUG'] = True
#Cookie
app.config['SECRET_KEY'] = 'Thisisasecret!'

# App.route is a function of Flask that will run the underlying function when parameter is called.
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={"name":"User"})
@app.route('/home/<name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name)

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

        #return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)
        return redirect(url_for('home', name=name, Location=location))
    
# This will take a JSON process and will respond
@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['location']
    location = data['randomlist']

    return jsonify({'result': 'Success', 'name': name, 'location': location, 'randomkeyinlist': randomlist[1]})

if __name__ == "__main__":
    app.run()