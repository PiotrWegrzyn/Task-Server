#Python version: 3.6
#Written and tested on Pycharm
#Author: Peter Wegrzyn
#Last update: 14.04.18

import socket
import sys
import re

def createConnection():
    newSocket = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 12345                 # Reserve a port for your service.
    newSocket.connect((host, port))

    return newSocket

def menu():
    choice = input('Enter a number:\n 1. Show the whole "Todo list".\n 2. Add task. \n 3. Remove task. \n 4. Show all taks with a certain priority. \n 5. Terminate Sever \n 6. Exit\n')
    if(None == re.match("^[1-6]$",str(choice))): print("Wrong input. Try again.\n")
    else:
        choice = int(choice)
        if choice == 6:
            sys.exit()
        s = createConnection()
        if choice == 1:
            s.send("SHOW".encode())
            recMessage = s.recv(1024)
            print(recMessage.decode())
            s.close()
        if choice == 2:
            newTaskName = input("What is the name of the task?\n")
            newTaskDesc = input("Please describe the task:\n")
            newTaskPriority = input("At a scale from 1 to 5 what is the priority for the task? (1 is the highest)\n")
            while None == re.match("^[1-5]$", str(newTaskPriority)):
                print("Priority can only be a number 1-5. Try again.")
                newTaskPriority = "1"  # input("At a scale from 1 to 5 what is the priority for the task? (1 is the highest)\n")
            sendMessage = "ADD;"+newTaskName+";"+newTaskDesc+";"+newTaskPriority
            s.send(sendMessage.encode())
            print("Added new task")
            s.close()
        if choice == 3:
            taskId = input("Enter the id of the task you want ot remove.\n")
            sendMessage = "REMOVE;" + taskId
            s.send(sendMessage.encode())
            recMessage = s.recv(1024)
            print(recMessage.decode())
            s.close()
        if choice == 4:
            taskPriority = input("Which priority do you want to see?")
            sendMessage = "SHOWP;" + taskPriority
            s.send(sendMessage.encode())
            recMessage = s.recv(1024)
            print(recMessage.decode())
            s.close()
        if choice == 5:
            password = input("Enter admin password.\n")
            if str(password)=="UJNaKolana2137":
                sendMessage = "DIE"
                s.send(sendMessage.encode())
                print("Server Terminated")
                s.close()
            else: print("Wrong password.")

while(True):
    menu()


