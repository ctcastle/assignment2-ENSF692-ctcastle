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

    # Takes a "measurement" of the world and updates the sensor's instance variables, if incorrect input is detected 
    # the user is notified of an invalid vision change, no status changes, and the main loop is repeated. 
    # Parameters: 
    # Self so the method can reference the instance object 
    # Measurement so it knows which part of the sensor to update, measurement has been preprocessed by main so
    # we can safely assume it is an int of value 1, 2, or 3. 
    def update_status(self,measurement): #
            SDetect = input("What change has been indentified? ") # Determine what the status update is 
            if (measurement == 1): # Checking stop light statuses, if input is not a valid option, print out 'Invalid vison change.' 
                if(SDetect == "red"):
                    self.stoplight_status = 'red' # self allows the function to reference its own instance variables 
                elif (SDetect == 'yellow'):
                    self.stoplight_status = 'yellow'
                elif (SDetect == 'green'):
                    self.stoplight_status = 'green'
                else:
                    print("Invalid vision change")
            elif (measurement == 2): 
                if(SDetect == "yes"): # Checking pedestrian statuses, if input is not a valid option, print out 'Invalid vison change.' 
                    self.pedestrian_status = 'yes'
                elif (SDetect == 'no'):
                    self.pedestrian_status = 'no'
                else:
                    print("Invalid vision change")
            elif (measurement == 3): # Checking vehicle statuses, if input is not a valid option, print out 'Invalid vison change.' 
                if(SDetect == "yes"):
                    self.vehicle_status = 'yes'
                elif (SDetect == 'no'):
                    self.vehicle_status = 'no'
                else:
                    print("Invalid vision change")


# Prints the appropriate action command and the current status of all the sensor elements. 
def print_message(sensor):
    if (sensor.stoplight_status == 'red' or 
        sensor.pedestrian_status == 'yes' or 
        sensor.vehicle_status == 'yes'): # Checks for all conditions that produce a STOP command, if any of these are true, STOP is printed 
        print("STOP")
    elif (sensor.stoplight_status == 'yellow'): # Checks for any conditions that produces a Caution command, this is only 1 condition since all the STOP conditions are checked first 
        print("Caution")
    else: # Only if not STOP or Caution will proceed be printed 
        print("Proceed")
    #No matter what print the status 
    print(f'Light: {sensor.stoplight_status} , Pedestrian: {sensor.pedestrian_status} , Vehicle: {sensor.vehicle_status}') 


# Holds the main flow of the program and keeps the loop running as long as the user does not enter 0 
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    runFlag = True 
    s = Sensor() # Instantiate a Sensor object and assign a reference to that object in 's' 
    while runFlag: 
        print('')
        print("Are changes detected in the vision input?")
        measurement = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ") # First input from the user, should be a integer but if not an exception is thrown and handled 
        try:
            measurement = int(measurement) # Check if the user input is an int, ValueError exception thrown if not 
            if (measurement == 0):
                runFlag = False 
                break # Break out of while loop to stop execution immediately if user wants to quit 
            elif (measurement == 1 or measurement == 2 or measurement == 3): # At this point we can safely assume measurement is a number but this if statement guagrantees update_status only runs if the value is 1,2,or3 
                s.update_status(measurement)
            else: 
                raise ValueError # Raises if the input value is a number but isn't 0,1,2,or3
            print_message(s)
        except ValueError:
            print("You must select either 1, 2, 3 or 0.")


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

