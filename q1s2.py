def lightbulb_solver_with_steps(lightbulb_array,target_array):
    """
    The function runs recursively on the given list and checks all the options in order to reach the target list. If we were able to find a relevant sequence of switches, we will return the list of indexes of the bulbs, if not we will return -1.
    :param lightbulb_array: The current state of the lamps
    :param target_array: The state to which we would like to bring the lamps by pressing switches
    :return: The indexes of the switches we clicked to get to the target list
    """
    def press_function(lightbulb_array,index): #Similar to the previous section, we will define a function that presses the switch of the current lamp and those next to it
        lightbulb_array[index] = not lightbulb_array[index]
        if index > 0:
            lightbulb_array[index-1] = not lightbulb_array[index-1]
        if index < len(lightbulb_array) - 1:
            lightbulb_array[index+1] = not lightbulb_array[index+1]
    def all_options(lightbulb_array,target_array,index,index_list = None):
        if index_list == None:
            index_list = [] #We will create an empty list to which we will add the indexes of the relevant switches
        if index == len(lightbulb_array): #My stopping condition is if the index is equal to the length of the list (the list is over)
            if lightbulb_array == target_array: #If we have reached the stopping conditions and the original list is equal to the target list, we will return the index list
                return index_list
            else: #If the list remains empty (no suitable indexes were found), we will return a list containing -1
                return [-1]
        not_press = all_options(lightbulb_array[:],target_array,index+1,index_list) #Checking the option of not pressing the switch. If the list does not contain -1, it means that a suitable option was found and we would like to return the list
        if not_press != [-1]:
            return not_press
        press_function(lightbulb_array,index) #If a suitable option is not found, we will try to click the switch and add it to the index list.
        index_list = index_list + [index]
        press = all_options(lightbulb_array,target_array,index + 1, index_list)
        if press != [-1]:
            return press
        return [-1]

    return all_options(lightbulb_array,target_array,0)
