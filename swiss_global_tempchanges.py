# Open the file
with open("/Users/shakira/Desktop/climate-data-swissmean_regSwiss_1.3.txt", "r") as file:
      # Read lines
    lines = file.readlines()

# Extract annual temperatures for the years 2000 to 2024
annual_temperatures = []

for line in lines[1:]:  # Skip the header line
    try:
        # Split the line by whitespace
        data = line.split()
        # Extract the year and annual temperature
        year = int(data[0])
        annual_temperature = float(data[-1])
        # Append annual temperature to the list
        annual_temperatures.append((year, annual_temperature))
    except (ValueError, IndexError):
        # Skip the header line and handle other potential errors
        continue

# Extract annual temperatures for the period 1961-1990
period_1961_1990_temperatures = [temp for year, temp in annual_temperatures if 1961 <= year <= 1990]

# Calculate the average temperature for the period 1961-1990
average_1961_1990_temperature = sum(period_1961_1990_temperatures) / len(period_1961_1990_temperatures)

# Calculate the annual temperature relative to the 1961-1990 average temperature for each year
for year, annual_temperature in annual_temperatures:
    # Calculate the temperature anomaly
    temperature_anomaly = annual_temperature - average_1961_1990_temperature
    # Print the result
    print(f"Year: {year}, Temperature Anomaly: {temperature_anomaly:.2f} °C")