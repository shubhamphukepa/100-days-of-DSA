'''FIRST PROBLEM : Given an array arr[], the task is to print every alternate element of the array starting from the first element.'''
def Alternate_element(lis):
    #first of all iterate array element using loop.
    for i in range(0,len(lis),2): 
    #Accessing Alternate element.
       print(lis[i],end=" ")
if __name__=="__main__":
    lis=[100,200,300,400,700,900]
    s1=Alternate_element(lis)



'''SECOND PROBLEM : Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.'''
def leaders(lis1):           
    l=len(lis1)
    final=[]
    for i in range(l):
        for j in range(i+1,l):
            if lis1[i]<lis1[j]:
                break
        else:
            
            final.append(lis1[i])
    return final
if __name__=="__main__":
    lis1=[1,2,3,4,5,2]
    s1=leaders(lis1)
    print(s1)



'''THIRD PROBLEM : Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.'''
def check_sorted(lis3):
    l=len(lis3)
    for i in range(1,l):
            if (lis3[i-1]>lis3[i]):
                return False
    return True
if __name__=="__main__":
    lis3=[10,30,30,40,50]
    k1=check_sorted(lis3)
    print(k1)



'''FOURTH PROBLEM : Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.''' 
def Remove_dup(lis4):
    lis4i=set()
    k=0
    for i in range(len(lis4)):
        if lis4[i] not in lis4i:
           lis4i.add(lis4[i])
           lis4[k]=lis4[i]
           k+=1
    return k
if __name__=="__main__":            
    lis4=[1,2,2,2,3,3,4,4,5,5]
    j1=Remove_dup(lis4)
    for i in range(j1):
        print(lis4[i],end=' ')
    
    

''' FIFTH PROBLEM : Given an array arr[], the task is to generate all the possible subarrays of the given array.'''
def generate_all_subarray(lis5):
    for i in range(len(lis5)):
        lis5i=[]
        for j in range(i,len(lis5)):
            lis5i.append(lis5[j])
            print(lis5i)
if __name__=="__main__":            
    lis5=[1,2,3,4]
    generate_all_subarray(lis5)
    
    
    
''' SIXTH PROBLEM : Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.'''
def array_reverse(lis6):
    left=0
    right=len(lis6)-1
    while left<right:
        lis6[left],lis6[right]=lis6[right],lis6[left]
        right-=1
        left+=1
    return lis6
if __name__=="__main__":
    lis6=[1,4,3,2,6,5] 
    print(array_reverse(lis6))   
''' SEVENTH PROBLEM : Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
Output: {5, 6, 1, 2, 3, 4}
Explanation: After first right rotation, arr[] becomes {6, 1, 2, 3, 4, 5} and after the second rotation, arr[] becomes {5, 6, 1, 2, 3, 4}'''

def rotate_array(lis7,k):
       k%=len(lis7)
       lis7.reverse()
       lis7[:k]=reversed(lis7[:k])
       lis7[k:]=reversed(lis7[k:])
       return  lis7
if __name__=="__main__":
    lis7=[1,2,3,4,5,6]
    k=2
    print(rotate_array(lis7,k))                



''' EIGHT PROBLEM : Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.'''
def move_zeros(lis8):
    for i in range(1,len(lis8)):
        if lis8[i-1]==0:
            lis8[i-1],lis8[i]=lis8[i],lis8[i-1]
    return lis8
if __name__=="__main__":
    lis8=[1,2,0,3,7,0]  
    print(move_zeros(lis8))
    
'''NINETH PROBLEM : You are given an array of n-elements, you have to find the number of operations needed to make all elements of array equal. Where a single operation can increment an element by k. If it is not possible to make all elements equal print -1.'''
def minimum_inrease(lis9,k):
    l=len(lis9)
    max1=max(lis9)
    res=0
    for i in range(l):
        if (max1-lis9[i])%k!=0:
            return -1
        else:
            res+=(max1-lis9[i])/k
    return int(res)
if __name__=="__main__":
    lis9=[4,7,19,16]
    k=3
    print(minimum_inrease(lis9,k))            
'''TENTH PROBLEM : Given an array of n integers. We need to reduce size of array to one. We are allowed to select a pair of integers and remove the larger one of these two. This decreases the array size by 1. Cost of this operation is equal to value of smallest one. Find out minimum sum of costs of operations needed to convert the array into a single element.'''
