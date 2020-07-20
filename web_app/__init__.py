from flask import Flask

from web_app.routes.home_routes import home_route
#from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_route)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)