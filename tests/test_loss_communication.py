import json
import unittest

from app import app
from db import db


class LossCommunicationTest(unittest.TestCase):
    def populate_db(self):
        pass

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        db.init_app(self.app)
        with app.app_context():
            db.create_all()
            self.populate_db()  # Your function that adds test data.

        self.payload = json.dumps({
            "name": "new test",
            "email": "test@example.com",
            "cpf": "12345678976",
            "lat": "-52.7548945",
            "lng": "-26.197678",
            "type_farming": "soja",
            "date": "2022-01-01",
            "event": 3
        })

    def test_successful_loss_communication(self):
        payload = self.payload
        response = self.client.post('/loss_communication', headers={'content-type': 'application/json'}, data=payload)
        self.assertEqual(201, response.status_code)

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
