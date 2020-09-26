import numpy as np
import matplotlib.pyplot as plt

# Import the data from the csv_file into an ndarray with shape (2, n) where n denotes the number of columns.
glob_temp_anoms = np.loadtxt("glob_temp_anom_1.csv", delimiter=",")

# Reshape from (m,n) to (n,m). Gives one array with all the years, and another with all the values.
glob_temp_anoms_T = np.transpose(glob_temp_anoms)

# Import data as ealier
glob_temp_anoms_2 = np.loadtxt("glob_temp_anom_2.csv", delimiter=",")

# Transpose it
glob_temp_anoms_2_T = np.transpose(glob_temp_anoms_2)

# Plot them. For simplicity's sake, i've done one plotting(the final one), but it would be the same if I were to plot either of them alone as in task b. Now you only get one figure.
plt.plot(glob_temp_anoms_T[0], glob_temp_anoms_T[1], glob_temp_anoms_2_T[0], glob_temp_anoms_2_T[2], label="Temperature Anomaly")
plt.xlabel("Time")
plt.ylabel("Temperature Anomaly")
plt.title("Global temperature anomalies")
plt.legend()
plt.show()

# Because the values are only defined at each year, so there are multiple values per x-value, vertical lines appear.