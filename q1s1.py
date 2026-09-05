
def lightbulb_solver(lightbulb_array,target_array):
    """
    The function runs on the given list and checks for each of the switches two options (off and on). If the desired state can be reached, the function returns true, and if not, it returns false.
    :param lightbulb_array: The current state of the lamps
    :param target_array: The state to which we would like to bring the lamps by pressing switches
    :return: Is it possible to reach the desired state by pressing switches
    """
    def press_function(lightbulb_array,index):
        lightbulb_array[index] = not lightbulb_array[index]
        if index > 0:
            lightbulb_array[index-1] = not lightbulb_array[index-1]
        if index < len(lightbulb_array) - 1:
            lightbulb_array[index+1] = not lightbulb_array[index+1]
    def all_options(lightbulb_array,target_array,index):
        if index == len(lightbulb_array): #stop condition
            return lightbulb_array == target_array
        if all_options(lightbulb_array[:],target_array,index+1): # The first option is not to press any switch
            return True
        press_function(lightbulb_array,index) #If we did not press any switch and did not reach the goal, we will try to press the switches in order from the end to the beginning. Every time we press one of the switches we will check if the stopping condition is met and if we have reached the goal
        if all_options(lightbulb_array[:],target_array,index+1):
            return True
        else: #If we have tried all the options and have not been able to reach the goal
            return False
    return (all_options(lightbulb_array,target_array,0))
