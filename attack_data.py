import csv
from matplotlib import pyplot as plt
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D

filename = 'normal.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  time = []
  dest = []
  sour = []

  max_value = 5
  for index, row in enumerate(reader):
    if index < max_value: 
      source = row[0].split(";")[2]
      destination = row[0].split(";")[3]
      times = row[0].split(";")[1]
      if (source == '' or destination == '' or times == '') :
        continue
      time.append(times)
      dest.append(destination)
      sour.append(source)

  #Plot Data
  # dest for x
  # time for y
  # source for z
  plt.plot(time, sour)  # plotting data
  #Format Plot
  plt.title("Time Progress", fontsize=24)
  plt.xlabel('Dest', fontsize=16)
  plt.ylabel('Time', fontsize=16)
  plt.tick_params(axis='both', which='major', labelsize=16)
  plt.legend()
  plt.show()
  plt.show()