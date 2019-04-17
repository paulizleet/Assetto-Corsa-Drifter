import win32api
import win32com
import ctypes


class WheelController:

    def __init__(self):
        self.gas = 0 # up
        self.brake = 0 # down
        self.clutch = 0 # lctrl
        self.handbrake = 0 # space
        self.steeringwheel = 0 # mouse
        self.gear = 0 #1,2,3,4,5,6
        self.horn = 0 # h

    def update_inputs(self, seq):
        None if seq[0] == self.gas else self._update_gas(seq[0])

        None if seq[1] == self.gas else self._update_brake(seq[1])
        None if seq[2] == self.gas else self._update_clutch(seq[2])
        None if seq[3] == self.gas else self._update_handbrake(seq[3])
        None if seq[4] == self.gas else self._update_steeringwheel(seq[4])
        None if seq[5] == self.gas else self._update_gear(seq[5])
        None if seq[6] == self.gas else self._update_horn(seq[6])

    #does holding keys block??

    def _update_brake(val):
        self.brake = val
        if val == 1:
            #hold key until update
        else:
            #release key

    def _update_clutch(val):
        self.clutch = val
        if val == 1:
            #hold key until update
        else:
            #release key

    def _update_gas(val):
        self.gas = val
        if val == 1:
            #hold key until update
        else:
            #release key

    def _update_gear(val):
        if val == 0 or val == 7:
            return

        self.gear = val
        #release key
        #hold new key

    def _update_handbrake(val):
        self.handbrake = val
        if val == 1:
            #hold key until update
        else:
            #release key

    def _update_horn(val):
        self.horn = val
        if val == 1:
            #hold key until update
        else:
            #release key

    def _update_steeringwheel(val):
        if abs(val) > 450:
            return
        else:
            self.steeringwheel = val
            self.move_mouse()


