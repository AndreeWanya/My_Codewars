def permutations(s):
    result = []
    if len(s) == 1:
        return list(s)
    if len(s) == 2:
        return list(set([s[0] + s[1], s[1] + s[0]]))
    else:
        for i in range(len(s)):
            s1 = s[:i] + (s[i+1:])
            for permut in permutations(s1):
                c = s[i] + permut
                result.append(c)
        return(list(set(result)))

print(permutations('a'))
print(permutations('ab'))
print(permutations('abc'))
print(permutations('aabb'))
