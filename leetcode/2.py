class Solution:
    def reverse(self, x: int) -> int:
        reverse = ''
        num = x
        if num < 0:
            neg = True
            num = -1 * (num)
            num = str(num)
            for i in range (len(num),0,-1):
                reverse += num[i-1]
            final = (-1 * int(reverse))
        else:
            num = str(num)
            for i in range (len(num),0,-1):
                reverse += num[i-1]
            final = (int(reverse))
        if(final in range((-2**31),((2**31)-1))):
            return final
        else:
            return 0