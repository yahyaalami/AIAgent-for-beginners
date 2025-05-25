# Azure OpenAI Travel Visualization Agent

This Python script demonstrates how to use Azure OpenAI with environment variables managed by `python-dotenv`. It randomly selects a travel destination and prompts Azure OpenAI to generate a bar chart from sample data, showcasing both language and code-generation abilities.

## Features

- Loads credentials securely from a `.env` file.
- Picks a random city from a curated list (no repeats).
- Uses Azure OpenAI (e.g., GPT-4o) for natural language and data visualization prompts.
- Example prompt included for generating a bar chart using sample travel data.

## Requirements

- Python 3.8+
- [`openai`](https://pypi.org/project/openai/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- An Azure OpenAI Service endpoint and API key

## Setup

### Install dependencies
pip install openai python-dotenv


### Configure your environment variables
Create a .env file in the root of your project:
AZURE_OPENAI_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_API_VERSION=2024-12-01-preview


### Run the script
python travel_visualization_agent.py


## Usage
The script will:
Select a random destination from the list (different each run).
Ask Azure OpenAI to create a bar chart using sample traveler data.
Print the AI’s response, which may include code or a chart description.


## Customization
Destinations: Edit the self.destinations list in DestinationsPlugin to include your preferred cities.
Prompt: Modify the user_query variable to ask Azure OpenAI for different data visualizations or travel-related tasks.
API parameters: Adjust temperature, max_tokens, or other settings for different outputs.