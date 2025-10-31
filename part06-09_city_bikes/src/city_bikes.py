# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    with open(filename) as f:
        return {line.split(';')[3]: (float(line.split(';')[0]), float(line.split(';')[1])) for line in f.readlines()[1:]}
    
def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    d = 0 
    mx_st1 = ''
    mx_st2 = ''
    for index, station1 in enumerate(stations):
        for i in range(index+1, len(stations)):
            d = max(d, distance(stations, station1, list(stations.keys())[i])) 
            if d == distance(stations, station1, list(stations.keys())[i]):
                mx_st1 = station1
                mx_st2 = list(stations.keys())[i]
    
    return (mx_st1, mx_st2, d)

