import numpy as np
import matplotlib.pyplot as plt
import sys

#a)
def make_columns(filename):
    time = np.array([])
    measured = np.array([])
    expected = np.array([])
    with open(filename) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if i == 0:
                continue
            else:
                values = lines[i].replace("\n", "").split(",")
                print(values)
                time = np.append(time, float(values[0]))
                measured = np.append(measured, float(values[1]))
                expected = np.append(expected, float(values[2]))

    return (time, measured, expected)

if __name__ == "__main__":
    columns = make_columns(sys.argv[1])
    plt.plot(columns[0], columns[1], label = "Measured")
    plt.plot(columns[0], columns[2], label = "Expected")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.show()
