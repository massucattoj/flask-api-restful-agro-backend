import enum
from datetime import datetime

from db import db
from sqlalchemy_utils import ChoiceType


class EventType(enum.Enum):
    excessive_rain = 1
    frost = 2
    hail = 3
    dry = 4
    gale = 5
    lightning = 6

EventType.excessive_rain.label = 'Chuva Excessiva'
EventType.frost.label = 'Geada'
EventType.hail.label = 'Granizo'
EventType.dry.label = 'Seca'
EventType.gale.label = 'Vendaval'
EventType.lightning.label = 'Raio'


class LossCommunicationModel(db.Model):
    __tablename__ = 'loss_communications'

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    lat = db.Column(db.Float(10))
    lng = db.Column(db.Float(10))
    type_farming = db.Column(db.String(100))
    date = db.Column(db.DateTime())
    event = db.Column(ChoiceType(EventType, impl=db.Integer()))

    def __init__(self, name, email, cpf, lat, lng, type_farming, date, event):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.lat = lat
        self.lng = lng
        self.type_farming = type_farming
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.event = event

    def json(self):
        return {'name': self.name, 'email': self.email, 'cpf': self.cpf, 'lat': self.lat, 'lng': self.lng, 'type_farming': self.type_farming, 'date': datetime.strftime(self.date, '%Y-%m-%d'), 'event': self.event.label}

    @classmethod
    def already_exists(cls, cpf, date):
        return cls.query.filter(cls.cpf == cpf, cls.date == datetime.strptime(date, '%Y-%m-%d')).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
