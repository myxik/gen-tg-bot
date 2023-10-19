import os
import requests
import psycopg2

from dotenv import load_dotenv
from aiogram.methods.send_photo import SendPhoto
from PIL import Image
from io import BytesIO
load_dotenv()


URL = os.getenv("URL")
url = URL
headers = {
    "accept": "application/json"
}

API_TOKEN = os.getenv("TELEGRAM_TOKEN")
tg_url = f"https://api.telegram.org/bot{API_TOKEN}/"


def call_generation(prompt, chat_id, working_uuid):
    conn = psycopg2.connect("postgresql://postgres:123@localhost/genbot")
    cursor = conn.cursor()

    response = requests.post(url, params={"prompt": prompt.strip()}, headers=headers)
    image = Image.open(BytesIO(response.content))
    img_path = f"/images/{working_uuid}.jpeg"
    image.save(img_path)
    
    update_query = """
    UPDATE data 
    SET current_status = %s, path_to_img = %s 
    WHERE id = %s;
    """

    cursor.execute(update_query, (2, img_path, working_uuid))
    conn.commit()

    cursor.close()
    conn.close()

    # Send picture using chat_id
    SendPhoto(chat_id=chat_id, photo=img_path)
    requests.post(tg_url + 'sendPhoto', data={'chat_id': chat_id}, files={'photo': open(img_path, 'rb')})
