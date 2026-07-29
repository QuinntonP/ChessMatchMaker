import requests

class Rest_utils():
    @staticmethod
    def send_data(ip, port, url):
        response = requests.get(f"http://{ip}:{port}/{url}")

        if response.status_code == 200:
            data = response.text
            print(data)
            return data
        else:
            print("Failed to reach URL:" + url)