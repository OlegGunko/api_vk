from urllib.parse import urlencode
import requests


# OAUTH_URL = 'https://oauth.vk.com/authorize'
# OAUTH_PARAMS = {
#      'client_id': 7491505,
#      'user_id': 17871293,
#      'display': 'page',
#      'scope': 'friends',
#      'response_type': 'token',
#
#      'v': '5.107'
#  }

# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

TOKEN = '875aba11fda5d732ebd859f7e72787535f8a59c250f6781e2638808db6fdee93a1e0dee841e273da2f30f'

# response = requests.get('https://api.vk.com/method/users.get?user_id=17871293&',
#                         params={'access_token': TOKEN, 'v': 5.107})

class User:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def __str__(self):
        return str(f'https://vk.com/id{self.user_id}')

    def get_id(user):
        resp = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': TOKEN,
                'user_id': user.user_id,
                'v': 5.107
            }
        )
        return resp.json()['response']['items']

    def __and__(self, user):
        first_user_id = set(self.get_id())
        second_user_id = set(user.get_id())
        mutual_friends = list(first_user_id & second_user_id)
        print(f'Список общих друзей пользователей:\n{mutual_friends}')
        return mutual_friends


user_1 = User(TOKEN, int(input(f'Введите id пользователя:\n')))
user_2 = User(TOKEN, int(input(f'Введите id пользователя:\n')))

user_1 & user_2

print(f'\nСсылка на профиль пользователя:\n{user_1}')

17871293
21657824
