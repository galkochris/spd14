# Given a list of n numbers, determine if it contains any duplicate numbers.


#Psuedo Code

#some list

#create some holder list, to add values to once looped over in the main list, and a duplicate holder

#first iterate over the list for all items in the list

#check if that list item exists in the holder list

#if the item does not exist in the holder list add it

#if the item DOES exist in the holder, add it to the duplicate holder, if it isn't already in the duplicate holder

#once the loop is complete, return all items in the duplicate holder list



#Code

def find_duplicates(items):

    temp_non_dup = []
    dups =[]

    for item in items:
        if item not in temp_non_dup:
            temp_non_dup.append(item)
        elif item not in dups:
            dups.append(item)
        
    print(dups)



if __name__ == "__main__":
    list1 = [1, 2, 2, 3]
    find_duplicates(list1)    