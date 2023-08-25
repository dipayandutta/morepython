import csv

ageList = []
def loadCSV():
    with open('D:/WORK/python/data/retailstore.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for ages in reader:
            if ages['Age'] != '':
                ageList.append(ages['Age']) 

    calculateAges(ageList) # function calling 

# function defination
def calculateAges(ageList):
    print(ageList)
    # convert all items in list to int
    ages = []
    ages = [int(x) for x in ageList]
    print(ages)
    print(sum(ages))
    avg = ((sum(ages))/len(ages))
    print(avg)



if __name__ == '__main__':
    loadCSV()