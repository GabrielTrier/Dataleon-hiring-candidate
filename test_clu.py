import pytest
from class_clu import CLUClient

class TestCLUClient:
    @pytest.fixture
    def clu_client(self):
        api_key = '754a1a912e084ef0a3e9eb6fd800361c'
        endpoint = 'https://dataleon.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2022-10-01-preview'  
        return CLUClient(api_key, endpoint)

    # Test the get_intent method
    @pytest.mark.parametrize("query, expected_intent", [
        ('What is the recipe for spaghetti?', 'GetRecipe'),
        ('How to cook a steak?', 'GetRecipe'),
        ('What are the ingredients for a Caesar salad?', 'GetIngredients'),
        ('What do I need to have to make sushi?', 'GetIngredients'),
        ('Can you give me the recipe for a Margherita pizza?', 'GetRecipe'),
        ('What ingredients do I need for a chocolate cake?', 'GetIngredients'),
    ])
    # Define the test_get_intent method
    def test_get_intent(self, clu_client, query, expected_intent):
        intent = clu_client.get_intent(query)
        assert intent == expected_intent
