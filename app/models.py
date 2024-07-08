from app.database import get_db

class Pet:
    def __init__(self, id_pet=None, nombre=None, edad=None, sexo=None, tamanio=None, informacion=None, banner=None):
        self.id_pet = id_pet
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.tamanio = tamanio
        self.informacion = informacion
        self.banner = banner

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_pet:
            cursor.execute("""
                UPDATE pet SET nombre = %s, edad = %s, sexo = %s, tamanio = %s, informacion = %s, banner = %s
                WHERE id_pet = %s
            """, (self.nombre, self.edad, self.sexo, self.tamanio, self.informacion, self.banner, self.id_pet))
        else:
            cursor.execute("""
                INSERT INTO pet (nombre, edad, sexo, tamanio, informacion, banner) VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.nombre, self.edad, self.sexo, self.tamanio, self.informacion, self.banner))
            self.id_pet = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pet")
        rows = cursor.fetchall()
        pets = [Pet(id_pet=row[0], nombre=row[1], edad=row[2], sexo=row[3], tamanio=row[4], informacion=row[5], banner=row[6]) for row in rows]
        cursor.close()
        return pets

    @staticmethod
    def get_by_id(pet_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pet WHERE id_pet = %s", (pet_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Pet(id_pet=row[0], nombre=row[1], edad=row[2], sexo=row[3], tamanio=row[4], informacion=row[5], banner=row[6])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM pet WHERE id_pet = %s", (self.id_pet,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_pet': self.id_pet,
            'nombre': self.nombre,
            'edad': self.edad,
            'sexo': self.sexo,
            'tamanio': self.tamanio,
            'informacion': self.informacion,
            'banner': self.banner
        }

