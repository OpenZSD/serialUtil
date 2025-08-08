from serialDevUtil import SerialDevUtil
import time

def main():
    devices = SerialDevUtil.getDeviceList()
    for dev in devices:
        #modify below code
        if ((dev.vendor == "PI") and (dev.device == "PICO")):
            s = SerialDevUtil.openPort(dev)
            print('sending: Test from python')
            s.write(("Test from python\n").encode('utf-8'))
            time.sleep(1)
            result = s.readline().decode('utf-8').strip()
            print(result)
            return
        else:
            print(f"Looping {dev.vendor}:{dev.device} is not it")
    
if (__name__ == "__main__"):
    main()
