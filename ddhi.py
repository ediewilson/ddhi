import csv
from place import Place

# add places to palces, add to newPlaceDict when i check if they're new 
places = []
newPlaces = []

placeDict = {}
newPlaceDict = {}


def readFile(fileName):
    # read the new file 
    global places

    with open(fileName,'rb') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',', quotechar='"') 
        i = 0  
        for row in reader:
            if i == 0:
                i += 1
            else:
                places.append(row[0])



# makes the dictionary from existing file 
def makeDict():
    global places

    with open('CSVs/placeDictionary.csv','rb') as csvfile: 
        
        reader = csv.reader(csvfile, delimiter=',', quotechar='"') 
        
        for row in reader:
            name = row[0]
            address = row[1]
            city = row[2]
            lat = row[3]
            longitude = row[4]
            source = row[5]
                
            newPlace = Place(name, address, city, lat, longitude, source) 
            
            placeDict[name] = newPlace


#  outputs file for download 
def outputFile(intervieweeName):
    global places, placeDict, newPlaceDict
    
    newFileName = 'newCSVs/' +intervieweeName + '_placeName.csv'
    outFile = open(newFileName, "w")

    outFile.write("name,address,city,latitude,longitude,source\n")

    for place in places:
            if placeDict.has_key(place):
                placeToAdd = placeDict[place]
            else: 
                print("This place -> " + place + " isn't in our current system. Fill in some new information.")
                # Add resiliancy tests and error catches
                address = raw_input("Enter address: ")
                city = raw_input("Enter city, state: ")
                latitude = raw_input("Enter latitude: ")
                longitude = raw_input("Enter longitude: ")
                source = raw_input("Enter source: ")

                placeToAdd = Place(place, address, city, latitude, longitude, source)
                newPlaceDict[place] = placeToAdd
                placeDict[place] = placeToAdd
            
            outFile.write(placeToAdd.toString())




# Function to update the dictionary file if we update values in the dictionary 
def updatePlaceDict():
    global newPlaceDict
    
    outFile = open('CSVs/placeDictionary.csv', 'a')
    # change to "a" when this is more certain 
    for place in newPlaceDict:
        outFile.write(newPlaceDict[place].toString())


intervieweeName = raw_input("Enter interviewee's last name: ")
nameOfFile = raw_input("Enter the name of the file you're processing: ")

makeDict()
readFile('CSVs/'+ nameOfFile)
outputFile(intervieweeName)
updatePlaceDict()