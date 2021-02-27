import unittest
import json

from app import app

class TestApi(unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Steve Malkmus is a good band"})
            assert response._status_code == 200

    def test_ner_given_json_body_with_named_entities_returns_entity_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Kamala Harris"})
            data = json.loads(response.get_data())
            assert data['entities'][0]['ent'] == 'Kamala Harris'
            assert data['entities'][0]['label'] == 'Person'


