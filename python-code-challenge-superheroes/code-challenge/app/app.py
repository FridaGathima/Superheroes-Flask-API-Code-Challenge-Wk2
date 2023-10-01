#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api, Resource, reqparse
from models import db, Hero, HeroPower, Power
from flask_migrate import Migrate
from flask import request, app, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from serializer import response_serializer2, response_serializer1



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


# @app.route('/')
# def home():
#     return 'Welcome to My Superheroes API'
parser = reqparse.RequestParser()
parser.add_argument('strength')
parser.add_argument('power_id')
parser.add_argument('hero_id')

class Index(Resource):
    def get(self):
        response = {
            "index": "Welcome to my Superheroes Api"
        }
        return make_response(jsonify(response))
api.add_resource(Index, '/')

class HeroesList(Resource):
    def get(self):
        heroes = Hero.query.all()
        response = response_serializer2(heroes)
        return make_response(jsonify(response), 200)

api.add_resource(HeroesList, '/heroes')

class HeroesId(Resource):
    def get(self, id):
        hero = Hero.query.filter_by(id=id).first()
        if hero:
            powers = [{"id": power.id, "name": power.name, "description": power.description} for power in hero.powers]
            response = {
                "id":hero.id,
                "name":hero.name,
                "super_name":hero.super_name,
                "powers": powers
            }
            return make_response(jsonify(response), 200 )
        else: 
            return make_response(jsonify({"error": "Hero not found"}), 404 ) 

api.add_resource(HeroesId, '/heroes/<int:id>')

class PowersList(Resource):
    def get(self):
        powers = Power.query.all()
        response = response_serializer1(powers)
        return make_response(jsonify(response), 200)

api.add_resource(PowersList, '/powers')

class PowersId(Resource):
    def get(self, id):
        power = Power.query.filter_by(id=id).first()
        if power:
            response = {
                "id":power.id,
                "name":power.name,
                "description":power.description,
            }
            return make_response(jsonify(response), 200 )
        else: 
            
            return (make_response(jsonify({"error": "Hero not found"}), 404 ))

api.add_resource(PowersId, '/powers/<int:id>')


if __name__ == '__main__':
    app.run(port=5555)

