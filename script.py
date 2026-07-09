import os
from time import sleep

import requests
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    devman_token = os.environ['DEVMAN_TOKEN']
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    first_connection = True
    while True:
        try:
            chat_id = bot.get_updates()[-1].message.chat_id
        except telegram.error.TelegramError:
            if first_connection:
                first_connection = False
                continue
            sleep(5)
            continue

        API_DEVMAN = 'https://dvmn.org/api/long_polling/'
        headers = {'Authorization': devman_token}
        params = {}

        try:
            response = requests.get(
                url=API_DEVMAN,
                headers=headers,
                params=params,
                timeout=90,
                )
            response.raise_for_status()
            response_data = response.json()
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            sleep(5)
            continue
        if response_data.get('status') == 'timeout':
            params['timestamp'] = response_data.get('timestamp_to_request')
            continue
        if response_data.get('status') == 'found':
            job_name = response_data['new_attempts'][0]['lesson_title']
            result_of_validate = response_data['new_attempts'][0]['is_negative']
            lesson_url = response_data['new_attempts'][0]['lesson_url']
            bot.send_message(
                chat_id=chat_id,
                text=f'У вас проверили работу "{job_name}"\n'
                     f'{'Работа не принята' if result_of_validate else 'Работа принята'}\n'
                     f'Ссылка на урок: {lesson_url}')


if __name__ == '__main__':
    main()