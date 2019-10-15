from nodes import *
class Network(object):
    def __init__(self,info=False):
        self.nodes=[]
        if info:
            for node in info:
                self.nodes.append(Node.read(node))
    
    def add(self,node):
        self.nodes.append(node)
    
    def save(self,path="base.txt"):
        info=[]
        for node in self.nodes:
            info.append(str(node) )
        info=str(info)
        f=open(path,"w+")
        f.write(info)
        f.close
    
    @staticmethod
    def read(path="base.txt"):
        f=open(path,"r")
        info=eval(f.read())
        f.close()
        return Network(info)
