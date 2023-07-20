class Solution:
    def FindFibonacci(self,num):
        if num==0:
            return 0
        if num ==1:
            return 1
        return self.FindFibonacci(num-1)+self.FindFibonacci(num-2)
if __name__ == '__main__':
    num=int(input())
    print(Solution().FindFibonacci(num))