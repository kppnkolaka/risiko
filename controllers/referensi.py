from flask import Blueprint, jsonify, request
from models.referensi import referensi

referensi_blueprint = Blueprint('referensi_blueprint', __name__)


@referensi_blueprint.route('/referensi/<kategori>', methods=['GET'])
def index(kategori):
  message = {
    "status": "success",
    "data": {}
  }

  try:
    query_result = referensi(kategori).find()
  except Exception as error:
    message['status'] = error
    return message

  message['data'] = query_result
  return jsonify(message)
  

@referensi_blueprint.route('/referensi/<kategori>', methods=['POST'])
def store(kategori):
  try:
    query_result = referensi(kategori).insert(request.json)
  except Exception as error:
    return {
      "status": error
    }

  return jsonify(query_result)


@referensi_blueprint.route('/referensi/<kategori>', methods=['PUT'])
def update(kategori):
  try:
    # request consist of query and data dict
    query_result = referensi(kategori).update(request.json)
  except Exception as error:
    return {
      "status": error
    }

  return jsonify(query_result)


@referensi_blueprint.route('/referensi/<kategori>', methods=['DELETE'])
def delete(kategori):
  try:
    query_result = referensi(kategori).delete(request.json)
  except Exception as error:
    return {
      "status": error
    }
  
  return jsonify(query_result)