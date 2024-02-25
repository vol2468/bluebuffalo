import csv

def extractByDate(targetDate):
    with open('Data_sorting/simplified.csv', 'r') as readData:
        readCsv = csv.reader(readData)
        data = list(readCsv)
        
    string = "Data_sorting/targetDate" + ".csv"
    with open(string, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            if row[0] == targetDate:
                writer.writerow(row)

    print("Extracted")

def extractByPlace(targetPlaceID):
    with open('Data_sorting/simplified.csv', 'r') as readData:
        readCsv = csv.reader(readData)
        data = list(readCsv)
    
    string = "Data_sorting/targetPlace" + ".csv"
    with open(string, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            if row[1] == str(targetPlaceID):
                writer.writerow(row)

    print("Extracted")

# Create file with only rows of specified date
#extractByDate('1/1/2000')

# Create file with only rows of specified place (by ID of 0 ~ 215)
extractByPlace(47)