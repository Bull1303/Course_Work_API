from Vkontakte import VK
from yandex import Yandex


def load_from_url(vk, ya):
    vk.get_all_photo()
    default = (input('Введите количество сохраняемых фотографий (По умолчанию 5): '))
    vk.get_top_photo(default)
    counter = 1
    for item in vk.top_photo:
        file_name = str(item['likes'])
        print(f'Загрузка файла {file_name}  {counter} из {len(vk.top_photo)}')
        counter += 1
        ya.upload_from_url(item['url'], file_name)
    print('Загрузка прошла успешно')


def main():
    id_user = input(str('Введите id пользователя: '))
    vk = VK(id_user)
    ya = Yandex()
    ya.new_folder()
    load_from_url(vk, ya)
    vk.json_photo()


if __name__ == '__main__':
    main()
