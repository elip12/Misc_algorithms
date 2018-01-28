# dc_power
# Eli Pandolfo

# Divide and conquer function to raise a number to a power.
# Runs in O(log b)


def power(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        return power(a, b/2) * power(a, b/2)
    else:
        return power(a, (b - 1) / 2) * power(a, (b - 1) / 2) * a
