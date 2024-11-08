import csv

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

        list_count_A.append(int(count_A))
        L_pulseheight.append(pulseheigt)
        # print(count_A)
 

max_A = max(list_count_A)
print(max(list_count_A))
print(L_pulseheight[list_count_A.index(max_A)])