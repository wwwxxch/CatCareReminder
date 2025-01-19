import os
import requests


def morningcall():
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")

    if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_GROUP_ID:
        raise Exception("LINE_CHANNEL_ACCESS_TOKEN and LINE_GROUP_ID are required")

    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"}
    payload = {
        "to": LINE_GROUP_ID,
        "messages": [{"type": "text", "text": "早上記得清貓沙、換前後的水盆、確定碗中有兩湯匙飼料哦！"}],
    }

    response = requests.post(url, headers=headers, json=payload)

    # check response
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    morningcall()
