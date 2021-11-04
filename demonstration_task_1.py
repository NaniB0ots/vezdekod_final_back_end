import base64
from io import BytesIO

import requests

from PIL import Image


def get_formatted_response(response):
    return f'Ответ сервера [{response.status_code}]:  {response.text[:150]}{"..." if len(response.text) > 150 else ""}\n'


def print_menu_actions():
    print('\nМеню:\n'
          '1 - Загрузить изображение\n'
          '2 - Получить изображение\n'
          '3 - Выход\n')


def main():
    api_url = 'http://back.698865-cs07173.tmweb.ru'
    api_port = ''

    if not api_port:
        api_port = '80'

    if api_url[-1] == '/':
        api_url = api_url[:-1]

    print_menu_actions()

    while True:

        action = input('Выберите действие: ')

        if action == '1':
            image_path = input('Введите путь до изображения: ')
            try:
                file = open(image_path, 'rb')
            except:
                print('[Error] Файл не найден')
                continue

            response = requests.post(f'{api_url}:{api_port}/upload/', files={'file': file})
            print(get_formatted_response(response))

        elif action == '2':
            image_id = input('Введите идентификатор изображения: ')
            response = requests.get(f'{api_url}:{api_port}/get/{image_id}')
            print(get_formatted_response(response))

            if response.status_code in [200, 201]:
                try:
                    img = Image.open(BytesIO(base64.b64decode(response.text)))
                    img.show()
                except:
                    print('[Error] Не удалось открыть изображение')

        elif action == '3':
            break
        else:
            print('[Error] Неверное действие.')
            print_menu_actions()


if __name__ == '__main__':
    main()
