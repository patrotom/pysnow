import requests


class Requestor:
    def __init__(self, opts):
        self.opts = opts
        self.__authenticate()

    def send(self, data, endpoint, method):
        url = f"{self.opts['api_url']}{endpoint}"
        headers = {"Content-Type": "application/json"}

        response = requests.request(method, url, headers=headers, data=data)

        return response

    def __authenticate(self):
        data = {
            "client_id": self.opts["client_id"],
            "username": self.opts["username"],
            "password": self.opts["password"],
            "connection": "Username-Password-Authentication",
            "grant_type": "password",
            "scope": "openid"
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(self.opts['auth_url'], headers=headers,
                                                        data=data).json()

        self.id_token = response["id_token"]
