# second_highest
# Eli Pandolfo

# finds second highest element in a list in O(n) time

def sec_highest(A):
    for index, e in enumerate(A):
        if index == 0:
            highest = e
        elif index == 1:
            if e > highest:
                second = highest
                highest = e
            else:
                second = e
        else:
            if e > highest:
                second = highest
                highest = e
            elif e > second:
                second = e
    return second
