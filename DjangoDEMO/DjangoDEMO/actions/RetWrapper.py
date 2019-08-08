import json
class RetWrapper():
    def __init__(self,Result=True,Data=dict(),Message=''):
        self.Result=Result
        self.Data=Data
        self.Message=Message
    def setData(self,Data={}):
        self.Data=Data
    def toJSON(self):
        json_dict={}
        json_dict['Result']=self.Result
        json_dict['Data']=self.Data
        json_dict['Message']=self.Message
        return json.dumps(json_dict,ensure_ascii=False)