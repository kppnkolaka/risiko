from flask import Blueprint, jsonify, request
from models.risiko import Risiko
from models.sasaran import Sasaran

risiko_blueprint = Blueprint('risiko_blueprint', __name__)


@risiko_blueprint.route('/risiko', methods=['GET'])
def index():
  return jsonify(Sasaran().find())


@risiko_blueprint.route('/risiko/<id>', methods=['GET'])
def show(id):
  return jsonify(Sasaran().show(id))


@risiko_blueprint.route('/risiko', methods=['POST'])
def store():
  return None


@risiko_blueprint.route('/risiko', methods=['PUT'])
def update():
  return None


@risiko_blueprint.route('/risiko', methods=['DELETE'])
def delete():
  return None