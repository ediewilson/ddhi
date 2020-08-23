class Place: 
    # constructor that takes "<placeName>", address, city, lattitude, longitude, and source
    # it's ok if these are blank when initialized
    def __init__(self, name, address, city, lattitude, longitude, source): 
        self.name = name
        self.address = address
        self.city = city 
        
        self.lattitude = lattitude
        self.longitude = longitude

        self.source = source

    
    def getName(self):
        return self.name
        

    def toString(self):
        if self.source is None:
            self.source = "UNKNOWN"
            
        return("\"" +self.name+ "\"," +self.address+ ",\""+self.city+ "\","+self.lattitude+ ","+self.longitude+ ","+self.source+"\n")


    def __repr__(self):
        if self.source is None:
            self.source = "UNKNOWN"
            
        return("\"" +self.name+ "\"," +self.address+ ",\""+self.city+ "\","+self.lattitude+ ","+self.longitude+ ","+self.source+"\n")
