from pprint import pprint
import requests
import os

token ='my_token_here'
file_path = 'C:/Новая папка/test.txt'

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }

    def _get_upload_link(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        disk_file_path = 'Загрузки' + '/' + os.path.split(os.path.basename(file_path))[1]
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self):
        href = self._get_upload_link().get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        else:
            print(response.status_code)
        return

if __name__ == '__main__':
    ya = YaUploader(file_path)
    ya.upload()


