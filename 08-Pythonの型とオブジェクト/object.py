stations = ["東京", "品川", "新横浜", "小田原"]
print(stations)
print(f"len {len(stations)}")

stations.insert(1, "a")
print(stations)
print(f"len {len(stations)}")

stations[1] = "b"
print(stations)
print(f"len {len(stations)}")

del stations[1]
print(stations)
print(f"len {len(stations)}")

for station in stations:
    print(station)

