
s1 = str(input("1st string \n"))
s2 = str(input("2nd string \n"))

def find_matching_character(s2, character):
    for index, letter in enumerate(s2):
        if character == letter:
            return index

    return False



def find_LCS(s1, s2):
    # print("s1 is: %s" %s1)
    # print("s2 is: %s" %s2)
    local_CS = []
    for index, character in enumerate(s1):
        # print(character)
        # print(s2)

        match = find_matching_character(s2, character)
        # print(match)
        if match is not False:
            # print(character)
            # print(s1[index+1:])
            # print(s2[match+1:])
            # print("----------\n")
            next_LCS = find_LCS(s1[index+1:], s2[match+1:])
            local_CS.append(character + next_LCS)
    if not local_CS:
        return ""
    return max(local_CS, key = len)


LCS = find_LCS(s1,s2)
print("LCS is: %s" %LCS)
print("length of LCS is: %d" %len(LCS))

