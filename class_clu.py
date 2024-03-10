import requests

class LanguageClient:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_intent(self, query):
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        data = {
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "id": "PARTICIPANT_ID_HERE",
                    "text": query,
                    "modality": "text",
                    "language": "en"
                }
            },
            "parameters": {
                "projectName": "dataleonProject",
                "verbose": True,
                "deploymentName": "DeploymentDataleon",
                "stringIndexType": "TextElement_V8"
            }
        }
        response = requests.post(f'{self.endpoint}/language/:analyze-conversations?api-version=2022-10-01-preview', headers=headers, json=data)
        data = response.json()
        print(data)
        if 'prediction' in data and 'topIntent' in data['prediction']:
            return data['prediction']['topIntent']
        else:
            return None
