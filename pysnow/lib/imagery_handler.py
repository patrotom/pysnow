from pysnow.lib.api_handler import APIHandler


class ImageryHandler:
    def __init__(self, requestor, opts):
        self.__requestor = requestor
        self.__opts = opts

    def initiate(self):
        data = {
            "provider": self.__opts["provider"],
            "dataset": self.__opts["dataset"],
            "extent": self.__extent(),
            "startDatetime": self.__opts["start_datetime"],
            "endDatetime": self.__opts["end_datetime"],
            "onlyDownloadable": True
        }

        response = self.__requestor.send(data, "/imagery/search/initiate", "POST")

        return response["pipelineId"]

    def is_finished(self, pipeline_id):
        data = {"pipelineId": pipeline_id}

        response = self.__requestor.send(data, "/tasking/get-status", "POST")

        return response["status"] == "RESOLVED"

    def retrieve(self, pipeline_id):
        data = {"pipelineId": pipeline_id}

        response = self.__requestor.send(data, "/imagery/search/retrieve", "POST")

        return response

    def __extent(self):
        return {
            "type": "Polygon",
            "coordinates": [self.__opts["coordinates"]]
        }
