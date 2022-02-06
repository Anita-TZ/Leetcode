# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

l1 = [0]
l2 = [0]


def addTwoNumbers(l1, l2):
    answer = []
    l1.reverse()
    l2.reverse()
    l1length = len(l1)
    l2length = len(l2)
    l1, l2 = makeEqual(l1, l2, l1length, l2length)
    length = max(l1length, l2length)

    for i in range(0, length):
        if (l1[i]+l2[i]) >= 10:
            if (i == length-1):
                answer.append(1)
            else:
                l1[i+1] = l1[i+1]+1
                answer.append(l1[i]+l2[i]-10)
        else:
            answer.append(l1[i]+l2[i])
    return answer


def makeEqual(l1, l2, l1length, l2length):
    if (l1length > l2length):
        for i in range(l2length, l1length):
            l2.append(0)
    if (l1length < l2length):
        for i in range(l1length, l2length):
            l1.append(0)
    return l1, l2


print((addTwoNumbers(l1, l2)))

#TypeError: 'ListNode' object is not iterable
#list(l1).reverse()
#Line 10 in addTwoNumbers(Solution.py)
#ret = Solution().addTwoNumbers(param_1, param_2)
#Line 60 in _driver(Solution.py)
#_driver()
#Line 71 in <module > (Solution.py)
