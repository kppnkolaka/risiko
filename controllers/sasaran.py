from flask import Blueprint, jsonify, request
from models.sasaran import Sasaran

sasaran_blueprint = Blueprint('sasaran_blueprint', __name__)


@sasaran_blueprint.route('/sasaran', methods=['GET'])
def index():
  message = {
    "status": "success",
    "data": {}
  }

  try:
    query_result = Sasaran().find()
  except Exception as error:
    message['status'] = error
    return message

  message['data'] = query_result
  return jsonify(message)