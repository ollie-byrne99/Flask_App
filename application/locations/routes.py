from flask import jsonify, request
from werkzeug import exceptions
from application import app
from .controllers import index, create, show, update, destroy

@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Locations API",
        "endpoints": [
            "GET /"
        ]
    }), 200


@app.route("/locations", methods=["GET", "POST"])
def handle_locations():
    if request.method == "POST":
        return create()
        
    if request.method == "GET":
        return index()


@app.route("/locations/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_location(id):
    if request.method == "GET":
        return show(id)
    
    if request.method == "PATCH":
        return update(id)
    
    if request.method == "DELETE":
        return destroy(id)



@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Oops {err}"}), 500

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f"Oops {err}"}), 400
