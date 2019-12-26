input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,5,19,23,2,9,23,27,1,27,5,31,2,31,13,35,1,35,9,39,1,39,10,43,2,43,9,47,1,47,5,51,2,13,51,55,1,9,55,59,1,5,59,63,2,6,63,67,1,5,67,71,1,6,71,75,2,9,75,79,1,79,13,83,1,83,13,87,1,87,5,91,1,6,91,95,2,95,13,99,2,13,99,103,1,5,103,107,1,107,10,111,1,111,13,115,1,10,115,119,1,9,119,123,2,6,123,127,1,5,127,131,2,6,131,135,1,135,2,139,1,139,9,0,99,2,14,0,0]
#input = [1,0,0,0,99]
op_code_index = 0
index_par1 = 1
index_par2 = 2
index_par3 = 3

while True:
    OPCODE = input[op_code_index]
    OPCODE_list = list(str(OPCODE))
    OPCODE_list.reverse()
    try:
        operation = int(OPCODE_list[0] + OPCODE_list[1])
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
        mode_par3 = int(OPCODE_list[3])
    except:
        mode_par3 = 0

    #Check if program should EXIT..
    if OPCODE == 99:
        break
    #..otherwise, preform operation.
    else:
        #Addition
        if OPCODE == 1:  
            # par1 = input[input[x]]
            # par2 = input[input[y]]
            input[input[index_par3]] = input[input[index_par1]] + input[input[index_par2]]
        #Multiplication
        elif OPCODE == 2:
            # par1 = input[input[x]]
            # par2 = input[input[y]]
            input[input[index_par3]] = input[input[index_par1]] * input[input[index_par2]]
        #Save only parameter to pos(parameter)

        
        op_code_index += 4
        print(op_code_index)
        index_par1 += 4
        index_par2 += 4
        index_par3 += 4

print(input[0])