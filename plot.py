import csv
import matplotlib.pyplot as plt

list_count_A = []
L_pulseheight = []
# Open the CSV file
with open('cal_Ge_Na_2.csv', mode='r') as spectrum:
    csv_reader = csv.reader(spectrum)

    # Skip the first line (header)
    next(csv_reader)  # This skips the first row

    # Iterate through the rows
    for row in csv_reader:
        pulseheigt, count_A, count_B = row

        list_count_A.append(float(count_A))
        L_pulseheight.append(float(pulseheigt))
        # print(count_A)

plt.plot(L_pulseheight, list_count_A)
plt.show()