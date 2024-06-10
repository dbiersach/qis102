# reverse_string.py

s1 = "Forever Young"
print(s1)

s2 = ""
for i in range(len(s1) - 1, -1, -1):
    s2 = s2 + s1[i]
print(s2)

s3 = ""
for c in s1:
    s3 = c + s3
print(s3)

print(s1[::-1])
