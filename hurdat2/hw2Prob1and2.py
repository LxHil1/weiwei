mport datetime
import math
cycloneList = []
with open("./hurdat2-1851-2016-041117.txt") as f:
    while True:
        line = f.readline()
        #if end of file, then break;
        if not line:
            break
        line = list(map(str.strip, line.strip().split(",")))
        #if line of intro, initialize the cyclone
        if len(line) == 4:
            cyclone = {}
            cyclone["id"] = line[0]
            cyclone["name"] = line[1]
            cyclone["numberOfRecords"] = int(line[2])
            cyclone["time"] = []
            cyclone["landfall"] = 0
            cyclone["maxSpeed"] = [-math.inf, -1]
            cyclone["isHurricane"] = False
            for i in range(cyclone["numberOfRecords"]):
                line = list(map(str.strip, f.readline().strip().split(",")))
                cyclone["time"].append((line[0], line[1]))
                if line[2] == "L":
                    cyclone["landfall"] += 1
                if line[3] == "HU":
                    cyclone["isHurricane"] = True
                if cyclone["maxSpeed"][0] < int(line[6]):
                    cyclone["maxSpeed"][0] = int(line[6])
                    cyclone["maxSpeed"][1] = i
            cycloneList.append(dict(cyclone))
for cyclone in cycloneList:
    print("Name: {0}".format(cyclone["name"]))
    print("Date range: {0} -- {1}".format(cyclone["time"][0][0], cyclone["time"][-1][0]))
    maxSpeed, timeIndex = cyclone["maxSpeed"]
    print("Maximum speed: {0} knots (Date: {1}, time: {2})".format(maxSpeed, cyclone["time"][timeIndex][0], cyclone["time"][timeIndex][1]))
    print("Number of landfalls: {0}".format(cyclone["landfall"]))
    print("*********************************************************")
