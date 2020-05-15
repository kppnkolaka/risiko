from config.config import mongo

class Dampak():
  __schema = {
    "kppn": "156",
    "level": "",
    "level_desc": "",
    "area_dampak": {
      "fraud": "",
      "non_fraud": ""
    },
    "reputasi": [],
    "sanksi": "",
    "kecelakaan": "",
    "gangguan": "",
    "kinerja": ""
  }


  def find(self):
    try:
      query = mongo.db.dampak.find()
    except:
      raise Exception('db connection error')
  
    parsed_cursor = []

    for parsed in query:
      parsed['_id'] = str(parsed['_id'])
      parsed_cursor.append(parsed)

    return parsed_cursor


  def insert(self, dampak_object):
    try:
      mongo.db.dampak.insert(dampak_object)
    except:
      raise Exception('db connection error')
    
    return {
      "status": "success"
    }


  def update(self, dampak_object):
    try:
      mongo.db.dampak.update(dampak_object['query'], dampak_object['data'])
    except:
      raise Exception('db connection error')
    
    return {
      "status": "success"
    }

  def delete(self, delete_criteria):
    try:
      mongo.db.dampak.delete_one(delete_criteria)
    except:
      raise Exception('db connection error')

    return {
      "status": "success"
    }