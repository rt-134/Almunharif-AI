import telebot
import requests
import json
import openai
import yaml
from flask import Flask, request

# قراءة إعدادات البوت من ملف config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

bot_token = config["bot_token"]
gpt_api_key = config["gpt_api_key"]

Almunharif1 = telebot.TeleBot(bot_token)
openai.api_key = gpt_api_key

print('تم التشغيل ✅')

Almunharif2 = {
    'Content-Type': 'application/json',
    'X-Mantra-App': 'kong.ai',
    'X-Client-Url': 'https://botup.com/ai-chatbot-app',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://botup.com/ai-chatbot-app',
}

Almunharif3 = {
    'messages': [
        {
            'type': 'system',
            'message': 'Hi, how can I help you today?',
        },
    ],
    'botUUID': '08d13002-af44-4089-a897-8497d0f73120',
    'finger_print': '7299473c-4f99-4321-8ce9-fd59c40867f3',
}

@Almunharif1.message_handler(commands=['start'])
def Almunharif4(Almunharif5):
    user_first_name = Almunharif5.from_user.first_name
    user_last_name = Almunharif5.from_user.last_name
    user_full_name = f"{user_first_name} {user_last_name}" if user_last_name else user_first_name
    user_photos = Almunharif1.get_user_profile_photos(Almunharif5.from_user.id)
    
    if user_photos.total_count > 0:
        user_photo = user_photos.photos[0][-1].file_id  
        Almunharif1.send_photo(Almunharif5.chat.id, user_photo, caption=f"*مرحباً {user_full_name} !*
*أنا بوت الذكاء الاصطناعي 🤖✨ : يمكنك الآن كتابة رسالتك وسارد عليك.*", parse_mode='Markdown')
    else:
        Almunharif1.send_message(Almunharif5.chat.id, f"*مرحباً {user_full_name} !*
*أنا بوت الذكاء الاصطناعي 🤖✨ : يمكنك الآن كتابة رسالتك وسارد عليك.*", parse_mode='Markdown')

@Almunharif1.message_handler(func=lambda message: True)
def handle_messages(message):
    user_message = message.text
    Almunharif1.send_chat_action(message.chat.id, 'typing')
    Almunharif3['messages'].append({
        'type': 'user',
        'message': user_message,
    })
    Almunharif12 = requests.post('https://5664bfwi0joe61lbyyr2jz-oaw.kong.ai/chat/stream', headers=Almunharif2, json=Almunharif3)
    Almunharif13 = ""
    Almunharif14 = Almunharif12.text.splitlines()
    for Almunharif15 in Almunharif14:
        try:
            Almunharif16 = Almunharif15.encode('latin1').decode('utf-8')
            Almunharif17 = json.loads(Almunharif16)
            if 'streaming_response' in Almunharif17 and Almunharif17['streaming_response'].strip():
                Almunharif13 = Almunharif17['streaming_response'].strip()
            elif 'response' in Almunharif17 and Almunharif17['response'].strip():
                Almunharif13 = Almunharif17['response'].strip()
        except (UnicodeDecodeError, json.JSONDecodeError):
            pass
    if Almunharif13:
        Almunharif1.send_message(message.chat.id, Almunharif13)
    else:
        Almunharif1.send_message(message.chat.id, "حدث خطا")

Almunharif1.polling(non_stop=True)
