def alternatingCharacters(s):
    count = 0
    if len(s) == 0:
        return None
    start, end = 0, 1
    for i in range(0,len(s)-1):
        print i,start,end
        if s[start] == s[end]:
            count+=1
            print count
            end +=1
        else:
            start = end
            end +=1
        i+=1
    return count


a=alternatingCharacters("AAABBBAABB")
print a