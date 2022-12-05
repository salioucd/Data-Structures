myString = "This is the string whose words we would like to count. This string contains some repeated words, as well as some unique words. It contains punctuation, and it contains words that are capitalized in different ways. If the method we write runs correctly, it will count 4 instances of the word 'it', 3 instances of the word 'this', and 3 instances of the word 'count'."

myString = myString.replace(".","") #Remove periods
myString = myString.replace(",","") #Remove commas
myString = myString.replace("'","") #Remove apostrophes
myString = myString.lower() #Make all lower case
mySplitString = myString.split() #Split by spaces

wordDictionary = {} #Create empty dictionary
for word in mySplitString:  #For each word in the split string
    if word in wordDictionary:  #If it's already been found...
        wordDictionary[word] += 1   #Add one to its count
    else:   #Otherwise...
        wordDictionary[word] = 1 #Create it with value 1

print(wordDictionary)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

seatingChart = {"David" : 3, "Lucy" : 3, "Dana" : 2,
                "Addison" : 2, "Vrushali" : 1, "Bilbo" : 3,
                "Sara" : 1, "Lugos" : 1, "Mireia" : 1,
                "Partha" : 2, "Venijamin" : 1, "Terra" : 2, 
                "Tryphon" : 3, "Gevorg" : 1, "Raza" : 3,
                "Rein" : 3, "Sofia" : 2, "Perle" : 2}

#For each name, table pair in the seating chart
for (name, table) in seatingChart.items():  
    #Print the table for the name
    print(name, " is seated at table #", table, sep="")  

print()
#For each table number
for i in range(1, 4):   
    print("The guests at table #", i, " are: ", sep="", end="")
    #For each name, table pair
    for (name, table) in seatingChart.items():  
        #If the table numer is this number
        if i == table:  
            #Print the name
            print(name, end=" ")    
    print()


