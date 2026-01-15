''' FIRST PROBLEM : Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.'''
def dup_k_dis(lis1,k):
    l=len(lis1)
    lis1i=set()
    for i in range(l):
        if lis1[i] in lis1i:
            return "Yes"
        lis1i.add(lis1[i])
        if (i>=k):
            lis1i.remove(lis1[i-k])    
    return 'No'          
if __name__=="__main__":
    lis1=[1,2,3,4,1,2,3,4] 
    k=4 
    print(dup_k_dis(lis1,k))     



''' SECOND PROBLEM : Given an array arr[], sort the array according to the following relations:  

arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n
Find the resultant array.[consider 1-based indexing]'''    
def rearrange_array(lis2):
    lis2.sort()
    l=len(lis2)
    result=[0]*l
    ktr,ktr1=0,l-1
    for i in range(l):
        if (i+1) % 2==0:
            result[i]=lis2[ktr1]
            ktr1-=1
        else:
            result[i]=lis2[ktr]    
            ktr+=1
    return result
if __name__=="__main__":
    lis2=[1,2,2,1]
    print(rearrange_array(lis2))    


''' THIRD PROBLEM : Given an integer array arr[], compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.'''
def sum_all_subarray(lis3):
    l=len(lis3)
    result=0
    for i in range(l):
        result+=lis3[i] * (i+1) * (l-i)
    return result    

if __name__=="__main__":
    lis3=[1,2,3,4]
    print(sum_all_subarray(lis3))            
            

'''FOURTH PROBLEM : Given an array prices[] representing stock prices, find the maximum total profit that can be earned by buying and selling the stock any number of times.

Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.'''

def stock_buy_sell(lis4):
    l=len(lis4)
    profit=0
    for i in range(1,l):
        if lis4[i]>lis4[i-1]:
            profit+=lis4[i]-lis4[i-1]
    return profit    
    
if __name__=="__main__":
    lis4=[100,180,260,310,40,535,695]
    print(stock_buy_sell(lis4))   


''' FIFTH PROBLEM : Given an array of integers, every element in the array appears twice except for one element which appears only once. The task is to identify and return the element that occurs only once.'''
def unique_num(lis5):
    lis5i={}
    for i in lis5:
        lis5i[i]=lis5i.get(i,0)+1
    for key,value in lis5i.items():
        if value==1:
            return key
    return None            
    
    
if __name__=="__main__":
    lis5=[1,2,3,3,4,4,5,5]
    print(unique_num(lis5))       



''' SIXTH PROBLEM : Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.'''
def find_missing(lis6):
    l=len(lis6)+1
    h=[0]*(l+1)
    for i in range(l-1):
        h[lis6[i]]+=1
    for i in range(1,l):
        if h[i]==0:
            return i    
if __name__=="__main__":
    lis6=[1,3,4]
    print(find_missing(lis6))    


'''SEVENTH PROBLE : Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.'''
def missing_duplitcate(lis7):
    l=len(lis7)+1
    missing=0
    dupli=0
    h=[0]*(l+1)
    for i in range(l-1):
        h[lis7[i]]+=1
    for i in range(1,l):
        if h[i]==0:
            missing=i
        elif h[i]==2:
            dupli=i
    
def m_d(lis7):
        dic={}
        for i in range(1,len(lis7)+1):
            dic[i]=lis7.count(i)
        miss=0
        dup=0
        for j,k in dic.items():
          if k==0:
            miss=j
          elif k==2:
            dup=j
        return [dup,miss]
         
if __name__=="__main__":
    lis6i=[1,4,5,6,3,3]
    print(m_d(lis6i))       
        

''' EIGHT PROBLEM : Given an array arr[] of size n filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. The task is to find the repetitive element.'''
def repeating_find(lis8):
    for i in range(len(lis8)):
        if lis8[abs(lis8[i])] < 0:
            return abs(lis8[i])
        lis8[abs(lis8[i])] = -lis8[abs(lis8[i])]
    return -1
if __name__== "__main__":
    lis8=[1,3,2,3,4]
    print(repeating_find(lis8))    


''' NINETH PROBLEM : Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time. If there are multiple such triplets, then print any one of them.'''
def sorted_subsec(lis9):
    n=len(lis9)
    mini=[0]*n
    maxi=[0]*n
    mini[0]=lis9[0]
    maxi[-1]=lis9[-1]    
    for i in range(1,n):
        mini[i]=min(mini[i-1],lis9[i])
        maxi[n-1-i]=max(maxi[-i],lis9[n-1-i])   
    for i in range(n):
        if lis9[i]>mini[i] and lis9[i]<maxi[i]:
            return mini[i],lis9[i],maxi[i]
if __name__=="__main__":
    lis9=[1,2,3,4,6]        
    print(sorted_subsec(lis9))


''' TENTH PROBLEM : Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
Note: A subarray is a continuous part of an array.'''
def maximum_sum(lis10):
    max_sum=lis10[0]
    summ=0
    for i in range(len(lis10)):
        summ+=lis10[i]
        max_sum=max(max_sum,summ)
        if summ < 0:
            summ=0
    return max_sum
if __name__=="__main__":
    lis10=[-2,-4]
    print(maximum_sum(lis10))        
             