from flask import Blueprint

home_route = Blueprint("home_routes", __name__)

@home_route.route('/')
def index():
    x = 2 + 2
    return f"Hello World! {x}"


@home_route.route("/about")
def about():
    return "About me"
