import openai

# Set up OpenAI API key
openai.api_key = "YOUR-API-KEY-HERE"

# Test API key
models = openai.Model.list()
print(models)
