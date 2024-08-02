string=input("Enter string")
check=' '
for i in range(1,len(string)+1):
    check=string[i:]+string[:i]
    if check==string:
        print(i)
        break