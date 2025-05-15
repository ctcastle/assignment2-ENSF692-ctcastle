# input_processing.py
# Conner Castle, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.vehicle_status = 'no' 
        self.pedestrian_status = 'no' 
        self.stoplight_status = 'green' 

    # Takes a "measurement" of the world and outputs the result 
    def update_status(self,measurement): # You may decide how to implement the arguments for this function 
            SDetect = input("What change has been indentified? ")
            if (measurement == 1):
                if(SDetect == "red"):
                    self.stoplight_status = 'red'
                elif (SDetect == 'yellow'):
                    self.stoplight_status = 'yellow'
                elif (SDetect == 'green'):
                    self.stoplight_status = 'green'
                else:
                    print("Invalid vision change")
            elif (measurement == 2): 
                if(SDetect == "yes"):
                    self.pedestrian_status = 'yes'
                elif (SDetect == 'no'):
                    self.pedestrian_status = 'no'
                else:
                    print("Invalid vision change")
            elif (measurement == 3): 
                if(SDetect == "yes"):
                    self.vehicle_status = 'yes'
                elif (SDetect == 'no'):
                    self.vehicle_status = 'no'
                else:
                    print("Invalid vision change")


# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    if (sensor.stoplight_status == 'red' or 
        sensor.pedestrian_status == 'yes' or 
        sensor.vehicle_status == 'yes'):
        print("STOP")
    elif (sensor.stoplight_status == 'yellow'):
        print("Caution")
    else:
        print("Proceed")
    print(f'Light: {sensor.stoplight_status} , Pedestrian: {sensor.pedestrian_status} , Vehicle: {sensor.vehicle_status}') 


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    runFlag = True 
    s = Sensor() 
    while runFlag:
        print('')
        print("Are changes detected in the vision input?")
        measurement = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
        try:
            measurement = int(measurement)
            if (measurement == 0):
                runFlag = False 
                break
            elif (measurement == 1 or measurement == 2 or measurement == 3):
                s.update_status(measurement)
            else: 
                raise ValueError 
            print_message(s)
        except ValueError:
            print("You must select either 1, 2, 3 or 0.")


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

