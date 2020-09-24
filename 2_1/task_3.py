data = [[2, 2, 1, 4, 1, 1], [10, 1, 1, 2, 1, 1], [1, 2, 8, 4, 9, 1], [9, 2, 4, 4, 1, 0]]

with open("data.txt", "w") as file: #open the file in write-mode(will create a new one if it doesn't exist, and overwrite the existing one, use append-mode to add to a file).
    table = [["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6"]]
    for values in data: # convert each data-value to str and add it to table.
        values_str = []
        for value in values:
            values_str.append(str(value))
        table.append(values_str)
    
    for i in range(len(table)): # write each row to data.txt.
        if i == 0: # if it's the first line(headers) we must use only one tab to get the proper formatting.
            row = table[i]
            for value in row:
                file.write(f"|{value}\t")
            file.write("\n")
        else:
            row = table[i]
            for value in row:
                file.write(f"|{value}\t\t")
            file.write("\n")

def read_first_column(filename: str) -> []:
    result = []

    with open(filename, "r") as file:
        for line in file: # loop through the lines, split it by "|" and assign the value from the first column to the result-list.
            values = line.replace("\t", "").replace("\n", "").split("|")
            result.append(values[1]) # values[0] is the "" before the first "|".

    return result


print(read_first_column("data.txt"))

        

