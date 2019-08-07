import copy
from time import sleep


# main function for running simulation
def startSim(input_mat, generations = 10, input_char = '█'):
    input_mat[0] = fixStart(input_mat[0], generations)
    printLine(input_mat[0])

    for i in range(1, 10):
        input_mat.append(applyRules(input_mat[0], input_char))


def applyRules(previous_array, input_char):
    new_array = []
    for i in range(0, len(previous_array)):
        alive1, alive2, alive3 = False
        loc1 = i - 1
        loc2 = i
        loc3 = i + 1

        if loc1 >= 0:
            alive1 = checkLife(previous_array[loc1])
        if 0 <= loc2 < len(previous_array):
            alive2 = checkLife(previous_array[loc2])
        if loc3 < len(previous_array):
            alive3 = checkLife(previous_array[loc3])
        
        if alive1 and alive2 and alive3:
            new_array.append(" ")
        elif alive1 and alive2 and not alive3:
            new_array.append(" ")

        


def checkLife(input_loc):
    if input_loc == ' ' or input_loc == "X":
        return False
    else:
        return True


# add spaces onto the starting array
def fixStart(input_array, num_gen):
    copy_array = copy.deepcopy(input_array)
    for i in range(0, num_gen):
        copy_array.insert(0, " ")
    for j in range(0, num_gen):
        copy_array.append(" ")
    return copy_array


# print out each array on its own line
def printLine(input_array):
    output_str = ""
    for loc in input_array:
        output_str += str(loc)
    print(output_str)


if __name__ == "__main__":
    test1 = [["█"]]
    startSim(test1)