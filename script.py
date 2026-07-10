import logging
import os
from time import sleep

import requests
import telegram
from dotenv import load_dotenv


logger = logging.getLogger(__file__)


def main():
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('script.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Running')
    
    load_dotenv()
    devman_token = os.environ['DEVMAN_TOKEN']
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    first_connection = True

    while True:
        try:
            chat_id = bot.get_updates()[-1].message.chat_id
        except telegram.error.TelegramError as err:
            logger.warning('%s', err)
            if first_connection:
                first_connection = False
                continue
            sleep(5)
            continue

        api_devman = 'https://dvmn.org/api/long_polling/'
        headers = {'Authorization': devman_token}
        params = {}

        try:
            response = requests.get(
                url=api_devman,
                headers=headers,
                params=params,
                timeout=90,
                )
            response.raise_for_status()
            serialized_response = response.json()
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError as err:
            logger.warning('%s' % (err))
            sleep(5)
            continue
        if serialized_response.get('status') == 'timeout':
            params['timestamp'] = serialized_response.get('timestamp_to_request')
            continue
        if serialized_response.get('status') == 'found':
            job_name = serialized_response['new_attempts'][0]['lesson_title']
            result_of_validate = serialized_response['new_attempts'][0]['is_negative']
            lesson_url = serialized_response['new_attempts'][0]['lesson_url']
            bot.send_message(
                chat_id=chat_id,
                text=f'У вас проверили работу "{job_name}"\n'
                     f'{'Работа не принята' if result_of_validate else 'Работа принята'}\n'
                     f'Ссылка на урок: {lesson_url}')


if __name__ == '__main__':
    main()
