def string_reverse(str1):
    rstr1 = ""
    index = len(str1)
    while index>0:
        rstr1 += str1[index -1]
        index = index -1
    return rstr1
print(string_reverse("python"))



str2="abcd"
str3=""
index=len(str2)
while index>0:
    str3 +=str2[index-1]
    index = index-1
print("string reverse",str3)
