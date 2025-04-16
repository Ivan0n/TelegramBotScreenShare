import pyscreenshot
import telebot
import time
from datetime import datetime
from PIL import ImageDraw, ImageFont
from telebot import types

bot = telebot.TeleBot('Token')

def make_screenshot_with_time():
    
    image = pyscreenshot.grab()

    draw = ImageDraw.Draw(image)
    time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        font = ImageFont.truetype("arial.ttf", 70)
    except:
        font = ImageFont.load_default()

    draw.text((10, 10), time_str, fill="red", font=font)
    draw.text((10, 1080), "github.com/Ivan0n", fill="white", font=ImageFont.truetype("arial.ttf", 30))

    image.save("screenshot.png")

@bot.message_handler(commands=['start'])
def start(starter):
    make_screenshot_with_time()
    with open('screenshot.png', 'rb') as photo:
        sent_msg = bot.send_photo(starter.chat.id, photo)

    while True:
        make_screenshot_with_time()
        with open('screenshot.png', 'rb') as photo:
            media = types.InputMediaPhoto(photo)
            try:
                bot.edit_message_media(media, chat_id=starter.chat.id, message_id=sent_msg.message_id)
            except Exception as e:
                print("Ошибка при редактировании фото:", e)

bot.polling(non_stop=True)