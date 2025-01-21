import csv  


def write(filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Define the schema (headers)
        writer.writerow(["name", "age", "salary"])
        
        # Write data rows
        writer.writerow(["John", 30, 50000])
        writer.writerow(["Alice", 25, 60000])
        writer.writerow(["Bob", 40, 70000])

def read(filename):
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        
        # Extract schema from the first row
        header = next(reader)
        print("Schema:", header)  
        
        for row in reader:
            print("Record:", row)

def data_types(filename):
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            # Convert age to integer
            age = int(row[1])

            # Convert salary to float
            salary = float(row[2])

            # Convert to boolean
            is_manager = row[3] == "TRUE"

            print("Age:", age, "Salary:", salary, "Is Manager:", is_manager)


def main():
    write("data.csv")
    read("data.csv")
    data_types("csv_datatypes.csv")


if __name__ == "__main__":
    main()
