"""
Port Scanner with Python
Ali Karahisar
Created Date: 19/01/2021
"""
from pyfiglet import Figlet
import sys
import socket
from datetime import datetime
from colorama import Fore

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

def runScan():
    print(Fore.LIGHTRED_EX)
    open_port_counter = 0
    for port in range(65535):
        try:
            serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            serv.bind((targetIp, port))
        except:
            print('⚠️ [Open Port] :', port,'\n')
            open_port_counter = open_port_counter + 1
        serv.close()
    scan_finish_time = datetime.now()
    print(Fore.LIGHTGREEN_EX+"\n")
    print("-" * 60)
    print("🎯️ Scanning Target: " + targetIp)
    print("⏳ Scanning started at: " + str(startTime))
    print("⌛️ Scanning finished at: " + str(scan_finish_time))
    completion_time = scan_finish_time - startTime
    print("🏁 Scan Completion Time: " + str(completion_time))
    print(Fore.LIGHTRED_EX+"⚠️ Total Open Ports: " + str(open_port_counter))
    print(Fore.LIGHTGREEN_EX+"-" * 60)

try:
    runScan()
except KeyboardInterrupt:
    print("\n Scan canceled")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved")
    sys.exit()
except socket.error:
    print("\n Server not responding")
    sys.exit()
