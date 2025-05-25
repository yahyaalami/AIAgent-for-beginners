import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import random

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # "gpt-4o-mini"
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# Plugin pour la destination aléatoire
class DestinationsPlugin:
    def __init__(self):
        self.destinations = [
            "Barcelona, Spain", "Paris, France", "Berlin, Germany", "Tokyo, Japan",
            "Sydney, Australia", "New York, USA", "Cairo, Egypt",
            "Cape Town, South Africa", "Rio de Janeiro, Brazil", "Bali, Indonesia"
        ]
        self.last_destination = None

    def get_random_destination(self):
        available = [d for d in self.destinations if d != self.last_destination]
        destination = random.choice(available)
        self.last_destination = destination
        return destination

plugin = DestinationsPlugin()
destination = plugin.get_random_destination()

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

# Tu peux changer ce prompt pour tout ce que tu veux :
user_query = f"Could you please create a bar chart for the operating profit using the following data and provide the file to me? Bali: 100 Travelers, Paris: 356 Travelers, London: 900 Travelers, Tokyo: 850 Travellers"

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful agent that can write code and generate visualizations.",
        },
        {
            "role": "user",
            "content": user_query,
        }
    ],
    max_tokens=1024,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print("Réponse de l'agent :\n")
print(response.choices[0].message.content)

