from csv import reader, DictReader, writer, DictWriter

print("Using reader:")
with open("files/fighters.csv") as file:
    csv_reader = reader(file)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

print("Using DictReader:")
with open("files/fighters.csv") as file:
    csv_reader = DictReader(file)
    for fighter in csv_reader:
        print(f"{fighter['Name']} is from {fighter['Country']}")

with open("files/fighters2.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
    csv_writer.writerow(["Ken", "Shoryuken"])
    csv_writer.writerow(["Chun-Li", "Hyakuretsukyaku"])

with open("files/fighters3.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({"Character": "Ryu", "Move": "Hadouken"})
    csv_writer.writerow({"Character": "Ken", "Move": "Shoryuken"})
    csv_writer.writerow({"Character": "Chun-Li", "Move": "Hyakuretsukyaku"})
