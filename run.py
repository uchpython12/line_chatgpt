import flask     # pip install flask
from flask import  request
import requests
import chatgpt
import Line_API
app = flask.Flask(__name__)
"""-----------------------------需要改成自己的--------------------------------"""
# auth_token = ""
# # YouruserID=""
auth_token, 接收人的id,openai_key = Line_API.Line_讀取設定檔Excel('line.xlsx')
"""-----------------------------需要改成自己的--------------------------------"""


def LineText(replyToken,str1,userId):



    message = {
        "replyToken": replyToken,
        "messages": [
            {
                "type": "text",
                "text": str1,
            }
        ]
    }

    hed = {'Authorization': 'Bearer ' + auth_token}
    url = 'https://api.line.me/v2/bot/message/reply'
    response = requests.post(url, json=message, headers=hed)
    print(response)
    print(response.json())
    return ""



@app.route("/", methods=[ 'POST'])
def LinePOST():
    data = request.json
    print("data=",data)
    replyToken = data['events'][0]['replyToken']  # replyToken
    userId = data['events'][0]['source']['userId']  # 用戶ID
    text = data['events'][0]['message']['text']  # 訊息內容
    # str1 =" Flask Server 說\n 你的 User Id: " + userId + "\n 傳過來的文字: = " + text
    print("text="+text)
    # LineText(replyToken, str1,userId)
    LineText(replyToken, chatgpt.chat_gpt(text), userId)
    return ""


if __name__ == '__main__':
    app.run(port=8888 ,debug=True)