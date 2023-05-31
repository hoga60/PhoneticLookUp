import openai

def read( api_key, word ):
    openai.api_key = api_key 

    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      temperature = 0.2,
      max_tokens = 100,
      messages = [
        {"role": "user", "content": word }
      ]
    )

    return (response['choices'][0]['message']['content'])
    