import numpy as np
import matplotlib.pyplot as plt

def load_to_dict(filename: str) -> {}:
    income_per_person = {}

    with open(filename, "r") as file:
        lines = file.readlines() # store each line of the file in a list
        for i in range(len(lines)): # loop by range-function so we can check index.
            line = lines[i].replace("\n", "").split(",")
            if i == 0: # if it's the first line, set key to "Time".
                income_per_person["Time"] = np.array([int(line[j]) for j in range(1, len(line))])# Set ndarray of all values on the line except the first as the value to key.
            else:
                # Some countries have name with commas, which means we need to account for that by checking whether or not the value is numeric or not.
                # If the value isnt numeric, we know that it's part of the name, or the key, so we concatenate until we meet a numeric value.
                # To keep commas in the name, we add commas until we're done concatenating the name, then we subtract the last comma
                # separating the name and the following commas.
                key = ""
                starting_index = 0
                for word in line:
                    if not word.isnumeric():
                        key += word + ","
                        starting_index += 1
                    else: 
                        break
                key = key[:len(key)-1]

                income_per_person[key] = np.array([int(line[j]) for j in range(starting_index, len(line))])

    return income_per_person

def find_average_income(income_per_person: {}) -> {}:
    result = {}
    for key in income_per_person:
        if key == "Time":
            continue # jump over "Time" key
        else:
            result[key] = np.mean(income_per_person[key]) # Calculate mean of list associated with key.
    return result

def rank_by_avg_income(average_income: {}) -> {}:
    result = {}
    temp = sorted(average_income.items(), key=lambda x: x[1]) # sorts the dictionary by value and stores the value and the key as a tuple in a list.

    for i in range(len(temp)):
        result[len(temp) - i] = temp[i][0] # store the firts value of the i-th typle, the country, in the value of the key being it's position in the ranking.

    return result

if __name__ == "__main__":
    income_per_person = load_to_dict("income_per_person.csv")
    plt.plot(income_per_person["Time"], income_per_person["Norway"], label="Norway")
    plt.plot(income_per_person["Time"], income_per_person["Sweden"], label="Sweden")
    plt.xlabel("Time")
    plt.ylabel("Income")
    plt.legend()
    plt.title("Income per person over time")
    plt.show()

    arr = rank_by_avg_income(find_average_income(income_per_person))

    print(arr)
    
    for key in arr:
        print(f"{key}: {arr[key]}")
