from Source_files import movies
import csv

source_file = open("C:/Users/Kasia/Desktop/Magisterka/Zaawansowane programowanie/Projekty/Project_Laborki/Lab_7/Source_files/movies.csv")
csv_file = csv.DictReader(source_file)


# with source_file as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(dict(row))

def print(self):
    for row in self.csv_file:
        print(dict(row))


def get(self):
    return print()