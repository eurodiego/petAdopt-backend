from flask import jsonify, request
from app.models import Pet

def index():
    return jsonify({'message': 'Hello World API PET-Adopt'})

def create_pet():
    data = request.json
    new_pet = Pet(nombre=data['nombre'], edad=data['edad'], sexo=data['sexo'], tamanio=data['tamanio'], informacion=data['informacion'], banner=data['banner'])
    new_pet.save()
    return jsonify({'message': 'Pet created successfully'}), 201

def get_all_pets():
    pets = Pet.get_all()
    return jsonify([pet.serialize() for pet in pets])

def get_pet(pet_id):
    pet = Pet.get_by_id(pet_id)
    if not pet:
        return jsonify({'message': 'Pet not found'}), 404
    return jsonify(pet.serialize())

def update_pet(pet_id):
    pet = Pet.get_by_id(pet_id)
    if not pet:
        return jsonify({'message': 'Pet not found'}), 404
    data = request.json
    pet.nombre = data['nombre']
    pet.edad = data['edad']
    pet.sexo = data['sexo']
    pet.tamanio = data['tamanio']
    pet.informacion = data['informacion']
    pet.banner = data['banner']
    pet.save()
    return jsonify({'message': 'Pet updated successfully'})

def delete_pet(pet_id):
    pet = Pet.get_by_id(pet_id)
    if not pet:
        return jsonify({'message': 'Pet not found'}), 404
    pet.delete()
    return jsonify({'message': 'Pet deleted successfully'})