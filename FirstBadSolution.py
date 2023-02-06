"""
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
def isBadVersion(n):
    if n<=3:
        return False
    if n>3:
        return True


def firstBadVersion(n: int) -> int:
    left, right = 0, n
    while True:
        mid = (left + right) // 2
        if isBadVersion(mid) == False and isBadVersion(mid + 1):
            return mid + 1
        elif isBadVersion(mid) and isBadVersion(mid + 1):
            right = mid - 1
        elif isBadVersion(mid)==False and isBadVersion(mid+1)==False:
            left = mid + 1
        else:
            return mid+1
print(firstBadVersion(5))