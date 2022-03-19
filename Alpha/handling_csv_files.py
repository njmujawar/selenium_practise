import csv


f_path = r"C:\Users\Vidya\PycharmProjects\Python_\csv_files\test.csv"

with open(f_path) as file:
    reader_obj = csv.reader(file)
    # print(reader_obj)
    for line in reader_obj:
        print(line)

with open(f_path) as file:
    reader_obj = csv.DictReader(file)
    # print(reader_obj)
    for line in reader_obj:
        print(line)

with open(f_path, "a") as csv_file:
    writer_obj = csv.writer(csv_file)
    writer_obj.writerow(["TESLA", 100, 37.6])
    data = [("TESLA1", 200, 37.6), ("TESLA2", 300, 37.6), ("TESLA3", 400, 37.6)]
    writer_obj.writerows(data)

path = r"C:\Users\Vidya\PycharmProjects\Python_\csv_files\\"
with open(path+"example.csv", "a") as file:
    dict_writer_obj = csv.DictWriter(file, ["name", "age", "salary"])
    # dict_writer_obj.writeheader()
    dict_writer_obj.writerow({"name": "Ram", "age": 30, "salary": 20000})
    dict_writer_obj.writerows([{"name": "Sita", "age": 25, "salary": 120000}, {"name": "Ravan", "age": 35, "salary": 200000}])











