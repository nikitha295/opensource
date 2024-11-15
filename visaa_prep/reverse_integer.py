def reverse_integer(n):
    is_neg = n<0
    reversed_num = int(str(abs(n))[::-1])
    if is_neg:
        reversed_num = -reversed_num
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    return reversed_num
n=int(input())
print(reverse_integer(n))
