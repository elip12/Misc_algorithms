# Eli Pandolfo
# finds longest palindrome in non-sequential subsequence of a string
# reference: https://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/

s = 'asvieetionakpoftagtjolpwanotmis'

def pal(s):

    # matrix stores longest palindrome starting at i and ending at j
    store = [[1 for e in range(len(s))] for f in range(len(s))]
    pals = [['0' for e in range(len(s))] for f in range(len(s))]

    for n in range(len(s)):
        pals[n][n] = s[n]

    # build matrix by substring length.
    # l is the length of the substring we are searching for a palindrome in
    # we can start at 2 because the matrix is already filled with ones, 
    # because every single char is itself a palindrome
    for l in range(2, len(s) + 1):
        # i is the starting position of every subsequence. It goes from 0
        # to length s - l
        for i in range(len(s) + 1 - l):
            # j is i + cl, the ending position of a substring starting at i with length l
            j = i + l - 1

            # if the start and end are different, find the largest palindrome within that substring that is 1 char shorter
            # since we build the matrix by increasing substring length, this subproblem is guaranteed to be stored.
            if s[i] != s[j]:
                if store[i + 1][j] > store[i][j - 1]:
                    store[i][j] = store[i + 1][j]
                    pals[i][j] = pals[i + 1][j]
                else:
                    store[i][j] = store[i][j - 1]
                    pals[i][j] = pals[i][j - 1]

            # else, the start and end are the same char: a palindrome is guaranteed.
            # if the length is 2, the palindrome's length must be 2.
            elif l == 2:
                store[i][j] = 2
                pals[i][j] = s[i] + s[i]

            # else, the start and end are not adjacent but are the same char. We are guarantted a
            # palindrome, but its length is determined by the existance of any palindrome inside
            # this substring: since the start and end are guaranteed to form a palindrome,
            # the length of this palindrome is 2 + the length of the longest palindrome between
            # those 2 chars, which is a subproblem that is guaranteed to be stored already
            # (because we build from shortest pal length to longest)
            else:
                store[i][j] = 2 + store[i + 1][j - 1]
                pals[i][j] = s[i] + pals[i + 1][j - 1] + s[j]

    # print lengths matrix
    # print(store)

    # print strings matrix
    # for f in pals:
    #     temp = ''
    #     for e in f:
    #         temp += e + ', ' 
    #     print(temp, '\n')

    longest = store[0][len(s) - 1]
    pal = pals[0][len(s) - 1]

    return longest, pal

print(pal(s))
