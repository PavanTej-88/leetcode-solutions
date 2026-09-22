def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


# Typical test case
strs = ["flower", "flow", "flight"]

result = longest_common_prefix(strs)
print("Typical test case:", result)


# Edge case
strs = ["dog", "racecar", "car"]

result = longest_common_prefix(strs)
print("Edge case:", result)