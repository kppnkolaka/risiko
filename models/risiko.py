from config.config import mongo

class Risiko:
  __schema = {
    "kppn": "156",
    "sasaran_organisasi": "#REF",
    "risiko": {
      "nomor": "",
      "kejadian": "",
      "penyebab": "",
      "dampak": ""
    },
    "kategori": "",
    "sistem_pengendalian": "",
    "kemungkinan": "#REF",
    "dampak": "#REF",
    "besaran_risiko": "",
    "LR": "",
    "prioritas": "",
    "risiko_residual": {
      "LK": "",
      "LD": "",
      "LR": ""
    },
    "keputusan_mitigasi": "",
    "IRU": {
      "nama": "",
      "batasan_nilai": ""
    }
  }


  def store(self, risiko_object):
    try:
      mongo.db.kemungkinan.insert(risiko_object)
    except:
      raise Exception('db connection error')

    return {
      "status": "success"
    }