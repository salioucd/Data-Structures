  #Create a function called tup_to_dict. tup_to_dict should take one
#parameter: a list of tuples. You can assume each tuple in
#the list has exactly two values.
#
#The function should return a dictionary where the first item
#in each tuple is the key, and the second item in each tuple
#is the corresponding value.
#
#For example:
# colors = [("turquoise", "#40E0D0"), ("red", "#990000")]
# tup_to_dict(colors) -> {"turquoise":"#40E0D0", "red":"#990000"}
#
#Hint: the previous exercise is very similar; this just turns
#it into a function! All our tuples will be color name-color
#value pairs.  
  
#First, we want to create an empty dictionary to add all
    #the colors to:
def tup_to_dict(tuple_list):
    
    color_dict = {}
    
    #Next, we want to iterate over each tuple in the tuple
    #list:
    
    for color_tuple in tuple_list:
        
        #Now for the dictionary-specific part. We want to take
        #the first item of the current tuple and make it a key
        #in the dictionary, and we want its value to be the
        #second item from the current tuple.
        #
        #So, first we get the current first item, which we know
        #will be a color name:
        
        color_name = color_tuple[0]
        
        #And then we get the second value, a hex value for that
        #color:
        
        color_value = color_tuple[1]
        
        #And then we add that key to the dictionary with that
        #value:
        
        color_dict[color_name] = color_value
        
        #We could also have skipped over the temporary variables
        #and just assigned the new key and value directly:
        #
        #color_dict[color_tuple[0]] = color_tuple[1]
    
    #Now that we've looped over each item in the tuple_list, we
    #return color_dict:
    
    return color_dict
  
  
  #Write your function here!
#function defination
def tup_to_dict(tuplist):
    colorDict = {}
    for color in tuplist:
        colorName = color[0]
        colorValue = color[1]
        colorDict[colorName] = colorValue
    return colorDict
  
