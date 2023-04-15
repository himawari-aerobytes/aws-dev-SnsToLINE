import os
import json
import urllib.parse
import urllib.request

def lambda_handler(event, context):
    # LINE Notifyのアクセストークンを環境変数から取得する
    access_token = os.environ['ACCESS_TOKEN']
    
    # SNSトピックからのメッセージを取得する
    message = json.loads(event['Records'][0]['Sns']['Message'])['default']
    
    # LINE Notifyに送信するメッセージ
    line_message = f"SNSトピックからのメッセージ: {message}"
    
    # LINE Notify APIのURL
    url = 'https://notify-api.line.me/api/notify'
    
    # LINE Notify APIに送信するヘッダー
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + access_token
    }
    
    # LINE Notify APIに送信するデータ
    data = urllib.parse.urlencode({'message': line_message}).encode('utf-8')
    
    # LINE Notify APIにPOSTリクエストを送信する
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
    
    # レスポンスのログを出力する
    print(body)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to LINE Notify!')
    }
