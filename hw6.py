## WRITE TWO TESTS OF EACH TYPE AND USE CLASS STRATEGY TO GUIDE CODING


# Given a name, return a string with the message:

# One for X, one for me.
# Where X is the given name.

# However, if the name is missing, return the string:

# One for you, one for me.

def twofer(name=None):
    if name is not None:
        print("One for " + name + ", one for me")
    else:
        print("One for you, one for me")

#Calculate the Hamming Distance between two DNA strands. (aka, how many different letters per position are their between two strings)

def hamming(dna1, dna2):
    acceptable_dna = ['G','T','A','C']
    count = 0
    if dna1[0] not in acceptable_dna and dna1[0] not in acceptable_dna:
        print("Not acceptable DNA strand")
    elif dna1 == dna2:
        print(count)
    else:
        for letter, check in zip(dna1, dna2):
            if letter is not check:
                count += 1
        print(count)





if __name__ == "__main__":
    
    #tests for twofer
    name = 'Christian'
    twofer(name)
    name2 = 'Ian'
    twofer(name2)
    twofer()
    name3 = None
    twofer(name3)
    name4 = '12dw'
    twofer(name4)
    name5 = '?????'
    twofer(name5)

    dna1 = 'GAGCCTACTAACGGGAT'
    dna2 = 'CATCGTAATGACGGCCT'
    hamming(dna1, dna2)
    dna1 = 'GATCCTACTAACGGGAT'
    dna2 = 'CATCGTAATGACGGCCT'
    hamming(dna1, dna2)
    dna1 = 'GGGGGGGGGGGGGGGGG'
    dna2 = 'TTTTTTTTTTTTTTTTT'
    hamming(dna1, dna2)
    dna1 = 'GGGGGGGGGGGGGGGGG'
    dna2 = 'GGGGGGGGGGGGGGGGG'
    hamming(dna1, dna2)
    dna1 = '123'
    dna2 = '321'
    hamming(dna1, dna2)
    dna1 = '!?!?'
    dna2 = '!?!?'
    hamming(dna1, dna2)