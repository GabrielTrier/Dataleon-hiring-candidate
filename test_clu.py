import requests
import pytest
class CLUClient:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_intent(self, query):
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        params = {
            'query': query
        }
        response = requests.post({self.endpoint}, headers=headers, json=params)
        data = response.json()
        if 'prediction' in data and 'topIntent' in data['prediction']:
            return data['prediction']['topIntent']
        else:
            return None

# pytest tests
class TestCLUClient:
    @pytest.fixture
    def clu_client(self):
        api_key = '5aabb484b0924f4f8af0e91a88367824'
        endpoint = 'https://dataleon.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2022-10-01-preview'  
        return CLUClient(api_key, endpoint)

    def test_get_recipe_intent(self, clu_client):
        intent = clu_client.get_intent('What is the recipe for spaghetti?')
        assert intent == 'GetRecipe'

    def test_greeting_intent(self, clu_client):
        intent = clu_client.get_intent('Hello')
        assert intent == 'Greeting'

    def test_goodbye_intent(self, clu_client):
        intent = clu_client.get_intent('Goodbye')
        assert intent == 'Goodbye'
