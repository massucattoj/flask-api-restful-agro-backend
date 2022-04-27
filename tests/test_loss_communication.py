import json
import unittest

from db import db
from flask import Flask


class LossCommunicationTest(unittest.TestCase):
    def populate_db(self):
        pass

    def setUp(self):
        #self.app = app.test_client()
        #self.db = db.create_all()
        #self.db = db.init(app)
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
            self.populate_db() # Your function that adds test data.

        self.payload = json.dumps({
            "name": "new test",
            "email": "test@example.com",
            "cpf": "12345678976",
            "lat": -52.7548945,
            "lng": -26.197678,
            "type_farming": "soja",
            "date": "2022-01-01",
            "event": 3
        })

    def test_successful_loss_communication(self):
        payload = self.payload
        response = self.app.post('/loss_communication', headers={"Content-Type": "application/json"}, data=payload)
        print('aaa', response)

        #self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        # for collection in db.list_collection_names():
        #     self.db.drop_collection(collection)
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()
