import csv

def loadCSV():
    with open('D:/WORK/python/data/retailstore.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


if __name__ == '__main__':
    loadCSV()