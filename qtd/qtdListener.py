from qtd.qtdBaseListener import *
from eventEngine import *

class qtdListener(qtdBaseListener):
    eventEngineDict={}
    def __init__(self):
        self(qtdListener,self).__init__()
    
    @classmethod
    def registed(self,_id,obj):
        if not self.eventEngineDict.has_key(_id):
            self.eventEngineDict[_id] = obj

    @classmethod
    def notify(self,evtid,_id,data):
        if self.eventDict.has_key(evtid):
            eventEngine = self.eventEngineDict[evtid]
            event2 = Event(type_=_id)
            event2.dict_['data'] = data
            eventEngine.put(event2)
            

class __listenerNotify(object):
    def __init__(self):
        super(__listenerNotify,self).__init__()
        
        