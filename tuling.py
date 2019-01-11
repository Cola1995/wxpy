import requests

KEY='db3aba857d8644588ff0f1b2d69b7382'
def get_response(msg):
    apiUrl = "http://openapi.tuling123.com/openapi/api"
    data = {
            'key' : KEY,
            'info': msg,
            'userid': '991571566',
            }
    try:
        r = requests.post(apiUrl,data).json()
        return '来自小马机器人的回复：'+r.get('text')
    except :
        return "不知道该说什么了"

if __name__=='__main__':
    print(get_response('hiaa'))