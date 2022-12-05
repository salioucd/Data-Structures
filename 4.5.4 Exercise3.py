Imagine we're writing a program that keeps track of group members for a group project. To do that, we create a function that adds a member to an existing group. It takes three parameters:

- A dictionary of groups, where the keys are group numbers and the values are lists of members

- A specific group number

- The name of a new group member

The function adds the new group member's name to the list of members associated with the group number. Note that this means that instead of the values being integers, floats, or strings like we've seen before, the values themselves are lists.

Here's the function that does this, but it has some blanks:

1| def add_member_to_group(groups, group_number, member_name):
2|     [1] #Get the group to which to add the new member
3|     [2] #Add the member to the group
4|     [3] #Do anything else necessary to finish the function
What code should go in each blank to complete the function as described?

#Blank #1
this_group = groups[group_number]

#Blank #2
this_group.append(member_name)

#Blank #3
No third line is necessary.

The code written on lines 2 through 4 of exercise 4.5.4 Exercise 2 could be condensed down to one line. Which of the following lines could be used to replace it?

return groups[group_number].append(member_name)
