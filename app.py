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

line_bot_api = LineBotApi('6n4joWoMjBcRvTQf9PI6ALHG2JE3pAnwNjkTvU9u67DFmRtt1hhE5I8v+bLzVyrK26lhW1ensyUSfHObO0JODL6pCPvWuMj8Jk/U3uLkyznHcYVikbhWA/WBtXHkrgsWpI5/XzQU8HkqW5QLPNCUb1gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5b1c376740b74efd124d9e5496fda0d8')


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