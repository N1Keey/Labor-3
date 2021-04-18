import json
from datetime import datetime

def add2protocol(password, ip):
  dtts=datetime.now().timestamp()
  protocol=loadProtocol()
  id=len(protocol)
  protocolentry={'ID':id,'DTTS':dtts,'PW':password,'IP':ip}
  protocol.append(protocolentry)
  saveProtocol(protocol)

def saveProtocol(protocol):
  jsondict = json.dumps(protocol,ensure_ascii=False,)
  with open("protocol.json","w", encoding='utf-8') as fw:
      fw.write(jsondict)

def loadProtocol():
  with open('protocol.json','r',encoding='utf-8') as fr:
    jsonstring=fr.read()
    protocol=json.loads(jsonstring)
  return protocol

def checkIPwithProtocol(ip):
  protocol=loadProtocol()
  ipBool=False
  for protocolentry in protocol:
    if ip == protocolentry.get("IP"):
      ipBool=True
  return ipBool

def getIDfromIP(ip):
  protocol=loadProtocol()
  for entry in protocol:
    if ip == entry.get("IP"):
      id=entry.get("ID")
  return id

def getDTTSFromID(id):
  protocol=loadProtocol()
  entry=protocol[id]
  dtts=entry.get("DTTS")
  return dtts

def getDTTSFromIP(ip):
  id=getIDfromIP(ip)
  dtts=getDTTSFromID(id)
  return dtts
  
def getTimeDiffBetweenLogins(ip):
  id=getIDfromIP(ip)
  dtts=getDTTSFromID(id)
  dttsnow=datetime.now().timestamp()
  dttsdiff=dttsnow-dtts
  return dttsdiff