from pysnow.lib.api_handler import APIHandler

class AnalysisHandler(APIHandler):
    def __init__(self, requestor, opts):
        self.__requestor = requestor
        self.__opts = opts
