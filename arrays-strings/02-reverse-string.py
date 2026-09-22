def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# Typical test case
s = ["h", "e", "l", "l", "o"]

reverse_string(s)
print("Typical test case:", s)


# Edge case
s = ["a"]

reverse_string(s)
print("Edge case:", s)