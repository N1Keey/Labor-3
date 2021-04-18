import json
from datetime import datetime

def add2protocol(password, ip):
  dt=datetime.now().isoformat()
  protocolentry={'DT':dt,'PW':password,'IP':ip}
  protocol=loadProtocol()
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

def checkIPwithProtocol(ip,protocol):
  ipBool=False
  for protocolentry in protocol:
    if ip == protocolentry.get('IP'):
      ipBool=True
  return ipBool

def checkTimefromIP(ip, protocol):
  print(ip)