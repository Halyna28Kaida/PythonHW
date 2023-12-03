# 1

while True:
    try:
        sum_of_money = int(input("Please, enter the sum of money you want to get, UAH: "))
    except ValueError:
        print("It isn't a number.")
    else:
        if sum_of_money <= 0:
            print("Your sum must be larger then 0.")
        elif sum_of_money > 380:
            print("I am very sorry. I don't have enough bills for you.")
        else:
            bills = []
            summ = 0
            bill = [1, 2, 5, 10, 20]
            sum_bills = 0

            while summ < sum_of_money:
                i = 0
                for i in bill:
                    while sum_bills < 10 and summ < sum_of_money:
                        bills.append(i)
                        summ += i
                        sum_bills += 1
                    sum_bills = 0
            while summ > sum_of_money:
                difference = summ - sum_of_money
                if difference in bill:
                    for el in bills:
                        if difference == el:
                            bills.remove(difference)
                            summ -= difference
                            difference = 0
                    break
                else:
                    for k in bill:
                        if difference < k:
                            index_k = bill.index(k)
                            bill_val = bill[index_k-1]
                            bills.remove(bill_val)
                            difference -= bill_val
                            summ -= bill_val
                            break
            break
print("I'm very sorry but I have only small bills. I can give you:")

for j in bill:
    if j in bills:
        amount = bills.count(j)
        print(f"{amount} bills of {j} UAH")
print(f"The sum of bills is: {summ}")

while True:
    answer = input("Is it OK (yes/no): ").strip().lower()
    if answer == "yes":
        print("You can get it. Thank you.")
        break
    elif answer == "no":
        print("So sorry. Have a nice day.")
        break
    else:
        print("Incorrect answer. Try again.")




