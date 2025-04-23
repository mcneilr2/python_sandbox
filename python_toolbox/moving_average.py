recentReadings = [21.0, 21.2, 20.8, 22.1, 50.0, 22.0, 21.8]
window = 5
windowMin = window//2
filteredArray = []

for x in range(windowMin,len(recentReadings)-windowMin):
    if abs(recentReadings[x] - recentReadings[x+1]) > 5 or abs(recentReadings[x] - recentReadings[x-1]) > 5:
        spike = max(abs(recentReadings[x] - recentReadings[x+1]), abs(recentReadings[x] - recentReadings[x-1]))
        print(f"Warning: Temperature spike of {spike}degC was detected.")
    window_values = recentReadings[x - windowMin : x + windowMin + 1]
    movingAverage = sum(window_values) / window

    filteredArray.append(movingAverage)

print(f"Filtered readings (degreesC): {filteredArray}")


    
