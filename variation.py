import openai
import os
import requests
from PIL import Image
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path='.env.dev')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

try:
    generation_response = client.images.create_variation(
        image=open("images/generated-image.png", "rb"),
        n=2,
        size="1024x1024")

    print(generation_response)
    # Image directory
    image_dir = os.path.join(os.curdir, 'images')

    # Create dictionary
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Image path
    image_path = os.path.join(image_dir, 'variation.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # get the image URL
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Open image
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.APIError as err:
    print(err)
