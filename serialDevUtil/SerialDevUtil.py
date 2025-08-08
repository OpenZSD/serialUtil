import serial
import serial.tools.list_ports
import os
import json
from dataclasses import dataclass
from enum import Enum

@dataclass
class Vendor:
    name: str 
    devices: dict
    
@dataclass
class PortInfo:
    vendor: str
    device: str
    port: any    

gVidMap = None

def _getModuleDir():
    return os.path.dirname(os.path.abspath(__file__))
def _deviceJson():
    return _getModuleDir() + "/device.json"
    
def getDeviceList():
    def _createDeviceMap(dlist):
        dmap = {}
        for item in dlist:
            dmap[item[1]] = item[0]
        return dmap

    global gVidMap
    if (gVidMap == None):
        vmap = {}
        with open(_deviceJson(), 'r') as file:
            data = json.load(file)
            for vendor in data:
                vmap[data[vendor]['VID']] = Vendor(vendor, _createDeviceMap(data[vendor]['DEV']))
        gVidMap = vmap
        
    ports = serial.tools.list_ports.comports()
    namedPorts = []
    for portInfo in ports:
        vn = "N/A"
        pn = "N/A"
        if (portInfo.vid in gVidMap):
            vn = gVidMap[portInfo.vid].name
            if (portInfo.pid in gVidMap[portInfo.vid].devices):
                pn = gVidMap[portInfo.vid].devices[portInfo.pid]
        namedPorts.append(PortInfo(vn,pn,portInfo))
    return namedPorts

def baudrates():
    return [110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000, 256000]

def openPort(portInfo, baudrate=9600, timeout=1):
    return serial.Serial(portInfo.port.device, baudrate=baudrate, timeout=timeout)
    
