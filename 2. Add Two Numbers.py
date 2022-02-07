# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

l1 = [0]
l2 = [0]


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = ListNode(0)
        nl1 = []
        nl2 = []
        nl1.append(l1.val)  # the first element in l1
        nl2.append(l2.val)  # the first element in l2

        while l1.next != None:
            tl1 = l1.next #pointer to nexr
            nl1.append(l1.val)
        while l2.next != None:
            l2 = l2.next
            nl2.append(l2.val)

        nl1.reverse()
        nl2.reverse()
        l1length = len(nl1)
        l2length = len(nl2)
        nl1, nl2 = makeEqual(nl1, nl2, l1length, l2length)
        length = max(l1length, l2length)

        for i in range(0, length):
            if (nl1[i]+nl2[i]) >= 10:
                if (i == length-1):
                    answer.val =1
                    answer= answer.next
                else:
                    nl1[i+1] = nl1[i+1]+1
                    answer.val=nl1[i]+nl2[i]-10
                    answer= answer.next
            else:
                answer.val= nl1[i]+nl2[i]
                answer= answer.next
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

# TypeError: 'ListNode' object is not iterable
# list(l1).reverse()
# Line 10 in addTwoNumbers(Solution.py)
# ret = Solution().addTwoNumbers(param_1, param_2)
# Line 60 in _driver(Solution.py)
# _driver()
# Line 71 in <module > (Solution.py)
