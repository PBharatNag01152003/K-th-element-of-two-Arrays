#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        self.k=k
        self.arr1=arr1
        self.arr2=arr2
        m=arr1+arr2
        m.sort()
        return m[k-1]
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
