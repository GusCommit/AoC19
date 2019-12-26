# puzzel_input = [3,225,1,225,6,6,1100,1,238,225,104,0,101,20,183,224,101,-63,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1101,48,40,225,1101,15,74,225,2,191,40,224,1001,224,-5624,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,62,60,225,1102,92,15,225,102,59,70,224,101,-885,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,35,188,224,1001,224,-84,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,66,5,224,1001,224,-65,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1002,218,74,224,101,-2960,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,49,55,224,1001,224,-104,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,43,46,225,1102,7,36,225,1102,76,30,225,1102,24,75,224,101,-1800,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,43,40,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,554,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,644,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
# print(puzzel_input[1])
# op_code_index = 0
# index_par1 = 1
# index_par2 = 2
# index_par3 = 3

# computer_input = int(input("Enter your input: "))

# while True:
#     OPCODE = puzzel_input[op_code_index]
#     OPCODE_list = list(str(OPCODE))
#     OPCODE_list.reverse()
#     try:
#         operation = int(OPCODE_list[1] + OPCODE_list[0])
#     except:
#         operation = int(OPCODE_list[0])

#     try:
#         mode_par1 = int(OPCODE_list[2])
#     except:
#         mode_par1 = 0

#     try:
#         mode_par2 = int(OPCODE_list[3])
#     except:
#         mode_par2 = 0

#     try:
#         mode_par3 = int(OPCODE_list[4])
#     except:
#         mode_par3 = 0

#     #Check if program should EXIT..
#     if operation == 99:
#         break
#     #..otherwise, preform operation.
#     else:
#         #Addition
#         if operation == 1:

#             if mode_par1 == 0:
#                 par1 = puzzel_input[puzzel_input[index_par1]]
#             elif mode_par1 == 1:
#                 par1 = puzzel_input[index_par1]

#             if mode_par2 == 0:
#                 par2 = puzzel_input[puzzel_input[index_par2]]
#             elif mode_par2 == 1:
#                 par2 = puzzel_input[index_par2]

#             if mode_par3 == 0:
#                 par3 = puzzel_input[puzzel_input[index_par3]]
#             elif mode_par3 == 1:
#                 par3 = puzzel_input[index_par3]         

#             puzzel_input[puzzel_input[index_par3]] = par1 + par2
#             op_code_index += 4
#             index_par1 += 4
#             index_par2 += 4
#             index_par3 += 4

#         #Multiplication
#         elif operation == 2:

#             if mode_par1 == 0:
#                 par1 = puzzel_input[puzzel_input[index_par1]]
#             elif mode_par1 == 1:
#                 par1 = puzzel_input[index_par1]

#             if mode_par2 == 0:
#                 par2 = puzzel_input[puzzel_input[index_par2]]
#             elif mode_par2 == 1:
#                 par2 = puzzel_input[index_par2]

#             if mode_par3 == 0:
#                 par3 = puzzel_input[puzzel_input[index_par3]]
#             elif mode_par3 == 1:
#                 par3 = puzzel_input[index_par3]   

#             puzzel_input[puzzel_input[index_par3]] = par1 * par2
#             op_code_index += 4
#             index_par1 += 4
#             index_par2 += 4
#             index_par3 += 4

#         #Save only parameter to pos(parameter)
#         elif operation == 3:

#             if mode_par1 == 0:
#                 par1 = puzzel_input[puzzel_input[index_par1]]
#             elif mode_par1 == 1:
#                 par1 = puzzel_input[index_par1]

#             puzzel_input[puzzel_input[index_par1]] = computer_input
#             op_code_index += 2
#             index_par1 += 2
#             index_par2 += 2
#             index_par3 += 2
#         #Output value of parameter(Immediate or Memory)
#         elif operation == 4:

#             if mode_par1 == 0:
#                 par1 = puzzel_input[puzzel_input[index_par1]]
#             elif mode_par1 == 1:
#                 par1 = puzzel_input[index_par1]

#             print(par1)
#             op_code_index += 2
#             index_par1 += 2
#             index_par2 += 2
#             index_par3 += 2

#----Part 2----#

