import requests

SERVER_IP = "IP"
API_SERVER = "http://" + SERVER_IP + ":5000"
DOWNLOAD_IMAGE_API = "/upload"

try:
    downloadImageInfoResponse = requests.get(
        API_SERVER + DOWNLOAD_IMAGE_API)

    if downloadImageInfoResponse.status_code == 200:
        with open('img.jpg', 'wb') as getFile:
            getFile.write(downloadImageInfoResponse.content)
except Exception as err:
    print('Other error occurred %s' % {err})