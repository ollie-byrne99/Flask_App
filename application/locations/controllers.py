from .models import Location
from werkzeug import exceptions
from flask import jsonify
from flask import jsonify, request
from .. import db

def index():
    try:
        locations = Location.query.all()
        data = [l.json for l in locations]
        return jsonify({"locations": data})
        
    except:
        raise exceptions.InternalServerError("We are working on it")
    
def create():
    try:
        name = request.json.values()
        new_location = Location(name=name)
            
        db.session.add(new_location)
        db.session.commit()

        return jsonify({"data": new_location.json}), 201

    except:
        raise exceptions.BadRequest(f"We cannot process your request, age, name and catch_phrase are required and you only provided")
    

def show(id):
    try:
        location = Location.query.filter_by(id=id).first()
        return jsonify({"data": location.json}), 200
        
    except:
        raise exceptions.NotFound("You get it")
    
    
def update(id):
    data = request.json
    location = Location.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(location, attribute):
            setattr(location, attribute, value)

    db.session.commit()

    return jsonify({ "data": location.json })

def destroy(id):
    location = Location.query.filter_by(id=id).first()
    db.session.delete(location)
    db.session.commit()
    return f"Location Deleted", 204
