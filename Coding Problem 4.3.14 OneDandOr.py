#Write a function called one_dimensional_booleans.
#one_dimensional_booleans should have two parameters:
#a list of booleans called bool_list and a boolean called
#use_and. You may assume that bool_list will be a list
#where every value is a boolean (True or False).
#
#The function should perform as follows:
#
# - If use_and is True, the function should return True if
#   every item in the list is True (simulating the and
#   operator).
# - If use_and is False, the function should return True if
#   any item in the list is True (simulating the or
#   operator).


#Write your function here!

def one_dimensional_booleans(bool_list, use_and):

   

   is_all_true = True

   is_one_true = False

   

   if use_and:

       for b in bool_list:

           if b == False:

               is_all_true = False

               break

   

       if is_all_true:

           return True

       else:

           return False

   

   else:

       for b in bool_list:

           if b == True:

               is_one_true = True

               break

   

       if is_one_true:

           return True

       else:

           return False



#Create a function named one_dimensional_booleans that takes two parameters, bool_list and use_and

#Inside the function:

#Set is_all_true as True and is_one_true as False. These will be used to check the list

#If use_and is True, check each item in the bool_list. If one item is False, set the is_all_true as False and stop the loop. 
#This implies that the list contains a False value. Then check the is_all_true. If it is True, return True. Otherwise, return False.

#If use_and is False, check each item in the bool_list. If one item is True, set the is_one_true as True and stop the loop. 
#This implies that the list contains a True value. Then check the is_one_true. If it is True, return True. Otherwise, return False.


def one_dimensional_booleans(bool_list, use_and):
    
    #There are a lot of different ways you could do this.
    #You could, for example, loop over each item in the
    #list and update a running result based on the new
    #value.
    #
    #Let's try it a simpler way, though. If use_and was
    #False, then our logic is pretty simple: we just
    #return whether 'True' is anywhere in the list:
    
    if not use_and:
        return True in bool_list
    
    #If use_and was True, our logic is just a little bit
    #more complicated. First, we want to find our whether
    #False is in the list. If it is, then we want to
    #return False; if it's not (meaning all the values
    #are True), then we want to return True. So, we want
    #to return the *opposite* of False in bool_list. We
    #can do that with the not operator:
    
    else:
        return not False in bool_list
    
    #Note that we could actually compress these four lines
    #down into only one, but it makes the logic a little
    #harder to follow:
    #return (use_and and True in bool_list) or (not use_and and not False in bool_list)
    
    
    #Below are some lines of code that will test your function.
    
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False.
