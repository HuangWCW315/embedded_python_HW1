# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = 'sample_input.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

def valid(L):
    if (L['station_id'] == 'C0A880' or L['station_id'] == 'C0F9A0' or L['station_id'] == 'C0G640' or L['station_id'] == 'C0R190' or L['station_id'] == 'C0X260'):
        if (float(L['HUMD']) != -99.0 and float(L['HUMD']) != -999.0):
            return 1
        else:
            return 0
    else:
        return 0

target_data = [['C0A880', 0], ['C0F9A0', 0],['C0G640', 0], ['C0R190', 0], ['C0X260', 0]]
sum = {'C0A880':0, 'C0F9A0':0,'C0G640':0, 'C0R190':0, 'C0X260':0}
times = {'C0A880':0, 'C0F9A0':0,'C0G640':0, 'C0R190':0, 'C0X260':0}
l = [sum, times]
temp_data = list(filter(valid, data))
for p in temp_data:
    if p['station_id'] in sum:
        k =  l[0].get(p['station_id'], 0) + float(p['HUMD'])
        l[0][p['station_id']] = k


for p in target_data:
    if (sum[p[0]] != 0):
        p[1] = sum[p[0]]
    else:
        p[1] = 'None'
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================