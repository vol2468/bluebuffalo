import csv

def extractByDate(targetDate):
    with open('Data_sorting/simplified.csv', 'r') as readData:
        readCsv = csv.reader(readData)
        data = list(readCsv)
        
    string = "Data_sorting/targetDate" + ".csv"
    with open(string, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date","Location Code","Address","O3 Mean","O3 1st Max Value","O3 1st Max Hour","O3 AQI","CO Mean","CO 1st Max Value","CO 1st Max Hour","CO AQI","SO2 Mean","SO2 1st Max Value","SO2 1st Max Hour","SO2 AQI","NO2 Mean","NO2 1st Max Value","NO2 1st Max Hour","NO2 AQI"])
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
        writer.writerow(["Date","Location Code","Address","O3 Mean","O3 1st Max Value","O3 1st Max Hour","O3 AQI","CO Mean","CO 1st Max Value","CO 1st Max Hour","CO AQI","SO2 Mean","SO2 1st Max Value","SO2 1st Max Hour","SO2 AQI","NO2 Mean","NO2 1st Max Value","NO2 1st Max Hour","NO2 AQI"])
        for row in data:
            if row[1] == str(targetPlaceID):
                writer.writerow(row)

    print("Extracted")

# Create file with only rows of specified date
extractByDate('1/1/2020')

# Create file with only rows of specified place (by ID of 0 ~ 215)
#extractByPlace(47)