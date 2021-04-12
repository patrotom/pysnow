import yaml

from pysnow.utils.requestor import Requestor

# 1. Authorization
# 2. Ragnar API - search scenes
#   a. POST /imagery/search/initiate
#   b. POST /tasking/get-status
#   c. POST /imagery/search/retrieve
# 3. Kraken API - retrieve data
#   a. ...

class PySnow:
    def __init__(self, username, password):
        self.__load_config()
        self.requestor = Requestor(self.__requestor_opts(username, password))

    def analyze_imagery(self, imagery_opts={}, analysis_opts={}):
        pass

    def __load_config(self):
        with open("../config.yml", "r") as cf:
            self.config = yaml.safe_load(cf)

    def __requestor_opts(self, username, password):
        return {
            "client_id": self.config["client_id"],
            "username": username,
            "password": password,
            "api_url": self.config["api_url"],
            "auth_url": self.config["auth_url"]
        }
