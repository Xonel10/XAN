import urllib3
import json
from urllib3.exceptions import InsecureRequestWarning
from logging import exception

# 禁用安全请求警告
urllib3.disable_warnings(InsecureRequestWarning)


# 从网络获取获取html地址
def getfaceData(imgurl):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    # 实例化-获取对象
    http = urllib3.PoolManager()
    # 根据url获取反馈的html代码
    #     url = 'http://www.3gosc.com'
    data = {}
    data['api_key'] = 'xWlLauJypmj9dGfoXRCAs_HXgZjWEXv4'
    data['api_secret'] = '9OkiL5ABPB0SdR9RWrINzslLm2BTh0Ja'
    data[
        'image_url'] = imgurl  # 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1352792673,1568148854&fm=27&gp=0.jpg'
    data[
        'return_attributes'] = 'gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus'
    r = http.request('POST', url, fields=data)
    #     urllib3.PoolManager().request("POST",url, fields=data)
    print(r.status)
    # 返回的网络码（200代表成功）
    if 200 == r.status:
        html = str(r.data, 'utf-8')
        try:
            json_data = json.loads(html)
            # print(json_data)
            return json_data
        except Exception as e:
            print(e)
            return None
    else:
        print('获取数据失败！！')
        return None


def strFormat(data):
    retdata = data['faces'][0]['attributes']
    ret = ''
    if 'Male' == retdata['gender']['value']:
        ret += '性别:男性'
    else:
        ret += '性别:女性'
    ret += '\n'

    ret += '年龄:' + str(retdata['age']['value']) + '岁'
    ret += '\n'

    ret += ('微笑指数:' + str(retdata['smile']['value']))
    ret += '\n'

    #     if 'anger' == retdata['emotion']:
    #         ret +='心情:愤怒'
    #     elif 'disgust' == retdata['emotion']:
    #         ret +='心情:厌恶'
    #     elif 'fear' == retdata['emotion']:
    #         ret +='心情:恐惧'
    #     elif 'happiness' == retdata['emotion']:
    #         ret +='心情:高兴'
    #     elif 'neutral' == retdata['emotion']:
    #         ret +='心情:平静'
    #     elif 'sadness' == retdata['emotion']:
    #         ret +='心情:伤心'
    #     elif 'surprise' == retdata['emotion']:
    #         ret +='心情:惊讶'
    #     ret+='\n'

    if 'Asian' == retdata['ethnicity']['value']:
        ret += '人种:亚洲人'
    elif 'White' == retdata['ethnicity']['value']:
        ret += '心情:白人'
    elif 'Black' == retdata['ethnicity']['value']:
        ret += '心情:黑人'
    ret += '\n'

    if 'None' == retdata['glass']['value']:
        ret += '眼镜:不佩戴眼镜'
    elif 'Dark' == retdata['glass']['value']:
        ret += '眼镜:佩戴墨镜'
    elif 'Normal' == retdata['glass']['value']:
        ret += '眼镜:佩戴普通眼镜'
    ret += '\n'

    return ret


def getFaceInfoStr(url):
    try:
        ret = getfaceData(url)
        #     print(ret)
        if 0 == len(ret['faces']):
            return None
        per = strFormat(ret)
        print(per)
        return per
    except:
        return None

# getFaceInfoStr('https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1787138323,3973940258&fm=27&gp=0.jpg')