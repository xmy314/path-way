class Node(object):
    def __init__(self,name,pre_requsites=[]):
        self.name=name
        self.prereqs=pre_requsites
        self.familiarity=0  #in seconds
    
    def __str__(self):
        info=str([self.name,self.prereqs,self.familiarity])
        return info
    
    @staticmethod    
    def read(info):
        info=eval(info)
        result=Node(info[0],info[1])
        result.familiarity=float(info[2])
        return result



