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
    api_url = input('Введите адрес сервиса: ')
    api_port = input('Введите порт сервиса (оставить пустым, если 80): ')

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
                with open(image_path, 'rb') as file:
                    response = requests.post(f'{api_url}:{api_port}/upload/', files={'file': file})
                    print(get_formatted_response(response))
            except FileNotFoundError:
                print('[Error] Файл не найден')
                continue

        elif action == '2':
            image_id = input('Введите идентификатор изображения: ')
            scale = input('Введите scale (можно оставить пустым): ')

            response = requests.get(f'{api_url}:{api_port}/get/{image_id}?scale={scale}')
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
