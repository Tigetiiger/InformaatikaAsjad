# Copyright 2022 by Artur Toom.
# All rights reserved.


inputFile = open("input.txt", "r")
input_lines = inputFile.readlines()
a = input_lines[1]
N = a.count("N")
S = a.count("S")
E = a.count("E")
W = a.count("W")
NS = N - S
EW = E - W
NS_abs = abs(NS)
EW_abs = abs(EW)
backToBase = NS_abs + EW_abs
output = backToBase
print(output)

