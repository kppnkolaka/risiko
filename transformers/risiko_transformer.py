from models.sasaran import Sasaran

class RisikoTransformer:
  __input_schema = {
    "kppn": "156",
    "sasaran_organisasi": "",
    "nomor": "",
    "risiko": {
      "kejadian": "",
      "penyebab": "",
      "dampak": ""
    },
    "kategori": "",
    "sistem_pengendalian": "",
    "kemungkinan_id": "",
    "dampak_id": "",
    "besaran_risiko": {
      "awal": "",
      "akhir": ""
    },
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

  __output_schema = [
    {
      "field": "_id",
      "value": ""
    }, {
      "field": "kppn",
      "value": "156"
    }, {
      "field": "sasaran_organisasi_id",
      "value": ""
    }, {
      "field": "nomor",
      "value": ""
    }, {
      "field": "kategori",
      "value": ""
    }, {
      "field": "sistem_pengendalian",
      "value": ""
    }, {
      "field": "kemungkinan_id",
      "value": ""
    }, {
      "field": "sistem_pengendalian",
      "value": ""
    }, {
      "field": "dampak_id",
      "value": ""
    }, {
      "field": "besaran_risiko",
      "value": ""
    }, {
      "field": "LR",
      "value": ""
    }, {
      "field": "prioritas",
      "value": ""
    }, {
      "field": "keputusan_mitigasi",
      "value": ""
    }, {
      "field": "risiko",
      "value": [
        {
          "field": "kejadian",
          "value": ""
        }, {
          "field": "penyebab",
          "value": ""
        }, {
          "field": "dampak",
          "value": ""
        }
      ]
    }, {
      "field": "risiko_residual",
      "value": [
        {
          "field": "LK",
          "value": ""
        }, {
          "field": "LD",
          "value": ""
        }, {
          "field": "LR",
          "value": ""
        }
      ]
    }, {
      "field": "IRU",
      "value": [
        {
          "field": "nama",
          "value": ""
        }, {
          "field": "batasan_nilai",
          "value": ""
        }
      ]
    }
  ]


  def transform_input(self, form_data):
    if len(form_data) < 7:
      self.__input_schema['nomor'] = form_data['nomor']
      self.__input_schema['sasaran_organisasi'] = Sasaran().show(form_data['sasaran_organisasi_id'])['desc']
      self.__input_schema['besaran_risiko']['awal'] = form_data['awal']
      self.__input_schema['besaran_risiko']['akhir'] = form_data['akhir']
      self.__input_schema['risiko']['kejadian'] = form_data['kejadian']

    return self.__input_schema


  # transform output to easily generate form and table
  def transform_output(self, db_data):
    transformed = []

    for item in db_data:
      temp_list = self.__do_transform(item)      

      transformed.append(temp_list)

    return transformed

  
  def __do_transform(self, transform):
    temp_list = []

    for key, value in transform.items():
      temp_dictionary = {}
      temp_dictionary['field'] = key
      temp_dictionary['value'] = value

      if type(value) is dict:
        temp_dictionary['value'] = self.__do_transform(value)

      temp_list.append(temp_dictionary)

    return temp_list