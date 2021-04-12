import requests


class Requestor:
    def __init__(self, opts):
        self.__opts = opts
        self.__headers = {"Content-Type": "application/json"}
        self.__authenticate()

    # TODO: Handle expired token
    # TODO: Handle HTTP and Connection errors
    def send(self, data, endpoint, method):
        url = f"{self.__opts['api_url']}{endpoint}"

        response = requests.request(method, url, headers=self.__headers,
                                                 data=data).json()

        return response

    def __authenticate(self):
        data = {
            "client_id": self.__opts["client_id"],
            "username": self.__opts["username"],
            "password": self.__opts["password"],
            "connection": "Username-Password-Authentication",
            "grant_type": "password",
            "scope": "openid"
        }

        response = requests.post(self.__opts['auth_url'], headers=self.__headers,
                                                        data=data).json()

        self.__headers["Authorization"] = f"Bearer {response['id_token']}"
