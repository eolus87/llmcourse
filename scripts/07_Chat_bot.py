"""
All the code in this py file is coming from the ChatGPT Prompt Engineering
for Developers Course from DeepLearning.ai:
https://learn.deeplearning.ai/chatgpt-prompt-eng
"""

# Standard libraries
import os

# Third party libraries
import openai

# Custom libraries

openai.api_key = os.getenv('OPENAI_API_KEY')


# Common prompt function used in the previous scripts
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


messages = [
    {'role': 'system', 'content': 'You are an assistant that speaks like Shakespeare.'},
    {'role': 'user', 'content': 'tell me a joke'},
    {'role': 'assistant', 'content': 'Why did the chicken cross the road'},
    {'role': 'user', 'content': 'I don\'t know'}]

response = get_completion_from_messages(messages, temperature=1)
print(response)

# To Create a chatbot, we just need to create a function that gathers all messages, correclty labelling
# if it was coming from the user, the system or the chatbot.
# Additionally, it requires an intro for the chatbot to know which role is playing and the instructions
# it should follow.
