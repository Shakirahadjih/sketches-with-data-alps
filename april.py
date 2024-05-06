# Open the file
with open("/Users/shakira/Desktop/climate-data-swissmean_regSwiss_1.3.txt", "r") as file:
    # Read lines
    lines = file.readlines()

# Extract April temperatures for the years 2000 to 2024
april_temperatures = []

for line in lines[1:]:  # Skip the header line
    try:
        # Split the line by whitespace
        data = line.split()
        # Extract the year and April temperature (assuming April is the 5th row)
        year = int(data[0])
        april_temperature = float(data[4])  # April is the 5th row (index 4)
        # Append April temperature to the list
        april_temperatures.append((year, april_temperature))
    except (ValueError, IndexError):
        # Skip the header line and handle other potential errors
        continue

# Print April temperatures for each year
for year, april_temperature in april_temperatures:
    print(f"Year: {year}, April Temperature: {april_temperature:.2f} °C")

