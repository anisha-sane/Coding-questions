'''
Created on 12-Mar-2018

@author: User
'''
def palindromePairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    if not words:
        return []
    # unique words
    dic = {w:i for i, w in enumerate(words)}
    print "dic: ",dic
    result = []
    for w in dic:
        i = dic[w]
        print "dic[w]",i
        # find substring to form palindrome pairs
        # since len(substring) <= len(w), there won't be duplicates
        # if len(substring) == len(w), substring is leading s2[::-1]
        for j in range(len(w)):
            s1, s2 = w[:j], w[j:]
            print "s1",s1 , "s2",s2
            print s1[::-1],s2[::-1]
            if s1 == s1[::-1] and s2[::-1] in dic and dic[s2[::-1]] != i:
                result.append([dic[s2[::-1]], i])
                print "Inside first if",result
            if s2 == s2[::-1] and s1[::-1] in dic and i != dic[s1[::-1]]:
                result.append([i, dic[s1[::-1]]])
                print "Inside second if",result
        # '' is only added once as tail, add it again as lead
        if w != '' and w == w[::-1] and '' in dic:
            result.append([dic[''], i])
            print "Inside third if: ",result
    return result

words = ["geekf", "geeks", "or", "keeg"]
a=palindromePairs(words)
print a