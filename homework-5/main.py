import os
import csv

with open("classmates.csv", encoding= "utf-8") as f:
    reader_object = csv.reader(f, delimiter=",")
    print(reader_object)


