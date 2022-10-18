# Copyright 2022 by Artur Toom.
# All rights reserved.

#list_duplicates_of taken from https://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

inputFile = open("input.txt", "r")
input_lines = inputFile.readlines()

num_of_pencils = input_lines[0]
pencil_orientation = input_lines[1]
pencil_orientation_list = list(pencil_orientation)

terav = pencil_orientation.count("t")
nyri = pencil_orientation.count("n")
if terav == 0 or nyri == 0:
    output = 0
else:
    keeratav = "t"
    keeratav1 = "n"
    loop = True
    esimene_keeratav_raw = pencil_orientation.find(keeratav)
    viimane_keeratav_raw = pencil_orientation.rfind(keeratav)
    esimene_keeratav = esimene_keeratav_raw + 1
    viimane_keeratav = viimane_keeratav_raw + 1
    output_list = []
    iterations = 0
    while loop == True:
        output_list_addon = str(esimene_keeratav) + "-" + str(viimane_keeratav) + "\n"
        output_list.append(output_list_addon)
        iterations += 1
        for listi_liige in range(esimene_keeratav_raw, viimane_keeratav):
            if str(pencil_orientation_list[listi_liige]) == "t":
                pencil_orientation_list[listi_liige] = "n"
            elif str(pencil_orientation_list[listi_liige]) == "n":
                pencil_orientation_list[listi_liige] = "t"
        try:
            temp_list = list_duplicates_of(pencil_orientation_list, keeratav)

            esimene_keeratav_raw = temp_list[0]
            viimane_keeratav_raw = temp_list[-1]
            esimene_keeratav = esimene_keeratav_raw + 1
            viimane_keeratav = viimane_keeratav_raw + 1
        except:
            loop = False
    loop = True
    esimene_keeratav_raw = pencil_orientation.find(keeratav1)
    viimane_keeratav_raw = pencil_orientation.rfind(keeratav1)
    esimene_keeratav = esimene_keeratav_raw + 1
    viimane_keeratav = viimane_keeratav_raw + 1
    output_list1 = []
    iterations1 = 0
    pencil_orientation_list = list(pencil_orientation)
    while loop == True:
        output_list_addon1 = str(esimene_keeratav) + "-" + str(viimane_keeratav) + "\n"
        output_list1.append(output_list_addon1)
        iterations1 += 1
        for listi_liige1 in range(esimene_keeratav_raw, viimane_keeratav):
            if str(pencil_orientation_list[listi_liige1]) == "t":
                pencil_orientation_list[listi_liige1] = "n"
            elif str(pencil_orientation_list[listi_liige1]) == "n":
                pencil_orientation_list[listi_liige1] = "t"
        try:
            temp_list = list_duplicates_of(pencil_orientation_list, keeratav1)

            esimene_keeratav_raw = temp_list[0]
            viimane_keeratav_raw = temp_list[-1]
            esimene_keeratav = esimene_keeratav_raw + 1
            viimane_keeratav = viimane_keeratav_raw + 1
        except:
            loop = False
    if iterations <= iterations1:
        output = str(iterations) + "\n"
        for output_loop in range(0, iterations):
            output = output + str(output_list[output_loop])
    else:
        output = str(iterations1) + "\n"
        for output_loop in range(0, iterations1):
            output = output + str(output_list1[output_loop])
print(output)
