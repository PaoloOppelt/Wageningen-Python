import math
def main():
    while True:
        ccn = input("Insert Credit Card Number: ")
        ccn = int(ccn)
        if ccn >= 0:
            break
    if check_validity(ccn):
        p_ccb(ccn)
    else:
        print("INVALID\n")


def check_validity(ccn):
    length = f_length(ccn)
    return (length == 13 or length == 15 or length == 16) and check_sum(ccn)


def f_length(n):
    length = 0
    while n != 0:
        length += 1
        # problem is here with unwanted decimals
        n /= 10
        n = math.trunc(n)
    print(length)
    return length


def check_sum(num):
    sum = 0
    i = 0
    while num != 0:
        if (i % 2 == 0):
            sum += num % 10
        else:
            d = 2 * (num % 10)
            sum += math.trunc(d / 10) + d % 10
        i += 1
        num /= 10
        num = math.trunc(num)
    return (sum % 10) == 0


def p_ccb(n):
    if (n >= 34e13 and n < 35e13) or (n >= 37e13 and n < 38e13):
        print("AMEX\n")
    elif n >= 51e14 and n < 56e14:
        print("MASTERCARD\n")
    elif (n >= 4e12 and n < 5e12) or (n >= 4e15 and n < 5e15):
        print("VISA\n")
    else:
        print("INVALID\n")


if __name__ == "__main__":
    main()
