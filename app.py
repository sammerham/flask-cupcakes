"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/api/cupcakes")
def list_all_cupcakes():
    """Return JSON {'cupcakes': [{id, flavor, size, rating}, ...]}"""
    cupcakes = Cupcake.query.all()
    serliaized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serliaized)
 