readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]

clean_readings = []

for reading in readings:
    if reading is None:
        continue

    if reading > 0 and reading < 50:
        clean_readings.append(reading)

average = sum(clean_readings) / len(clean_readings)

alerts = []

for reading in clean_readings:
    if reading > 30:
        alerts.append(reading)

print("Clean readings:", clean_readings)
print("Average:", f"{average:.2f}")
print("Alerts:", alerts)