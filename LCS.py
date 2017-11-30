#Bokai Chen
#The program asks for 2 inputs from user
#Returns the LCS of the 2 strings and the length of the LCS


s1 = str(input("1st string \n"))
s2 = str(input("2nd string \n"))


def find_matching_character(s2, character):
    """Function finding a character in a given string and return the index of that character. """
    for index, letter in enumerate(s2):
        if character == letter:
            return index

    return False



def find_LCS(s1, s2):
    """Recursive function to find the LCS between 2 input strings recursively """

#The list of common subsequences between 2 strings
    local_CS = []

#Looping through the first string to find a match in the second string.
    for index, character in enumerate(s1):
        # print(character)
        # print(s2)

        match = find_matching_character(s2, character)

#If matching is found, the right side of the 2 characters of the 2 strings are passed into the function recursively
        if match is not False:
            next_LCS = find_LCS(s1[index+1:], s2[match+1:])
#The returned LCS of the substrings are appended to the mathing characters
            local_CS.append(character + next_LCS)
    if not local_CS:
        return ""
#The longest of the list of common subsequence is returned
    return max(local_CS, key = len)


LCS = find_LCS(s1,s2)
print("LCS is: %s" %LCS)
print("length of LCS is: %d" %len(LCS))

