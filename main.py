"""
Port Scanner with Python
Ali Karahisar
Created Date: 19/01/2021
First Update: 04/02/2021
Second Update: 21/03/2021
"""
from pyfiglet import Figlet
import sys
import socket
from datetime import datetime
from colorama import Fore
import os

openPortsArray=[]

def addForWrite(portNumber):
    openPortsArray.append(portNumber)

def osFilePath(os,filePath,fileName):
    if(os=="nt"):
        filePath = filePath+"\\"+fileName
    else:
        filePath=filePath+"/"+fileName
    return filePath

def savePortTxt(ip):
    opSystem=os.name
    filePath = os.getcwd()
    fileName= "openPorts-"+str(ip)+"-"+ str(datetime.now())+".txt"
    with open(fileName, "w") as txt_file:
        for row in openPortsArray:
            txt_file.write(str(row)+'\n')
    filePath = osFilePath(opSystem,filePath,fileName)
    print("📝 Open Port(s) .txt file saved - " + str(filePath))

def runScan():
    print(Fore.LIGHTRED_EX)
    for port in range(65535):
        try:
            serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            serv.bind((targetIp, port))
        except:
            print('⚠️ [Open Port] :', port,'\n')
            addForWrite(port)
        serv.close()
    scan_finish_time = datetime.now()
    print(Fore.LIGHTGREEN_EX+"\n")
    print("-" * 60)
    print("🎯️ Scanning Target: " + targetIp)
    print("⏳ Scanning started at: " + str(startTime))
    print("⌛️ Scanning finished at: " + str(scan_finish_time))
    completion_time = scan_finish_time - startTime
    print("🏁 Scan Completion Time: " + str(completion_time))
    print(Fore.LIGHTRED_EX+"⚠️ Total Open Ports: " + str(len(openPortsArray)))
    print(Fore.LIGHTGREEN_EX+"-" * 60)

f= Figlet(font='poison')
header = f.renderText("PScan")
print(Fore.LIGHTRED_EX + header)

targetIp = input('❓ Enter the host to be scanned: ')
forTextFile = targetIp;
targetIp = socket.gethostbyname(targetIp)
startTime = datetime.now()

print(Fore.CYAN)
print("-" * 60)
print("🎯️ Scanning Target: " + targetIp)
print("⏳ Scanning started at: " + str(startTime))
print("-" * 60)

try:
    runScan()
    savePortTxt(forTextFile)


except KeyboardInterrupt:
    print("\n Scan canceled")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved")
    sys.exit()
except socket.error:
    print("\n Server not responding")
    sys.exit()