puzzel_input = [3,225,1,225,6,6,1100,1,238,225,104,0,101,20,183,224,101,-63,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1101,48,40,225,1101,15,74,225,2,191,40,224,1001,224,-5624,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,62,60,225,1102,92,15,225,102,59,70,224,101,-885,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,35,188,224,1001,224,-84,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,66,5,224,1001,224,-65,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1002,218,74,224,101,-2960,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,49,55,224,1001,224,-104,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,43,46,225,1102,7,36,225,1102,76,30,225,1102,24,75,224,101,-1800,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,43,40,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,554,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,644,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
print(puzzel_input[1])
op_code_index = 0
index_par1 = 1
index_par2 = 2
index_par3 = 3


computer_input = int(input("Enter your input: "))

while True:
    OPCODE = puzzel_input[op_code_index]
    OPCODE_list = list(str(OPCODE))
    OPCODE_list.reverse()
    try:
        operation = int(OPCODE_list[1] + OPCODE_list[0])
    except:
        operation = int(OPCODE_list[0])

    try:
        mode_par1 = int(OPCODE_list[2])
    except:
        mode_par1 = 0

    try:
        mode_par2 = int(OPCODE_list[3])
    except:
        mode_par2 = 0

    try:
        mode_par3 = int(OPCODE_list[4])
    except:
        mode_par3 = 0

    #Check if program should EXIT..
    if operation == 99:
        break
    #..otherwise, preform operation.
    else:
        #Addition
        if operation == 1:

            if mode_par1 == 0:
                par1 = puzzel_input[puzzel_input[index_par1]]
            elif mode_par1 == 1:
                par1 = puzzel_input[index_par1]

            if mode_par2 == 0:
                par2 = puzzel_input[puzzel_input[index_par2]]
            elif mode_par2 == 1:
                par2 = puzzel_input[index_par2]

            if mode_par3 == 0:
                par3 = puzzel_input[puzzel_input[index_par3]]
            elif mode_par3 == 1:
                par3 = puzzel_input[index_par3]         

            #Actual operation
            puzzel_input[puzzel_input[index_par3]] = par1 + par2
            
            op_code_index += 4
            index_par1 += 4
            index_par2 += 4
            index_par3 += 4

        #Multiplication
        elif operation == 2:

            if mode_par1 == 0:
                par1 = puzzel_input[puzzel_input[index_par1]]
            elif mode_par1 == 1:
                par1 = puzzel_input[index_par1]

            if mode_par2 == 0:
                par2 = puzzel_input[puzzel_input[index_par2]]
            elif mode_par2 == 1:
                par2 = puzzel_input[index_par2]

            if mode_par3 == 0:
                par3 = puzzel_input[puzzel_input[index_par3]]
            elif mode_par3 == 1:
                par3 = puzzel_input[index_par3]   

            #Actual operation
            puzzel_input[puzzel_input[index_par3]] = par1 * par2
            
            op_code_index += 4
            index_par1 += 4
            index_par2 += 4
            index_par3 += 4

        #Save only parameter to pos(parameter)
        elif operation == 3:

            if mode_par1 == 0:
                par1 = puzzel_input[puzzel_input[index_par1]]
            elif mode_par1 == 1:
                par1 = puzzel_input[index_par1]
            
            #Actual operation
            puzzel_input[puzzel_input[index_par1]] = computer_input
            
            op_code_index += 2
            index_par1 += 2
            index_par2 += 2
            index_par3 += 2
        #Output value of parameter(Immediate or Memory)
        elif operation == 4:

            if mode_par1 == 0:
                par1 = puzzel_input[puzzel_input[index_par1]]
            elif mode_par1 == 1:
                par1 = puzzel_input[index_par1]

            #Actual operation
            print(par1)

            op_code_index += 2
            index_par1 += 2
            index_par2 += 2
            index_par3 += 2

        elif operation == 5:
            
            if mode_par1 == 0:
                par1 = puzzel_input[puzzel_input[index_par1]]
            elif mode_par1 == 1:
                par1 = puzzel_input[index_par1]

            if mode_par2 == 0:
                par2 = puzzel_input[puzzel_input[index_par2]]
            elif mode_par2 == 1:
                par2 = puzzel_input[index_par2]

            #Actual operation
            if par1 != 0:
                op_code_index = par2
                index_par1 = par2+1
                index_par2 = par2+2
                index_par3 = par2+3

            else:
                op_code_index += 2
                index_par1 += 2
                index_par2 += 2
                index_par3 += 2
            
        