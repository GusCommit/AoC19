
# current_num = 136818
# total = 0

# while True:
#     if current_num == 685979: break
#     first = True
#     ajecent = False
#     larger = True
#     current_num_str = str(current_num)
#     for x in current_num_str:
#         x_int = int(x)
#         if first:
#             first = False
#             prev = x_int
#             continue
        
#         if x_int == prev:
#             ajecent = True
#         elif x_int < prev:
#             larger = False
#             break
#         prev = x_int
#     if larger and ajecent:
#         total += 1
#     current_num += 1
# print(total)

#345 is to low

current_num = 136818
total = 0

while True:
    if current_num == 685979: break
    first = True
    ajecent = False
    larger = True
    total_ajecent = 1
    too_many = False
    legit = False
    current_num_str = str(current_num)
    for x in current_num_str:
        x_int = int(x)
        #If its the first digit, save digit and skip to next itteraton.
        if first:
            first = False
            prev = x_int
            continue

        #Reset the "more than 2 of same parameters"
        if x_int != prev:
            too_many = False
            if total_ajecent == 2:
                legit = True
            total_ajecent = 1
            
        

        if (x_int == prev) and not too_many:
            ajecent = True
            total_ajecent += 1
            if total_ajecent > 2:
                ajecent = False
                too_many = True
        elif x_int < prev:
            larger = False
            break

        prev = x_int
    if larger and (ajecent or legit):
        total += 1
    current_num += 1
print(total)

#345 is to low
#137788 was wrong(fixed)
#1087 to low
#Todo 111122 passerar inte(jk gjorde den visst)
#1088 to low
#Om det stämmer, med de tre sista är samma blir ajecent fel. 144555 passerar inte.