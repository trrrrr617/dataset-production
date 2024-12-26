from neo4j import GraphDatabase
import json
import requests


key = ("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=DXR"
       "8hnVsIcH7Z0SQrx56TnM6&client_secret=53uI4Qek8y0jDAzmABgZvbZnU2ryNESN")


def answer_generate(message):
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", key, headers=headers, data=payload)
    url = ("https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/e"
           "rnie-4.0-turbo-128k?access_token=") + response.json().get("access_token")
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("result")


def get_nodes(request):
    getting_nodes = []
    if request == 1:
        with open('basic_Color.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        for objects in data:
            getting_nodes.append(objects)
        return getting_nodes
    if request == 2:
        with open('basic_Company.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        for objects in data:
            getting_nodes.append(objects)
        return getting_nodes
    if request == 3:
        with open('basic_KeyNeed.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        for objects in data:
            getting_nodes.append(objects)
        return getting_nodes


if __name__ == "__main__":
    for i in range(1, 4):
        dic = {}
        try:
            nodes = get_nodes(i)
            print("Found {} nodes:".format(len(nodes)))
            count = 0
            for node in nodes:
                count += 1
                generating = []
                emotion = ["开心", "轻松", "中立", "愤怒", "害羞", "紧张", "奇怪", "焦虑", "急躁", "激动"]
                history = []
                for j in range(10):
                    question = "请基于"+emotion[j]+"情感提出一个关于你需要选配空调的诉求，诉求的目的是使得空调有以下属性："
                    question = question+str(node)
                    question = question+("。目前已经有过如下的结果："+"".join(history) +
                                         "。请展开思路，写一个与众不同的提问。同时，我希望其中不要参杂表情包等内容，大约40字以内即可，请"
                                         "使用一些口语化的词进行生成！而不是过于追求华丽、优美、对仗。注意不要写的跟宣传口号那样！要写的更像用户正常的提问诉求")
                    print("如下是给大模型进行的提问："+question)
                    answer = answer_generate(question)
                    print("以下是给出的答复："+answer)
                    history.append(answer)
                    generating.append(answer)
                    print("正在执行第"+str(i)+"个类别（颜色、公司、需求）中的第"+str(count)+"个关键词")
                dic[str(node)] = generating
        finally:
            path = " "
            if i == 1:
                path = 'basic_Color.json'
            if i == 2:
                path = 'basic_Company.json'
            if i == 3:
                path = 'basic_KeyNeed.json'
            with open(path, 'w', encoding="utf-8") as fp:
                json.dump(dic, fp, indent=4, ensure_ascii=False)
