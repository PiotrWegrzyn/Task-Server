#Python version: 3.6
#Written and tested on Pycharm
#Author: Peter Wegrzyn
#Last update: 14.04.18

class Task:
    id
    name = ""
    description =""
    priority = 0


#Constructor needs to have id in arguments because it needs to be set this way when deserlializing from dictionary
    def __init__(self,id, name, description, priority):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority
        Task.id+=1



    def printTask(self):
        s= "\nTask Id: "+str(self.id)+" Priority: "+str(self.priority)+" Name: "+self.name+"\nDescription: "+ self.description
        return s

#used for initializing Task from a dictionary. Use: foo = Task.fromDict({"id":bar,"name": baz, etc.})
    @classmethod
    def fromDict(cls, dictionary):
        return cls(dictionary["id"],dictionary["name"],dictionary["description"],dictionary["priority"])