POSSIBLE_BILLS = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
AMOUNT_OF_BILLS = 10
using_bills = []
result = dict.fromkeys(POSSIBLE_BILLS, 0)
while True:
    try:
        amount = int(input("Please, enter the sum of money you want to get, UAH: "))
    except ValueError:
        print("It isn't a number.")
    else:
        for i in range(len(POSSIBLE_BILLS)):
            if sum(POSSIBLE_BILLS[:i+1]) * AMOUNT_OF_BILLS > amount:
                using_bills = POSSIBLE_BILLS[:i+1]
                break
        if using_bills:
            while amount:
                current_bill = using_bills[-1]
                amount -= current_bill
                result[current_bill] += 1
                if sum(using_bills[:-1]) * AMOUNT_OF_BILLS > amount:
                    using_bills.remove(current_bill)
            print(result)
            break
        else:
            print("Sorry we don't have needed amount")

