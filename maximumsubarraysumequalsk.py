'''
Created on 16-Feb-2018

@author: User
'''
nums=[]
def maxsubarraysumequalsk(nums,k):
    dic={0:-1}
    if len(nums)==0:
        return 0
    sum=0
    maxlen=0
    
    for i in xrange(len(nums)):
        print nums[i]
        sum+=nums[i]
        if sum==k:
            maxlen=i+1
        diff=sum-k
        if dic.get(diff,None) is not None:
            i=i-dic[diff]
            maxlen=max(maxlen,i)
        if dic.get(sum,None) is None:
            dic[sum]=i
    
    return maxlen

nums=[1,2,3,4,5]
b=int(raw_input("Enter k: "))
c=maxsubarraysumequalsk(nums, b)
print "Anser: ",c