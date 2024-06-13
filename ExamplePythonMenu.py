# Basic menu functionality. Translate this into Arduino/C++ code. 

array = ["line1", "line2", "line3", "line4,", "line5", "line6", "line7", "8888888", "999999", "000000", "11111111"]
trueLength = len(array)
window = 5

# Make the array divisible by the window size by adding empty strings.
while len(array) % window != 0:
    array.append("")
   
pointer = 1
position = 1

i = 0
j = i + window

while True:
    subarray = array[i:j]
    print(" ")
    print("SUBARRAY = ", subarray)
    print("POINTER = ", pointer)
    print("POSITION = ", position)
    print("i j = ", i, j)

    command = input()
 
    if command == "u" and position != trueLength:
        print("UP")
        pointer = pointer + 1
        position = position + 1
       
    if command == "d":
        print("DOWN")
        pointer = pointer - 1
        if position > 1:
            position = position - 1


    if position == len(array):
        pointer = pointer - 1
        position = position - 1
        

    if position == j + 1 and position != len(array):
        i = i + window
        j = j + window
        pointer = 1


    if pointer == 0 and i != 0:
        i = i - window
        j = j - window
        pointer = window
 
    if pointer == 0 and i == 0:
        pointer = 1
