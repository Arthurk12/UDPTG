# -*- coding: utf-8 -*-

import sys, time
from socket import *

BYTE_SIZE_IN_BITS = 8
PACKET_SIZE_IN_BYTES = 256

def readArgs():

    if len(sys.argv) < 6:
        paramError()

    if sys.argv[1]=='-i':
        targetIP = sys.argv[2]
    else:
        print('Erro no arg[1]')
        paramError()
        

    if sys.argv[3]=='-p':
        targetPort = sys.argv[4]
    else:
        print('Erro no arg[2]')
        paramError()
        

    if sys.argv[5]=='-r':
        
        traffic = sys.argv[6]
    else:
        print('Erro no arg[3]')
        paramError()
        

    return targetIP, int(targetPort), int(traffic)

def printTargets(targetIP, targetPort, traffic):
    print('================UDP================')
    print('IP destino   : ' + str(targetIP))
    print('Porta destino: ' + str(targetPort))
    print('Trafego      : ' + str(traffic) + "(" + str(traffic/1000) + ' Mbits/s' + ")")
    print('===================================')

def paramError():
    print("O comando deve possuir o formato : 'python gtrf.py -i IPdestino -p Porta -r Qnttrafego'")
    sys.exit()

def UDPtrafficGenerator(targetIP, targetPort, traffic):
    packet_size_in_bytes = 128
    packet_size_in_bits = packet_size_in_bytes * 8
    numberOfBursts = ((traffic*1024)/(packet_size_in_bits))
    sleepTime = float(1/numberOfBursts)

    tsocket = socket(AF_INET, SOCK_DGRAM) 
    
    print(str(sleepTime) + " | " + str(numberOfBursts))

    while 1:
        start = time.time()
        tsocket.sendto(bytes(packet_size_in_bytes), (targetIP, targetPort))
        end = time.time() - start
        sleepTime = sleepTime - end

        if(sleepTime > 0):
            time.sleep(sleepTime)
        

targetIP, targetPort, traffic = readArgs()
printTargets(targetIP, targetPort, traffic)
UDPtrafficGenerator(targetIP, targetPort, traffic)