import requests
import time
import csv

# Данная программа собирает со стены группы все записис с наибольшими лайками
def take_1000_posts():
    token = 'fcff139cfcff139cfcff139ce5fc8cd84bffcfffcff139ca3aa582c0de1169945c5396e'
    version = 5.92  # Прописываем версию API VK
    domain = 'fit4life_official'  # Пишем адрес группы
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                params = {
                    'access_token':token,
                    'v': version,
                    'domain': domain,
                    'count': count,
                    'offset': offset
                    }
                    )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts

def file_writer(data):
    with open('fit4life.csv','w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow('likes', 'body', 'url')
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow((post['likes']['count'], post['text'], img_url))

all_posts = take_1000_posts()
file_writer(all_posts)

print(1)