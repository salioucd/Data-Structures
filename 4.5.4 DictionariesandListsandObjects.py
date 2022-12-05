classes = {"Math" : ["David", "Lucy", "Dana"],
           "Physics" : ["Addison", "Vrushali", "Bilbo"],
           "Chemistry" : ["Sara", "Lugos", "Mireia", "Perle"],
           "Computing" : ["Partha", "Venijamin", "Terra", "Sofia"],
           "History" : ["Tryphon", "Gevorg", "Raza", "Rein"]}

print("Students in Computing:", classes["Computing"])
#Add Francis to History
classes["History"].append("Francis")    
print("Students in History:", classes["History"])

#------------------------------------------------------------------------------

addressBook = {"David": ("555 Home St", "4045551234", "david@david.com"),
               "Lucy" : ("555 Home St", "4045555678", "lucy@lucy.com"),
               "Dana" : ("123 There Rd", "4045559101", "dana@dana.net")}

print("David's Information:", addressBook["David"])
print("Dana's Phone Number:", addressBook["Dana"][1])

#------------------------------------------------------------------------------

addressBook = {"David": {"address" : "555 Home St", "phone" : "4045551234", 
                          "email" : "david@david.com"},
               "Lucy" : {"address" : "555 Home St", "phone" : "4045555678", 
                         "email" : "lucy@lucy.com"},
               "Dana" : {"address" : "123 Here Rd", "phone" : "4045559101", 
                         "email" : "dana@dana.net"}}

print("David's Information:", addressBook["David"])
print("Dana's Phone Number:", addressBook["Dana"]["phone"])

#------------------------------------------------------------------------------

ANSWER_KEY = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "A"}

students={}
students["David"] = {"1" : "A", "2" : "B", "3" : "A", "4" : "B", "5" : "C"}
students["Terra"] = {"1" : "A", "2" : "B", "3" : "C", "4" : "D", "5" : "A"}
students["Lugos"] = {"1" : "A", "2" : "C", "3" : "C", "4" : "D", "5" : "A"}

#For each student and their answers
for (student, answers) in students.items(): 
    grade = 0   #Start grade at 0
    #For each question and answer
    for (question, answer) in answers.items():  
        #If the answer matches ANSWER_KEY's answer...
        if answer == ANSWER_KEY[question]:  
            grade +=1   #Increment their grade
    #Create a new key "grade" and assign it their grade
    students[student]["grade"] = grade  
#For each student and their answers
for (student, answers) in students.items(): 
    #Print the name and grade
    print(student, ": ", answers["grade"], sep = "", end = "; ")

    
    
