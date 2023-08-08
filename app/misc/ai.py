import logging

import openai

from app.misc.env import AI_TOKEN

logger = logging.getLogger(__name__)

openai.api_key = AI_TOKEN
messages = [{"role": "system", "content": "You are a intelligent assistant."}]


def generate_text(message: str | None):
    if message and openai.api_key is not None:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        logger.debug(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
        return reply


def generate_image(text: str | None):
    if text and openai.api_key is not None:
        res = openai.Image.create(
            prompt=text,
            n=1,
            size="512x512",
        )
        # returning the URL of one image as
        # we are generating only one image
        return res["data"][0]["url"]

def edit_image(text: str | None):
        imageName="photo"
        maskName="mask"
        if text and openai.api_key is not None:
          response = openai.Image.create_edit(
            image = open("/home/lodygin/git/telegrambot/{}.png".format(imageName), "rb"),
            mask = open("/home/lodygin/git/telegrambot/{}.png".format(maskName), "rb"),
            prompt = text,
            n = 1,
            size = "1024x1024",
          )
          image_url = response['data'][0]["url"]
          print("image_url=",image_url)
          return image_url

def edit_image2(text: str | None):
        imageName="photo"
        maskName="mask"
        if text and openai.api_key is not None:
          response = openai.Image.create_edit(
            image = open("/home/lodygin/git/telegrambot/{}.png".format(imageName), "rb"),
            mask = open("/home/lodygin/git/telegrambot/{}2.png".format(maskName), "rb"),
            prompt = text,
            n = 1,
            size = "1024x1024",
          )
          image_url = response['data'][0]["url"]
          print("image_url=",image_url)
          return image_url
