import yaml
import time
import os

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
        self.__requestor = Requestor(self.__requestor_opts(username, password))

    # Start with synchronous version, do async later
    # Will accept only polygon with coordinates
    # imagery_opts = {
    #   coordinates: [[x, y]],
    #   startDatetime: YYYY-MM-DD HH:MM:SS,
    #   endDatetime: YYYY-MM-DD HH:MM:SS,
    # }
    def analyze_imagery(self, imagery_opts={}, analysis_opts={}):
        analysis_handler = AnalysisHandler(self.__requestor, analysis_opts)

        imagery = self.__retrieve_imagery(imagery_opts)


    def __retrieve_imagery(self, imagery_opts):
        imagery_opts["provider"] = self.__config["provider"]
        imagery_opts["dataset"] = self.__config["dataset"]
        imagery_handler = ImageryHandler(self.__requestor, imagery_opts)

        pipeline_id = imagery_handler.initiate()
        while True:
            if imagery_handler.is_finished(pipeline_id):
                break
            time.sleep(1)

        return imagery_handler.retrieve(pipeline_id)

    def __load_config(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_segments = dir_path.split("/")[:-1]
        path_segments.append("config.yml")
        file_path = "/".join(path_segments)

        with open(file_path, "r") as cf:
            self.__config = yaml.safe_load(cf)

    def __requestor_opts(self, username, password):
        return {
            "client_id": self.__config["client_id"],
            "username": username,
            "password": password,
            "api_url": self.__config["api_url"],
            "auth_url": self.__config["auth_url"]
        }
