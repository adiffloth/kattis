vowels = ['a', 'e', 'i', 'o', 'u']
s = input()
out = []
i = 0
while i < len(s):
    out.append(s[i])
    if s[i] in vowels:
        i += 2
    i += 1

print(''.join(out))
