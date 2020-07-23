from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('kGa0sT+lMHebEbu2P+Y7u6Iu+NDkDImMCRhJsLg4j5sQpHuK5MJcVroaQZB2ecdI6lhW1ensyUSfHObO0JODL6pCPvWuMj8Jk/U3uLkyznH1+HhR5Hgi4ZXE4mpXU7pFh1BJC56LJlqXJPd4jY5sAAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d8b2be9f473e2b54b474c019586be697')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    result = ''
    if msg=='你好':
        result = '安安'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))


if __name__ == "__main__":
    app.run()