from config.config import mongo

class Risiko:
  def find(self):
    try:
      query = mongo.db.risiko.find()
    except:
      raise Exception('db connection error')
    
    parsed_cursor = []

    for parsed in query:
      parsed['_id'] = str(parsed['_id'])
      parsed_cursor.append(parsed)

    return parsed_cursor


  def store(self, risiko_object):
    try:
      mongo.db.risiko.insert(risiko_object)
    except:
      raise Exception('db connection error')

    return {
      "status": "success"
    }

  
  def update(self, risiko_update):
    try:
      mongo.db.risiko.update(
        risiko_update['query'],
        {
          "$set": risiko_update['data']
        }
      )
    except:
      raise Exception('db connection error')

    return {
      "status": "success"
    }


  def delete(self, delete_criteria):
    try:
      mongo.db.risiko.delete_one(delete_criteria)
    except:
      raise Exception('db connection error')

    return {
      "status": "success"
    }