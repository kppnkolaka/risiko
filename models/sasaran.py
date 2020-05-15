from config.config import mongo
from bson.objectid import ObjectId


class Sasaran:
  __schema = {
    "desc": ""
  }


  def find(self):
    try:
      query = mongo.db.sasaran.find()
    except:
      raise Exception('db connection error')

    parsed_cursor = []

    for parsed in query:
      parsed['_id'] = str(parsed['_id'])
      parsed_cursor.append(parsed)

    return parsed_cursor


  def show(self, string_id):
    try:
      query = mongo.db.sasaran.find_one({"_id": ObjectId(string_id)})
    except:
      raise Exception('db connection error')
    
    parsed_cursor = {
      'desc': ''
    }

    parsed_cursor['_id'] = str(query['_id'])
    parsed_cursor['desc'] = query['desc']

    return parsed_cursor