import os
print("Current working directory:", os.getcwd())


# Open the text file
with open('climate-data-swissmean_regSwiss_1.3.txt', 'r') as file:
    # Read the contents of the file
    data = file.read()

# Print the contents of the file
print(data)
