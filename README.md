# Test-Hiring-candidate
These were the instructions given:
- Create account on Azure and keep API Key
- Create a Python Class to retrieve intent from the Machine Learning LUIS engine
- Write in pytest differents intents from recipe cooking
- Make sure to write the Python test with pytest
- Write ReadME for using

# Usage
## 1. Creating Azure account and getting API key

    Since I had no LUIS resource created beforehand and that since April 2023 we are no longer able to create new LUIS resources, I had to create a new Language resource in the Azure portal.

    This new resource needed to be assinged to the US region since some regions do not have access to the full authoring and prediction.

    After this step done, I was able to create a new projet using the Azure resource that I had just created and obtained my APi key to make API calls.  

    To conclude I'am working with a Conversational Language Understanding (CLU) project in Azure. 

## 2. Using the LUISClient Class

This Python class allows you to interact with the Language Understanding Intelligent Service (LUIS) engine to retrieve intents.

1. Instantiate the LUISClient class with your API key, LUIS app ID, and endpoint.
2. Use the `get_intent(query)` method to retrieve the intent for a given query.

    Example:
    ```python
    from luis_client import LUISClient

    api_key = 'YOUR_API_KEY'
    app_id = 'YOUR_LUIS_APP_ID'
    endpoint = 'YOUR_LUIS_ENDPOINT'

    luis_client = LUISClient(api_key, app_id, endpoint)
    intent = luis_client.get_intent('What is the recipe for spaghetti?')
    print(intent)  # Output: 'GetRecipe'

# Author
- Gabriel Trier 
