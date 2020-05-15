from config.config import mongo

class Kemungkinan:
  __schema = {
    "kppn": "required",
    "level": "required",
    "level_desc": "required",
    "kriteria": {
      "persentase": "required",
      "jumlah": "required"
    },
    "low_tolerance": "required"
  }


  def find(self):
    try:
      query = mongo.db.kemungkinan.find()
    except:
      raise Exception('db connection error')
    
    parsed_cursor = []

    for parsed in query:
      parsed['_id'] = str(parsed['_id'])
      parsed_cursor.append(parsed)

    return parsed_cursor


  def insert(self, kemungkinan_object):
    try:
      mongo.db.kemungkinan.insert(kemungkinan_object)
    except:
      raise Exception('db connection error')
    
    return {
      "status": "success"
    }


  def update(self, kemungkinan_object):
    try:
      mongo.db.kemungkinan.update(kemungkinan_object['query'], kemungkinan_object['data'])
    except:
      raise Exception('db connection error')
    
    return {
      "status": "success"
    }

  def delete(self, delete_criteria):
    try:
      mongo.db.kemungkinan.delete_one(delete_criteria)
    except:
      raise Exception('db connection error')

    return {
      "status": "success"
    }