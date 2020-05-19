from flask import Flask
from config.config import mongo, MONGO_URI
from controllers.referensi import referensi_blueprint
from controllers.risiko import risiko_blueprint
from controllers.sasaran import sasaran_blueprint

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
mongo.init_app(app)

# register blueprint
app.register_blueprint(referensi_blueprint)
app.register_blueprint(risiko_blueprint)
app.register_blueprint(sasaran_blueprint)