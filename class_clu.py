import requests
import uuid

class CLUClient:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_intent(self, query):
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        participant_id = str(uuid.uuid4()) 
        data = {
            'kind': 'Conversation',
            'analysisInput': {
                'conversationItem': {
                    'id': participant_id,
                    'text': query,
                    'modality': 'text',
                    'language': 'en',
                    'participantId': participant_id
                }
            },
            'parameters': {
                'projectName': 'dataleonProject',
                'verbose': True,
                'deploymentName': 'DataLeonRecipeCooking',
                'stringIndexType': 'TextElement_V8'
            }
        }
        response = requests.post(self.endpoint, headers=headers, json=data)
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}: {response.content}")
            return None
        data = response.json()
        if 'result' in data and 'prediction' in data['result'] and 'topIntent' in data['result']['prediction']:
            return data['result']['prediction']['topIntent']
        else:
            print(f"Response does not contain 'result', 'prediction', or 'topIntent': {data}")
            return None
