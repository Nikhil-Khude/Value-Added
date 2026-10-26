def highestOccurringElement(nums):
    # Write your code here
    freq={}
    for i in nums:
        if i in freq:
            freq [i]+=1
        else:
            freq[i]=1
    highest=0
    result=nums[0]

    for i in freq:
        if freq[i]>highest:
            highest=freq[i]
            result=i
    return result