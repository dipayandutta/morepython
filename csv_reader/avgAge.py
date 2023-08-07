import csv

ageList = []
def loadCSV():
    with open('D:/WORK/python/data/retailstore.csv',newline='') as csvFile:
        reader = csv.DictReader(csvFile)
        for ages in reader:
            if ages['Age'] != '':
                ageList.append(ages['Age'])

    displayAges(ageList)

def displayAges(ageList):
    print("List of ages")
    # convert all items in list to integer
    ages = []
    ages = [int(x) for x in ageList]
    print(ages)
    print(sum(ages))
    avg = ((sum(ages))/len(ages))
    print(int(avg))

    

if __name__ == '__main__':
    loadCSV()