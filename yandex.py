import requests


class Yandex:
    def __init__(self):
        self.token = input(str("Введите токен яндекс диска: "))
        self.folder = ''

    def headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth ' + self.token}

    def new_folder(self):
        folder = str(input('Введите имя папки для загрузки на Я.Диск:'))
        self.folder = folder
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": self.folder}
        response = requests.put(url=url, headers=self.headers(), params=params)
        return response

    def upload_from_url(self, url_param, file_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        path = f'{self.folder}/{file_name}'
        if path:
            path = f"{self.folder}/{file_name}.jpg"
        params = {"path": path, "url": url_param}
        response = requests.post(url=url, headers=self.headers(), params=params)
        return response
