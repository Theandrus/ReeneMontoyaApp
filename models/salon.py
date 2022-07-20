from framework.models import Model


class Salon(Model):
    file = "salons.json"

    def __init__(self, id, location, name, director_id):
        self.id = id
        self.location = location
        self.name = name
        self.director_id = director_id

    def _generate_dict(self):
        super()._generate_dict()
        return {
            'id': self.id,
            'location': self.location,
            'name': self.name,
            'director_id': self.director_id
        }

    def save(self):
        super().save()


