import traceback
from datetime import datetime

from flask_restful import Resource, reqparse
from models.loss_communication import LossCommunicationModel


class LossCommunicationList(Resource):

    ''' Using parse to get just the fields that want update ,look to the json payload and get price for example '''
    # name, email, cpf, location, type_farming, date, event
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('cpf', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('lat', type=float,  required=True)
    parser.add_argument('lng', type=float,  required=True)
    parser.add_argument('type_farming', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('date', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('event', type=int, required=True, help='This field cannot be left blank')


    def get(self):
        """
        Get all the loss communications
        ---
        responses:
          200:
            description: all items
          404:
            description: something goes wrong
        """
        return {'items': list(map(lambda x: x.json(), LossCommunicationModel.query.all()))}

    def post(self):
        """
        Create new loss communication
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                email:
                  type: string
                cpf:
                  type: string
                lat:
                  type: number
                lng:
                  type: number
                type_farming:
                  type: string
                date:
                  type: string
                event:
                  type: integer
        responses:
          201:
            description: loss communication created
          400:
            description: invalid data
        """

        # Create new loss communication
        data = LossCommunicationList.parser.parse_args()
        item = LossCommunicationModel(**data)

        if LossCommunicationModel.already_exists(data['cpf'], data['date']):
            return {'message': "An item with cpf '{}'  and date '{}' already exist.".format(data['cpf'], data['date'])}, 400

        try:
            item.save_to_db()
        except Exception as e:
            traceback.print_exc()
            return {"message": "An error occurend when saving the loss communication"}, 500

        return item.json(), 201

class  LossCommunication(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('cpf', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('lat', type=float,  required=True)
    parser.add_argument('lng', type=float,  required=True)
    parser.add_argument('type_farming', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('date', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('event', type=int, required=True, help='This field cannot be left blank')

    def put(self, id):
        """
        update or create new loss communication
        ---
        parameters:
          - name: id
            in: path
            type: string
            required: true
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                email:
                  type: string
                cpf:
                  type: string
                lat:
                  type: float
                lng:
                  type: float
                type_farming:
                  type: string
                date:
                  type: date
                event:
                  tpye: int
        responses:
          200:
            description: item updated
          400:
            description: invalid data
        """

        # Update some loss communication
        data = LossCommunication.parser.parse_args()
        item = LossCommunicationModel.find_by_id(id)

        if item is None:
            item = LossCommunicationModel(**data)
        else:
            item.name = data['name']
            item.email = data['email']
            item.cpf = data['cpf']
            item.lat = data['lat']
            item.lng = data['lng']
            item.type_farming = data['type_farming']
            item.date = datetime.strptime(data['date'], '%Y-%m-%d')
            item.event = data['event']

        item.save_to_db()
        return item.json()

    def delete(self, id):
        """
        Delete item by id
        ---
        parameters:
          - in: path
            name: id
            type: string
            required: true
        responses:
          200:
            description: item deleted
          404:
            description: item not found
        """

        # Remove loss communication
        item = LossCommunicationModel.find_by_id(id)
        if item:
            item.delete_from_db()
            return {'message': "Item deleted"}
        return {'message': "There is no item with this id."}
