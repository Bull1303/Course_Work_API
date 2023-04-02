import json
import requests


class VK:

    def __init__(self, id_user, version='5.81'):
        self.token = (input(str("Введите токен Вконтакте: ")))
        self.id = id_user
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
        self.pic_list = []
        self.top_photo = []
        self.likes = []
        self.dates_list = []

    def size_variable(self, size):
        # lst = [[0,'w'],[1,'z'],[2,'y'],[3,'r'],[4,'q'],[5,'p'],[6,'o'],[7,'x'],[8,'m'],[9,'s']]
        if size == 'w':
            return 0
        if size == 'z':
            return 1
        if size == 'y':
            return 2
        if size == 'r':
            return 3
        if size == 'q':
            return 4
        if size == 'p':
            return 5
        if size == 'o':
            return 6
        if size == 'x':
            return 7
        if size == 'm':
            return 8
        if size == 's':
            return 9

    def get_all_photo(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile', 'extended': '1', 'rev': '1'}
        response = requests.get(url, params={**self.params, **params}).json()
        response = response["response"]["items"]
        for sizes in response:
            temp_list = []
            like = sizes['likes']['count']
            date_ = sizes['date']
            self.dates_list.append(date_)
            for i in sizes['sizes']:
                temp_list.append([self.size_variable(i['type']), i['type'], i['url']])
            temp_list.sort()
            self.pic_list.append([temp_list[0][0], temp_list[0][1], temp_list[0][2], like])
        print(f"Доступно к скачиванию {len(self.pic_list)} фотографий!")
        return self.pic_list

    def get_top_photo(self, default):
        if not default:
            default = 5
        else:
            default = int(default)
        if len(self.pic_list) < default:
            default = len(self.pic_list)
        for i in range(default):
            like = self.pic_list[i][3]
            if like not in self.likes:
                self.likes.append(like)
            else:
                like_date = f"{like}-{self.dates_list[i]}"
                self.likes.append(like_date)
            url = self.pic_list[i][2]
            size = self.pic_list[i][1]
            dic = {'size': size, 'url': url, 'likes': self.likes[i]}
            self.top_photo.append(dic)
        return self.top_photo

    def json_photo(self):
        temp_list = []
        for i in self.likes:
            file_name = i
            for item in self.top_photo:
                size = str(item['size'])
            dic = {'file_name': file_name, 'size': size}
            temp_list.append(dic)
        new_json = json.dumps(temp_list, indent=2)
        with open('output.json', 'w') as file:
            file.write(new_json)
        return True
