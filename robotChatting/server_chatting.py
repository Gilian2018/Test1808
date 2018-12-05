import requests

# 向api发送请求
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
    'key'  : "11ce8a607b50469bab70d4664782b766",
    'info'  : msg,
    'userid' : 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        print(r)
        text=r.get('text')
        # print(text)
        url=r.get('url')#股票，油价，列车，图片的链接地址
        # print(url)
        list = r.get('list') #含有菜谱，新闻资讯的链接地址的列表
        if list is not None:
            list_url = list[0]['detailurl']#从列表中提取地址
        else:
            list_url = list
        # print(list_url)
        if url is None:
            if list_url is None:
                return text
            return "%s:%s" % (text, list_url)
        return "%s:%s" % (text, url)
    except:
        # print("request problem")
        return

def auto_chatting(c,msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = "嗯嗯，让我想一想..."
    reply = get_response(msg)
    if reply:
        c.send(reply.encode())
    else:
        c.send(defaultReply.encode())

