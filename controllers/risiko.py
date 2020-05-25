from flask import Blueprint, jsonify, request
from models.risiko import Risiko
from models.sasaran import Sasaran
from transformers.risiko_transformer import RisikoTransformer

risiko_blueprint = Blueprint('risiko_blueprint', __name__)


@risiko_blueprint.route('/risiko', methods=['GET'])
def index():
  message = {
    "status": "success",
    "data": {}
  }

  try:
    query_result = Risiko().find()
  except Exception as error:
    message['status'] = error
    return message
  
  # transform = RisikoTransformer().transform_output(query_result)

  message['data'] = query_result
  return jsonify(message)


@risiko_blueprint.route('/risiko', methods=['POST'])
def store():
  transform = RisikoTransformer().transform_input(request.json)

  try:
    query_result = Risiko().store(transform)
  except Exception as error:
    return {
      "status": error
    }

  return jsonify(query_result)


@risiko_blueprint.route('/risiko', methods=['PUT'])
def update():
  try:
    # request consist of query and data dict
    query_result = Risiko().update(request.json)
  except Exception as error:
    return {
      "status": error
    }

  return jsonify(query_result)


@risiko_blueprint.route('/risiko', methods=['DELETE'])
def delete():
  try:
    query_result = Risiko().delete(request.json)
  except Exception as error:
    return {
      "status": error
    }
  
  return jsonify(query_result)