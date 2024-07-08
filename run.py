from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

app = Flask(__name__)

# Configurar la aplicación Flask
# app.config.from_pyfile('config/development.py')

# Inicializar la base de datos con la aplicación Flask
init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)
#permitir solicitudes desde un origen específico
# CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})

# Rutas para el CRUD de la entidad Pet
app.route('/', methods=['GET'])(index)
app.route('/api/pets/', methods=['POST'])(create_pet)
app.route('/api/pets/', methods=['GET'])(get_all_pets)
app.route('/api/pets/<int:pet_id>', methods=['GET'])(get_pet)
app.route('/api/pets/<int:pet_id>', methods=['PUT'])(update_pet)
app.route('/api/pets/<int:pet_id>', methods=['DELETE'])(delete_pet)

if __name__ == '__main__':
    app.run(debug=True)