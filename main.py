"""
Port Scanner with Python
Ali Karahisar
Created Date: 19/01/2021
First Update: 04/02/2021
"""
from pyfiglet import Figlet
import sys
import socket
from datetime import datetime
from colorama import Fore

openPortsArray=[]

def addForWrite(portNumber):
    openPortsArray.append(portNumber)

def savePortTxt():
    with open("openPorts.txt", "w") as txt_file:
        for row in openPortsArray:
            txt_file.write(str(row)+'\n')

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
targetIp = socket.gethostbyname(targetIp)
startTime = datetime.now()

print(Fore.CYAN)
print("-" * 60)
print("🎯️ Scanning Target: " + targetIp)
print("⏳ Scanning started at: " + str(startTime))
print("-" * 60)

try:
    runScan()
    savePortTxt()

    print("📝 Open Port(s) .txt file saved")
except KeyboardInterrupt:
    print("\n Scan canceled")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved")
    sys.exit()
except socket.error:
    print("\n Server not responding")
    sys.exit()