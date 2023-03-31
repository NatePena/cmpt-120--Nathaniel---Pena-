# import the flask package for making rest apis.
from flask import *
from movies import movies

# create an instance of a Flask object.
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    '''
    This is our base route. When visited, we get the text "Hello, world!"
    '''
    return "Hello, world!"


@app.route("/api/movies", methods=["GET"])
def list_movies():
    """
    This function returns a Response object back containing all
    of stored movies and reviews back to the caller on the web.

    This function is filterable by a movie title query parameter.
    """
    response_body = []

    # get the movie title query parameter.
    titles = request.args.getlist("title")
    print(titles)

    # only get the movies that have the same title as the query parameter.
    if titles:
        for movie in movies:
            if movie["title"] in titles:
                response_body.append(movie)
    else:
        response_body = movies

    return jsonify(response_body)


if __name__ == '__main__':
    app.run()
