
from flask import Flask
from flask_restful import Api, Resource

import json


app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        home = open("home.json", "r")
        homeJson = json.load(home)
        return {"home": homeJson}


class About(Resource):
    def get(self):
        about = open("about.json", "r")
        aboutJson = json.load(about)
        return {"about": aboutJson}


class Shop(Resource):

    def get(self):
        shop = open("shop.json", "r")
        shopJson = json.load(shop)
        return {"shop": shopJson}


api.add_resource(Home, '/v1/home/')
api.add_resource(About, '/v1/about/')
api.add_resource(Shop, '/v1/shop/')

if __name__ == '__main__':
    app.run()
