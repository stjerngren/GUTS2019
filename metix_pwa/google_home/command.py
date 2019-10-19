import requests

def send_broadcast(broadcast):
    data = {
        'command': broadcast,
        'user':"test",
        "broadcast":"true"
    }

    response = requests.post(
        url="http://127.0.0.1:3000/assistant/",
        json=data
    )
    print(response)


if __name__ == "__main__":
    send_broadcast("Hello world")