# -*- coding: utf-8 -*-

import sys, time, timeit
from socket import *

BYTE_SIZE_IN_BITS = 8

def readArgs():

    if len(sys.argv) < 6:
        paramError()

    if sys.argv[1]=='-i':
        targetIP = sys.argv[2]
    else:
        paramError()

    if sys.argv[3]=='-p':
        targetPort = sys.argv[4]
    else:
        paramError()

    if sys.argv[5]=='-r':
        
        traffic = sys.argv[6]
    else:
        paramError()

    return targetIP, int(targetPort), int(traffic)

def printTargets(targetIP, targetPort, traffic):
    print('================UDP================')
    print('IP destino   : ' + str(targetIP))
    print('Porta destino: ' + str(targetPort))
    print('Trafego      : ' + str(traffic/1000) + ' Mbits/s')
    print('===================================')

def paramError():
    print("O comando deve possuir o formato : 'gt –i IPdestino –p Porta -r Qnttrafego'")
    sys.exit()

def UDPtrafficGenerator(targetIP, targetPort, traffic):
    timeout = 1
    targetAddress = (targetIP, targetPort)

    gtSocket = socket(AF_INET, SOCK_DGRAM)
    numberOfBursts = ((traffic*1024)/BYTE_SIZE_IN_BITS)/512
    print ("Number of bursts -> %d" % numberOfBursts)
    print ("Intervalo entre as rajadas de 512bytes -> %f" % (float(1)/numberOfBursts))
    print ("Gerando trafego. . .")
    while(1):
        gtSocket.sendto(bytes(512), targetAddress)
        
        time.sleep(float(1)/(numberOfBursts))
        

targetIP, targetPort, traffic = readArgs()
printTargets(targetIP, targetPort, traffic)
UDPtrafficGenerator(targetIP, targetPort, traffic)