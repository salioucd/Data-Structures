#Recall in the previous problem you counted the number of
#instances of a certain first name in a list of full names.
#You returned a dictionary with the name as the key, and the
#number of times it appeared as the value.
#
#Modify that code such that instead of having a count as the
#value, you instead have a list of the full names that had
#that first name. So, each key in the dictionary would still
#be a first name, but the values would be lists of names.
#Make sure to sort the list of names, too.
#
#Name this new function name_lists.


#Add your function here!
def name_lists(fullnames):
    result = dict()
    for name in fullnames:
        first = name.split()[0]
        if first not in result:
            result[first] = []
        result[first].append(name)
    for key in result:
        result[key].sort()
    return result

  
  
#There are multiple ways we could do this, but the simplest
#is just a tiny wrinkle on our answer to the previous
#problem. Previously, we created a counter at 0 for any new
#names, and we incremented it when we found new instances of
#that name. Instead, we now want to create an empty list for
#any new names, and append to it if we find the same name
#again.
#
#So, let's start with our previous code...
def name_lists(names):
    
    name_dict = {}
    
    for name in names:
        
        split_name = name.split()
        first_name = split_name[0]
        
        if not first_name in name_dict:
            
            #Here's where our first change happens. Instead
            #of adding this key with a value of 0, we
            #want to add this key with the value of an empty
            #list:
            
            #name_dict[first_name] = 0
            name_dict[first_name] = []
            
            #So, we just replace the 0 with an [] to replace
            #a value of 0 with the value of an empty list.
         
        #Previously, the value associated with that key was
        #an integer, so we'd add one to it. Now, the value
        #associated with that key is a list, so we can append
        #to it:
        
        #name_dict[first_name] += 1
        name_dict[first_name].append(name)
    
    #Now before we return, we need to do one more thing: sort
    #each list of names.
    for first_name, full_names in name_dict.items():
        full_names.sort()
    
    #And that's all! Everything else is exactly the same.
    return name_dict



# required method, taking a list of full names
def name_lists(fullnames):
    # defining an empty dict
    result = dict()
    # looping through each name in fullnames
    for name in fullnames:
        # fetching first name from current name
        first = name.split()[0]
        # if first is not a key in result dict, adding to result dict with first being
        # the key and an empty list being the value
        if first not in result:
            result[first] = []
        # appending name to the list associated with key=first
        result[first].append(name)
    # now we sort the lists associated with each key, alphabetically
    # note: we are only sorting the values (lists), not the keys of dicts, which is not possible
    for key in result:
        result[key].sort()
    # finally returning list
    return result
  
 #Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Fry', 'Shelba Odle'],
#'David': ['David Joyner', 'David Zuber'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber'],
#'Maren': ['Maren Fry'], 'Nicol': ['Nicol Barthel']}

name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_lists(name_list))

