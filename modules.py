import statistics

list = [45, 46, 47, 99, 87, 90, 20, 66, 65, 20]

mean  = statistics.mean(list)
median = statistics.median(list)
mode = statistics.mode(list)

print("Mean: " + str(mean))
print("Median: " + str(median))
print("Mode: " + str(mode))

