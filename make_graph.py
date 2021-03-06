import mathplotlib.pyplot as pyplot
import csv
import mathplotlib.ticker as ticker

time = []
download = []
upload = []

with open('test.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        time.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

print(time, "\n", download, "\n", upload)

plt.plot(30,30)
plt.plot(time,download, label='download', color='r')
lt.plot(time,upload, label='upload', color='b')
plt.xlabel('time')
plt.ylabel('speed in Mb/s')
plt.title("internet speed")
plt.legend()
plt.savefig('test_graph.jpg', bbox_inches='tight')
