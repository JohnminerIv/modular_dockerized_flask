from dotenv import load_dotenv
load_dotenv("../.env") 
from flask import Flask, send_from_directory
import os


# Database
from src.database.mongodb import db
# Modules
from src.blueprints.auth import routes as auth
from src.blueprints.landing_page import routes as landing_page

def create_app(modules):
    app = Flask(__name__, template_folder="shared_templates", static_folder='shared_static')
    for module in modules:
        app.register_blueprint(module.bp)
    return app

application = app = create_app([auth, landing_page])
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'shared_static'),
                               'img/favicon.jpeg', mimetype='image/vnd.microsoft.icon')
if __name__ == '__main__':
    app.run(debug=True)