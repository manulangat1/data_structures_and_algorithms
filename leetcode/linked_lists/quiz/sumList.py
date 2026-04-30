from LinkedList import LinkedList


def sumList(num1, num2):
    # result = 0
    carry = 0
    n1 = num1.head
    n2 = num2.head
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.val
            n1 = n1.next
        if n2:
            result += n2.val
            n2 = n2.next

        ll.add(int(result % 10))
        carry = result % 10

    return ll


ll = LinkedList()
ll.generate(10, 5, 10)
ll2 = LinkedList()
ll2.generate(10, 5, 10)
print(ll, ll2)
print(sumList(ll, ll2))
