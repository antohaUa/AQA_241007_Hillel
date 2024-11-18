import csv

try:
    # Attempt to open and read a CSV file
    with open("stars.csv", mode="r") as file:
        reader = csv.reader(file)

        # Check if the file is empty
        first_row = next(reader, None)
        if not first_row:
            raise ValueError("The CSV file is empty.")

        # Process the remaining rows
        print("Star Data:")
        for row in reader:
            if len(row) != 3:  # Expecting 3 columns: Star Name, Constellation, Distance
                raise ValueError(f"Malformed row: {row}")

            star_name, constellation, distance = row

            try:
                distance = float(distance)  # Convert distance to a float
            except ValueError:
                raise ValueError(f"Invalid distance value for star '{star_name}': {distance}")

            print(f"{star_name} is in {constellation}, {distance} light-years away.")

except FileNotFoundError:
    print("Error: The specified CSV file does not exist.")
except ValueError as e:
    print(f"Data Error: {e}")
except csv.Error as e:
    print(f"CSV Parsing Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")