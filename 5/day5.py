
for noun in range(100):
    #print("Noun is: " + str(noun))
    for verb in range(100):
        #print("Verb is: " + str(noun))
        input = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,5,19,23,2,9,23,27,1,27,5,31,2,31,13,35,1,35,9,39,1,39,10,43,2,43,9,47,1,47,5,51,2,13,51,55,1,9,55,59,1,5,59,63,2,6,63,67,1,5,67,71,1,6,71,75,2,9,75,79,1,79,13,83,1,83,13,87,1,87,5,91,1,6,91,95,2,95,13,99,2,13,99,103,1,5,103,107,1,107,10,111,1,111,13,115,1,10,115,119,1,9,119,123,2,6,123,127,1,5,127,131,2,6,131,135,1,135,2,139,1,139,9,0,99,2,14,0,0]
        while True:
            #print(op_code_index)
            if input[op_code_index] == 99:
                break
            else:
                par1 = input[input[x]]
                # print(par1)
                par2 = input[input[y]]
                if input[op_code_index] == 1:
                    #preform add
                    input[input[z]] = par1 + par2

                elif input[op_code_index] == 2:
                    #preform mul
                    input[input[z]] = par1 * par2
                op_code_index += 4
                #print("Op Code is: " + str(op_code_index))
                x += 4
                y += 4
                z += 4
        #print(input[0])
        if input[0] == 19690720:
            print(100*noun+verb)
            exit()
        op_code_index = 0
        x = 1
        y = 2
        z = 3