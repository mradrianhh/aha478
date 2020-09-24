
def read_csv(filename: str, skiplines = 0) -> []:
    """
        Reads the csv-file found by "filename" and skips the number of lines given by "skiplines".
        Returns a list of lines where each line is a list containing it's words.
    """
    result = []
    with open(filename, "r") as file:
        for line in file:
            # skip the lines until we've skipped as many as specified.
            if skiplines == 0: 
                values = line.replace("\n", "").split(",") # filter out newlines and split the line by the comma.
                result.append(values) 
            else:
                skiplines -= 1
    
    return result

csv = read_csv("trees.csv", 1)

# Too basic
csv_floats = []
for values in csv:
    arr = []
    for value in values:
        arr.append(float(value))
    csv_floats.append(arr)

# Russian hackerboy do like this.
csv_floats = list(map(lambda line: list(map(float, line)), csv)) # for each list in the list, I convert each object to float.

print(csv_floats[0][0] + csv_floats[0][1])