
def divide_pancakes_extended(pancakes, total_size):
    """
    The function receives a list of numbers representing sizes of pancakes and a number representing the size of pancakes each person should receive. The function returns the maximum number of people to whom the pancakes can be distributed so that each person gets the required size
    :param pancakes: A list of numbers representing the sizes of pancakes we want to divide
    :param total_size: The sum of the sizes each person should receive
    :return: the maximum amount of the people who can get the requested amount by dividing the numbers on the list of pancakes
    """
    def recursive_max(take, not_take): #A recursive function that finds the option where the number of people to whom the pancakes were distributed is maximum
        if take > not_take:
            return take
        return not_take

    def divide_options(pancakes, total_size, index, current_sum, taken_pancakes, people):
        if index == len(pancakes):  # The stopping condition is if we have reached the end of the list (the pancakes are finished)
            return people

        # Now we have two options for each pancake:
        not_take = divide_options(pancakes, total_size, index + 1, current_sum, taken_pancakes, people) #The first option is not to take the pancake, move to the next pancake (increase the index by 1) and leave the total size as it was

        # A second option is if the pancake has not already been taken, take it, add it to the list of taken pancakes (thus avoiding using the same pancake twice), increase the index by 1 and subtract the size of the pancake we took from the total size
        take = 0
        if index not in taken_pancakes and current_sum + pancakes[index] <= total_size:
            taken_pancakes.append(index)
            if current_sum + pancakes[index] == total_size:  # If we have reached the total size, we will call the function one more time with the next index and add 1 to the people
                take += divide_options(pancakes, total_size, 0, 0, taken_pancakes, people + 1)
            else:  # If we have not reached the total size, we will call the function one more time with the next index, but we will not add 1 to the people
                take += divide_options(pancakes, total_size, index + 1, current_sum + pancakes[index], taken_pancakes, people)

            taken_pancakes.remove(index)  # After the end of the recursive call in which we chose to take the pancake, we will return the list of taken pancakes to be empty so as not to miss other options in which the pancakes taken will be different

        return recursive_max(take, not_take) #We will return the option in which the maximum number of people was received

    return divide_options(pancakes.copy(), total_size, 0, 0, [], 0)
print(divide_pancakes_extended([1,2,3,4,5,5,6,7,8,9,10,15], 15))