# Copyright 2022 by Artur Toom.
# All rights reserved.
import time
start_time = time.time_ns()


#@profile
def ETTE(list, pos1, pos2):
    liigutatavadList = []
    liigutatavadList.extend(list[pos1: pos2])
    del list[pos1: pos2]
    list[0:0] = liigutatavadList
    return list

#@profile
def TAHA(list, pos1, pos2):
    list.extend(list[pos1: pos2])
    del list[pos1: pos2]
    return list

#@profile
def POORA(list, pos1, pos2):
    list[pos1: pos2] = list[pos1: pos2][::-1]
    return list
"""
    liigutatavadList = list[pos1: pos2]
    liigutatavadList.reverse()
    del list[pos1: pos2]
    list[int(pos1):int(pos1)] = liigutatavadList
    return list
"""

#@profile
def PUNASEID(list, pos1, pos2):
    l=len([i for i in range(pos1, pos2) if list[i]=='P'])
    return l

#@profile
def ROHELISI(list, pos1, pos2):
    l=len([i for i in range(pos1, pos2) if list[i]=='R'])
    return l
#@profile
def SINISEID(list, pos1, pos2):
    l=len([i for i in range(pos1, pos2) if list[i]=='S'])
    return l
#@profile
def Dict(input_lines):
    itemDict = dict()
    for i in range(2, len(input_lines)):
        dictNum = i - 1
        itemDict[dictNum] = input_lines[i].split()
    return itemDict



inputFile = open("input.txt", "r")
input_lines = inputFile.readlines()

list = list(input_lines[1])
del list[-1]

itemDict = Dict(input_lines)
outputList = []

scope = locals()

for i in range(1, len(input_lines) - 1):
    if itemDict[i][0] in ("ETTE", "TAHA", "POORA"):
        list = eval(itemDict[i][0] + "(list, int(itemDict[{}][1]) - 1, int(itemDict[{}][2]))".format(i, i))
    else:
        outputList.append(str(eval(itemDict[i][0] + "(list, int(itemDict[{}][1]) - 1, int(itemDict[{}][2]))".format(i, i))))

output = ""
end_time = time.time_ns()
output = "\n".join(outputList)

print(output)
print("\nTerve aeg koos compilimisega: " + str(time.process_time()))
print("programmi jooksmise aeg: " + str((end_time - start_time)) + " ns - vhel lühematega ei näita aga siis tuleb mitu korda lugeda")