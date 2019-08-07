# -*- coding: utf-8 -*-
import copy
from time import sleep

def playGame(input_mat, duration = 10, num_wait = 1.0, input_char = "O"):
    printMatrix(input_mat)
    current_mat = copy.deepcopy(input_mat)

    for t in range(1, duration):
        sleep(num_wait)
        new_mat = copy.deepcopy(current_mat)
        for i in range(0, len(current_mat)):
            for j in range(0, len(current_mat[i])):
                new_mat[i][j] = applyRules(current_mat, i, j, input_char)
        printMatrix(new_mat)
        current_mat = copy.deepcopy(new_mat)


def applyRules(mat_to_change, row, column, input_char):
    total_neighbors = 0

    for i in range(row-1, row+2):
        for j in range(column-1, column+2):
            curr_row = i
            curr_col = j
            if i == -1:
                curr_row = len(mat_to_change) - 1
            elif i == len(mat_to_change):
                curr_row = 0

            if j == -1:
                curr_col = len(mat_to_change[curr_row]) - 1
            elif j == len(mat_to_change[curr_row]):
                curr_col = 0

            if 0 <= curr_row < len(mat_to_change):
                if 0 <= curr_col < len(mat_to_change[curr_row]):
                    if curr_row != row or curr_col != column:
                        if checkLife(mat_to_change[curr_row][curr_col]):
                            total_neighbors += 1

    if checkLife(mat_to_change[row][column]):
        if total_neighbors < 2:
            return " "
        elif total_neighbors > 3:
            return " "
        else:
            return input_char
    else:
        if total_neighbors == 3:
            return input_char
        else:
            return " "
                   

def printMatrix(input_mat):
    output_str = ""
    for i in range(0, len(input_mat)):
        for j in range(0, len(input_mat[i])):
            output_str += input_mat[i][j]
            output_str += " "
        output_str += "\n"
    print(output_str)


def checkLife(input_loc):
    if input_loc == ' ' or input_loc == "X":
        return False
    else:
        return True



if __name__ == "__main__":
                # 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37
    gosper_glider_gun = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O','O',' ',' ',' ',' ',' ',' ','O','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O','O',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O',' ',' ',' ','O',' ',' ',' ',' ','O','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O','O',' ',' '],
                ['O','O',' ',' ',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ','O',' ',' ',' ','O','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                ['O','O',' ',' ',' ',' ',' ',' ',' ',' ','O',' ',' ',' ','O',' ','O','O',' ',' ',' ',' ','O',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O',' ',' ',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','O','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],]
    
    simple_glider = [[' ','O',' ',' ',' ',' ',' ',' '],
                     [' ',' ','O',' ',' ',' ',' ',' '],
                     ['O','O','O',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ',' ']]

    playGame(gosper_glider_gun, duration = 100, num_wait = 0.05)