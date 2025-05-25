# AIAgent-for-beginners

## Random Travel Planner with Azure OpenAI
This Python script generates a random travel destination from a predefined list and uses Azure OpenAI to plan a day trip to that location. It demonstrates how to interact with the Azure OpenAI API using the openai Python package and a custom plugin for random destination selection.

### Features
Picks a random city from a curated list (no repeats).
Generates a travel itinerary using Azure OpenAI (GPT-4o).
Easily customizable and ready for expansion.

### Requirements
Python 3.8+
openai
An Azure OpenAI Service endpoint and API key

### Setup
#### Install dependencies
pip install openai

#### Configure your environment variables
It's recommended to use a .env file to store your secrets. Create a .env file in the root of your project:

AZURE_OPENAI_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_API_VERSION=2024-12-01-preview

Then, update the script to load these variables (e.g. using python-dotenv) or set them directly in your code.

#### Update the script
Replace the placeholders in the script with your actual Azure OpenAI credentials, or load them from your .env.


### Usage
python travel-planner.py
The script will output:
The randomly chosen destination
A detailed day trip itinerary planned by Azure OpenAI


### Customization
Destinations: Edit the self.destinations list in DestinationsPlugin to include your preferred cities.
Prompt: Modify the messages list for different system or user instructions.
API parameters: Adjust temperature, max tokens, or other model settings as needed.

## Credits 
https://github.com/microsoft/ai-agents-for-beginners/tree/main
