# pylint: disable=F0401
# from wheelcontroller.WheelController import WheelController 
from brane import Brane
import socket
import time
import win32pipe
import os
import mmap
class Driver:

    def __init__(self):
        #self.controller = WheelController()
        self.brane = Brane()
        

    def _drive(self, car_stats):
        print("{}".format(car_stats))
        #maneuver = self.brane.thinke(car_stats)
        #self.controller.update_inputs(maneuver)

    def _look(self):
        return 1
        #take screenshot, return
    
    def _be_aware(self):
        print("3...2...1... GO")

        # Open the file for reading only
        fd = os.open('drive', os.O_RDONLY)
        buf = mmap.mmap(fd, mmap.PAGESIZE, access=mmap.ACCESS_READ)
    
        # Print when the content changes
        last = b''
        while True:
            screen = self._look()
            buf.seek(0)
            car_stats = buf.readline()
            if car_stats != last:
                print(car_stats)
                #self._drive(car_stats)
            else:
                time.sleep(.001)
            
            if len(car_stats) == 5:
                return



    def wake_up(self):
        print("*yawn*\n I cant wait to go driving")
        self._be_aware()




