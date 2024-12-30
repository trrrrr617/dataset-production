import json
import requests


key = ("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="
       "[your key]&client_secret=[your secret key]")


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

