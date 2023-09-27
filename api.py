import json
import requests
from settings import Credentials


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_registration(self) -> json:
        """Запрос к Swagger сайта для регистрации пользователя"""
        data = {"email": 'iaqaQaQaQ@gmail.com',
                "password": '1234', "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json()
        my_id = my_id.get('id')
        status = res.status_code
        print(my_id)
        return status, my_id

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": Credentials.VALID_EMAIL,
                "password": Credentials.VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        print(my_token)
        print(res.json())
        return my_token, status, my_id

    def get_list_users(self):
        """Запрос к Swagger сайта для получения списка пользователей"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json

        print(res.json())
        return status, amount

    def post_pet(self):
        """Запрос к Swagger сайта для создания питомца"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"name": 'Eleven', "type": 'cat', "age": 21, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        print(pet_id)
        print(res.json())
        return pet_id, status

    def post_pet_photo(self):
        """Запрос к Swagger сайта для добавления фото питомцу"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        # pic = open('tests\\photo\\1.jpg', 'rb')
        files = {'pic': ('pic.jpg', open('./tests/photo/raccon.jpg', 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        print(res.json())
        return status, link

    def put_pet_like(self):
        """Запрос к Swagger сайта для создания питомца и добавления Like"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        print(res.json())
        return status

    def put_pet_comment(self):
        """Запрос к Swagger сайта для создания питомца и добавления комментария"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"message": 'Best cat'}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def get_pet_info(self):
        """Запрос к Swagger сайта для получения информации о питомце"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        pet_info = res.json()
        return status, pet_id, pet_info

    def update_pet_type(self):
        """Запрос к Swagger сайта для изменения типа питомце"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_info = Pets().get_pet_info()[2]
        pet_info['pet']['type'] = pet_info['pet']['type'] = 'raccoon'
        res = requests.patch(self.base_url + 'pet', headers=headers, data=json.dumps(pet_info['pet']))
        status = res.status_code
        print(status)
        return status

    def post_pet_list(self):
        """Запрос к Swagger сайта для получения списка питомцев по типу"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"type": 'cat', "user_id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        list_info = res.json()
        amount = res.json()['total']
        return status, list_info, pet_id, amount

    def delete_pet(self):
        """Запрос к Swagger сайта для удаления питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def delete_all_pets(self):
        """Запрос к Swagger сайта для удаления всех питомцев"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        list_info = Pets().post_pet_list()[1]
        print(list_info)
        for i in list_info['list']:
            pet_id = i["id"]
            res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def delete_user(self):
        """Запрос к Swagger сайта для удаления пользователя"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, data=data)
        status = res.status_code
        return status, my_id


# Pets().get_registration()
# Pets().get_token()
# Pets().get_list_users()
# Pets().post_pet()
# Pets().post_pet_photo()
# Pets().put_pet_like()
# Pets().put_pet_comment()
# Pets().get_pet_info()
# Pets().update_pet_type()
# Pets().post_pet_list()
# Pets().delete_pet()
# Pets().delete_all_pets()
# Pets().delete_user()
