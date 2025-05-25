import os
import random
from openai import AzureOpenAI

# Variables (mets-les dans un .env si tu veux)
endpoint = "https://ai-agent-pfe-resource.cognitiveservices.azure.com/"
deployment = "gpt-4o-mini"
subscription_key = "TA_CLE_API_ICI"  # <--- remplace par ta clé
api_version = "2024-12-01-preview"

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
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful travel assistant.",
        },
        {
            "role": "user",
            "content": f"Plan me a day trip to {destination}.",
        }
    ],
    max_tokens=512,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(f"Destination choisie : {destination}\n")
print(response.choices[0].message.content)
