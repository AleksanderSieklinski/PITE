import random
import time

# The task was to write a python programme that simulates a plane's turbulance correction system. 
# The plane has a tilt, which is corrected by the system. 
# The system also has a rate of correction, which is increased by the turbulance. 
# If the tilt is greater than 1, the seatbelt sign is turned on. 
# The system should print out the current turbulance, rate of correction, tilt and whether the seatbelt sign is on or off. 
# The system should also update the turbulance, rate of correction and tilt every second. The turbulance should be a random number between -2 and 2, and the rate of correction should be increased by the turbulance divided by 10. 
# The tilt should be increased by the turbulance. 
# The system should also print out the details every second.
class Plane:
    def __init__(self):
        self.tilt=0
        self.turbulance=0
        self.rate_of_correction = 0.1
        self.seatbelt_sign=False
        self.print_details()

    def update_tick(self):
        self.turbulance = random.gauss(0, 2*self.rate_of_correction)
        self.tilt = self.tilt + self.turbulance
        self.rate_of_correction = self.rate_of_correction + self.turbulance/10
        self.seatbelt_sign = False
        if abs(self.tilt)>1:
            self.seatbelt_sign = True
        self.print_details()

    def print_details(self):
        print("Turbulance: {𝟂}\nRate of correction: {}\nTilt: {}".format(self.turbulance, self.rate_of_correction, self.tilt))
        if self.seatbelt_sign:
            print("Please fasten your seatbelts, we're experiencing some heavy turbulance.\n")
        else:
            print("Seatbelt sign is off, you can walk around.\n")

def main():
    plane = Plane()
    while True:
        plane.update_tick()
        time.sleep(1)

if __name__ == "__main__":
    main()