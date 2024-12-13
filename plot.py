import csv
import matplotlib.pyplot as plt

list_count_A = []
L_pulseheight = []

list_count_A2 = []
L_pulseheight2 = []

list_count_A3 = []
L_pulseheight3 = []

list_count_A4 = []
L_pulseheight4 = []
# Open the CSV file
with open('book1_600s.csv', mode='r') as spectrum:
    csv_reader = csv.reader(spectrum)

    # Skip the first line (header)
    next(csv_reader)  # This skips the first row

    # Iterate through the rows
    for row in csv_reader:
        pulseheigt, count_A, count_B = row

        list_count_A.append(float(count_A))
        L_pulseheight.append(float(pulseheigt))
        # print(count_A)

with open('book2_600s.csv', mode='r') as spectrum:
    csv_reader = csv.reader(spectrum)

    # Skip the first line (header)
    next(csv_reader)  # This skips the first row

    # Iterate through the rows
    for row in csv_reader:
        pulseheigt, count_A, count_B = row

        list_count_A2.append(float(count_A))
        L_pulseheight2.append(float(pulseheigt))
        # print(count_A)

with open('book3_600s.csv', mode='r') as spectrum:
    csv_reader = csv.reader(spectrum)

    # Skip the first line (header)
    next(csv_reader)  # This skips the first row

    # Iterate through the rows
    for row in csv_reader:
        pulseheigt, count_A, count_B = row

        list_count_A3.append(float(count_A))
        L_pulseheight3.append(float(pulseheigt))
        # print(count_A)

with open('cal_Ge_Cs_2.csv', mode='r') as spectrum:
    csv_reader = csv.reader(spectrum)

    # Skip the first line (header)
    next(csv_reader)  # This skips the first row

    # Iterate through the rows
    for row in csv_reader:
        pulseheigt, count_A, count_B = row

        list_count_A4.append(float(count_A))
        L_pulseheight4.append(float(pulseheigt))
        # print(count_A)

plt.plot(L_pulseheight, list_count_A, linestyle = 'solid', label = "Book 1")
plt.plot(L_pulseheight2, list_count_A2, linestyle = "dotted", label = "Book 2")
plt.plot(L_pulseheight3, list_count_A3, linestyle = 'dashed', label = "Book 3")
plt.plot(L_pulseheight4, list_count_A4, linestyle = 'dashdot', label = "Book 4")
plt.xlabel("Pulseheight (mV)")
plt.ylabel("Counts")
plt.legend()
plt.show()

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(L_pulseheight, list_count_A, linewidth = 1)
axs[0, 0].set_title('Book 1')
axs[0, 1].plot(L_pulseheight2, list_count_A2, 'tab:orange', linewidth = 1)
axs[0, 1].set_title('Book 2')
axs[1, 0].plot(L_pulseheight3, list_count_A3, 'tab:green', linewidth = 1)
axs[1, 0].set_title('Book 3')
axs[1, 1].plot(L_pulseheight4, list_count_A4, 'tab:red', linewidth = 1)
axs[1, 1].set_title('Book 4')


# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()