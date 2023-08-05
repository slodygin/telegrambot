import openai
from os import environ
from bot.misc.env import TgKeys
openai.api_key = TgKeys.AI_TOKEN
messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
def generate_text(message):
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    #print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    return reply;

def generate_image(text):
  res = openai.Image.create(
    prompt=text,
    n=1,
    size="512x512",
  )
  # returning the URL of one image as
  # we are generating only one image
  return res["data"][0]["url"]
