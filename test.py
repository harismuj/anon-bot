import requests
import json
import keyboard
import os

# Token API bot Anda
TOKEN = '6036728228:AAHmnhauraZJ_t4BewRrjUGGTjIuQfJ0-7I'

# URL dasar untuk endpoint Bot API Telegram
base_url = f"https://api.telegram.org/bot{TOKEN}/"

# Fungsi untuk mengambil pembaruan
def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {'offset': offset}
    response = requests.get(url, params=params)
    return json.loads(response.content.decode('utf-8'))

# Fungsi untuk mengirim pesan
def kirim_pesan(chat_id, teks):
    url = base_url + f"sendMessage"
    params = {'chat_id': chat_id, 'text': teks}
    response = requests.post(url, data=params)
    return response

# Fungsi utama untuk menangani pesan
def handle_message(message):
    text = message['text']
    print(f"Pesan dari User : {text}")
    reply()

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if updates['ok']:
            for update in updates['result']:
                last_update_id = update['update_id'] + 1
                if 'message' in update:
                    handle_message(update['message'])
def reply():
    pesan = input("Masukkan Pesan : ")
    os.system('cls')
    print(f"\nPesan Berhasil Terkirim\nPesan Anda: {pesan}\nID: {chat_id_custom}")
    kirim_pesan(chat_id_custom, pesan)

if __name__ == '__main__':
    # Mengirim pesan
    chat_id_custom = input("Masukkan ID : ")
    reply()
    main()
