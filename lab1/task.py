import random
import time
import math

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
        print("Turbulance: ", self.turbulance, 
        "\nRate of correction: ", self.rate_of_correction, 
        "\nTilt: ", self.tilt)
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