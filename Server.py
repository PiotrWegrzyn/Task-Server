#Python version: 3.6
#Written and tested on Pycharm
#Author: Peter Wegrzyn
#Last update: 14.04.18

import socket
import sys
from Task import Task
import json
import pickle
import os


def jdefault(o):
    return o.__dict__

def taskListToString(list):
    str ="List currently contains:"
    for i in range(0, len(list)):
        str += list[i].printTask()
    return str

def priorityTaskListToString(list,priority):
    str ="List currently contains:"
    for i in range(0, len(list)):
        if list[i].priority == priority:
            str += list[i].printTask()
    return str

def removeTask(list,id):
    s ="Task with such id has not been found."
    for i in range(0, len(list)):
        if str(list[i].id) == str(id):
            s = "Removed:" + list.pop(i).printTask()
            return s
    return s

#message - whatever we recived from client.
#list - taskList from "main"
def processMessage(message,list):
    messageTable = message.split(";")
    if messageTable[0] == "SHOW":
        c.sendall(taskListToString(list).encode())                                  #converting a list of task to string and than encoding the string and sending it to client
    if messageTable[0]=="ADD":
        newTask = Task(Task.id,messageTable[1], messageTable[2], messageTable[3])   #creating new task
         #print("Added:\n"+newTask.printTask())
        list+=[newTask]                                                             #adding a new task to the list
        #c.sendall(taskListToString(list).encode())
    if messageTable[0] =="SHOWP":
        c.send(priorityTaskListToString(list,messageTable[1]).encode())             #converting tasks with X priority from the list to string and than encoding the string and sending it to client
    if messageTable[0] == "REMOVE":
        c.sendall(removeTask(list,messageTable[1]).encode())                        #sending data that has been removed
    if messageTable[0] == "DIE":
        s.close()
        print("Server Terminated.")
        sys.exit()


#Creating server socket
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.



#setting up a list where we will store all Tasks. When the server starts taskList is imported from json file
taskList = []
Task.id = 0
size = os.path.getsize("taskList.json")
if os.path.getsize("taskList.json")>0:                       #json throws some errors when deserializing an empty file
    with open("taskList.json", 'r') as txtfile:
        fromJson = json.load(txtfile)
        for i in range(0,len(fromJson)):
            taskList.append(Task.fromDict(fromJson[i]))
        Task.id = taskList[-1].id +1                    #setting the "static" class variable which is used when creating new Task objects

#Loop that keep accepting connections from Clients
while True:
    print("Waiting for incomming connections..")
    c, addr = s.accept()     # Establish connection with client.
    recivedMessage = c.recv(1024).decode()
    print('Got connection from', addr," Message was: ",recivedMessage)
    processMessage(recivedMessage,taskList)

    #write taskList to json
    fileObject = open("taskList.json", 'w')
    serlializedTaskList = json.dumps(taskList, default=jdefault)
    fileObject.write(serlializedTaskList)
    fileObject.close()



    c.close()








    #Just for testing:
    #q = input("Read next connection?\n")
    #if(0 == int(q)):
    #    s.close()
    #    print("Server Terminated.")
    #    sys.exit()




