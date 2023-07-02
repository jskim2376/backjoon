maxCustomer = 0
customer = 0
for _ in range(10):
    outPeople, inPeople = map(int, input().split())
    customer = customer - outPeople + inPeople
    if maxCustomer < customer:
        maxCustomer = customer

print(maxCustomer)