import json

class jSona() :
    def __init__(self) :
        pass

    def error(self, e, msg="", ex=False) :
        print("ERROR {} : {}".format(msg, e))
        if ex : exit()    

    def loads(self, data, cry=True) :
        try :
            data = json.loads(data)
            if cry : print("LOADS SUCCESS.")
        except Exception as e :
            self.error(e, "LOADS")
        finally :
            return data

    def dumps(self, data, cry=True) :
        try :
            data = json.dumps(data)
            if cry : print("DUMPS SUCCESS.")
        except Exception as e :
            self.error(e, "DUMPS")
        finally :
            return data

    def loadJson(self, cpath, cry=True, ex=False) :
        try :
            with open(cpath, 'r') as openfile :
                return json.load(openfile)
                if cry : print("LOAD SUCCESS FROM [ {} ]".format(cpath))
        except Exception as e :
            self.error(e, "LOAD JSON [ {} ]".format(cpath), ex)

    def saveJson(self, cpath, data, cry=True, ex=False) :
        try :
            with open(cpath, 'w') as openfile :
                json.dump(data, openfile)
                if cry : print("SAVE SUCCESS TO [ {} ]".format(cpath))
        except Exception as e :
            self.error(e, "SAVE JSON [ {} ]".format(cpath), ex)