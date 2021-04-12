import yaml

from pysnow.utils.requestor import Requestor
from pysnow.lib.analysis_handler import AnalysisHandler
from pysnow.lib.imagery_handler import ImageryHandler

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
        requestor = Requestor(self.__requestor_opts(username, password))
        self.__imagery_handler = ImageryHandler(requestor)
        self.__analysis_handler = AnalysisHandler(requestor)

    # Start with synchronous version, do async later
    # Will accept only polygon with coordinates
    # imagery_opts = {
    #   coordinates: [[x, y]],
    #   startDatetime: YYYY-MM-DD HH:MM:SS,
    #   endDatetime: YYYY-MM-DD HH:MM:SS,
    # }
    def analyze_imagery(self, imagery_opts={}, analysis_opts={}):
        pass

    def __retrieve_imagery(self):
        pass

    def __load_config(self):
        with open("../config.yml", "r") as cf:
            self.__config = yaml.safe_load(cf)

    def __requestor_opts(self, username, password):
        return {
            "client_id": self.__config["client_id"],
            "username": username,
            "password": password,
            "api_url": self.__config["api_url"],
            "auth_url": self.__config["auth_url"]
        }
