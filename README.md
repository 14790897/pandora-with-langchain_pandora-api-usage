English | [简体中文](README.cn.md)

# Pandora ChatGPT API Integration for Langchain (customize-longchain-LLm.py)

This project saves the cost of using the GPT-4 API by integrating the Pandora project to call the ChatGPT web version as an API and using it in conjunction with Langchain's custom language model.

## Features

- Call the ChatGPT web version's API
- Use custom. language model to implement ChatGPT's functionality
- Optional stop list support

## Code examples

```python
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
import uuid
import requests
import json
from pydantic import BaseModel
import os
from tool import other_tools

class CustomChatGPT(LLM).
    ...

if __name__ == "__main__".
    llm = CustomChatGPT(base_url="your url") # need to build the pandora application on the server itself
    response = llm("This is a foobar thing")
```

## How to use

1. Deploy the Pandora project to your server. 2.
2. Replace `your url` with your server URL. 3.
3. Instantiate the `CustomChatGPT` class. 4.
4. Call the `_call` method (also known as llm("prompt")), pass in the relevant parameters and get the returned message.

## Caution

- Make sure your server has successfully deployed the Pandora project.
- When using the `_call` method, make sure you pass in the correct parameters, such as prompt, stop, etc.

# Pandora ChatGPT API Integration for Langchain - additional content (pandora-usage.py)

This project not only provides integration with Pandora, but also introduces basic usage of Pandora.

## Pandora Basic Usage

The following code provides some basic Pandora usage, including

- List available models
- List sessions in a paginated manner
- Deleting all sessions
- Get the details of a given session by its session ID
- Deleting a specified session by session ID
- Set the specified session title by session ID
- Automatically generate a title for a specified new session
- Have ChatGPT regenerate replies
- Allow ChatGPT to continue the previous recovery
- Ask ChatGPT a question and wait for a reply

```python
import requests
import json
import uuid

# base_url = "https://your-api-domain" # Replace with your API domain name

# List the models available for the account
def list_models().
    ...

# List the conversations in a paginated manner
def list_conversations(offset=1, limit=20).
    ...

# Delete all conversations
def delete_all_conversations().
    ...

# Get the details of a given session by its session ID
def get_conversation(conversation_id).
    ...

# Delete the specified conversation by its session ID
def delete_conversation(conversation_id).
    ...

# Set the specified session title by the session ID
def set_conversation_title(conversation_id, title).
    ...

# Automatically generate the title of the specified new session
def generate_conversation_title(conversation_id, model, message_id).
    ...

# Make ChatGPT regenerate replies
def regenerate_chatgpt(prompt, model, message_id, parent_message_id, conversation_id, stream=True).
    ...

# Let ChatGPT continue with the previous recovery
def continue_chatgpt(model, parent_message_id, conversation_id, stream=True).
    ...

# Ask ChatGPT a question and wait for a reply
def ask_chatgpt(prompt, model, message_id, parent_message_id, conversation_id=None, stream=False).
    ...

def ask().
    ...

def main().
    ...

if __name__ == "__main__".
    main()
```

## Usage

1. Replace `base_url` with the domain name of your API.
2. Call the corresponding function to perform the corresponding operation.

## Caution

- Please make sure your API domain name is configured correctly.
- When calling the function, please make sure to pass the correct parameters.

## Contributors

Feel free to contribute to this project! Please submit an issue or pull request on GitHub.

Translated with www.DeepL.com/Translator (free version)