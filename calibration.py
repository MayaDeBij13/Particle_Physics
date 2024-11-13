import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

list_count_A = []
L_pulseheight = []
# Open the CSV file
with open('cal_test_2.csv', mode='r') as spectrum:
    csv_reader = csv.reader(spectrum)

    # Skip the first line (header)
    next(csv_reader)  # This skips the first row

    # Iterate through the rows
    for row in csv_reader:
        pulseheigt, count_A, count_B = row

        list_count_A.append(float(count_A))
        L_pulseheight.append(float(pulseheigt))
        # print(count_A)
 

max_A_1 = max(list_count_A)
index_max_A1 = list_count_A.index(max_A_1)

max_A_2 = max(list_count_A[index_max_A1 + 2:])
index_max_A2 = list_count_A.index(max_A_2)


pulseheight_A1 = float(L_pulseheight[index_max_A1])
pulseheight_A2 = float(L_pulseheight[index_max_A2])

print(pulseheight_A1, pulseheight_A2)

print(f"De eerste piek heeft {max_A_1} counts en een pulseheight van {pulseheight_A1} mV")
print(f"De tweede piek heeft {max_A_2} counts en een pulseheight van {pulseheight_A2} mV")

Energy = [511, 1275]
Ph = [pulseheight_A1, pulseheight_A2]



def fit_function(Energy, a, b):
    Ph = a * Energy + b
    return Ph


# Fit the curve
params, covariance = curve_fit(fit_function, Energy, Ph)

# Extract fitted parameters
a, b = params
print(f"Fitted parameters: a = {a}, b = {b}")

# Generate fitted values for plotting
Ph_fitted = []
for item in Energy:
    Ph_fitted.append(fit_function(item, a, b))

plt.plot(L_pulseheight, list_count_A)
plt.show()

# Plot the original data and the fitted line
plt.scatter(Energy, Ph, label="Data")
plt.plot(Energy, Ph_fitted, color="red", label=f"Fitted Line: Ph = (E - {b:.2f}) / {a:.2f}")
plt.xlabel("Energy")
plt.ylabel("Pulseheigth")
plt.legend()
plt.show()


cesium_counts = []
cesium_pulseheight = []
with open('cal_cs_1.csv', mode='r') as cs_spectrum:
    csv_reader = csv.reader(cs_spectrum)

    # Skip the first line (header)
    next(csv_reader)  # This skips the first row

    # Iterate through the rows
    for row in csv_reader:
        pulseheigt, count_A, count_B = row

        cesium_counts.append(float(count_A))
        cesium_pulseheight.append(float(pulseheigt))
        # print(count_A)

cs_energies = []

for item in cesium_pulseheight:
    eng = (item - b) / a
    cs_energies.append(eng)

plt.plot(cs_energies, cesium_counts)
plt.xlim(0, 2000)
plt.show()