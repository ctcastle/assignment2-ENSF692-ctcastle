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
        pass

    # Takes a "measurement" of the world and outputs the result 
    def update_status(): # You may decide how to implement the arguments for this function 
        pass 



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    pass



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    runFlag = True 
    while runFlag:
        sensorStatus = input("Update sensor:\n 1. Update stoplight detection\n 2. Update pedestrian detection\n 3. Update vehicle detection\n 4. Q to quit\n")
        runFlag = (menuInput.lower() != 'q')

# Two ways I could see doing this: 
# Either you should have Sensor request updates that the main command provides/ so like pretending that the main IS the sensor getting data 
# Or you have the main command request updates from the sensor/ pretending that you are requesting data FROM the sensor 
# Basically this is the difference between a publisher, or master/slave communication style 

# I think I want to do this by having all the sensor logic in the sensor so: 
# So basically sensor.update will "measure" the state of the world 
# But then have a separate logic that says what to do with the updated status 
# This way the sensor just measures things but the main function "brain" decides what to do with those things 





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

