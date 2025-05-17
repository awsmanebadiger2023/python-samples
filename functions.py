def calculate_interest(p,r,t):
    si = (p*r*t)/100
    return si


print('Calling calculate_interest on P, R  & T',2000,5,4)
interest = calculate_interest(2000, 5, 4) ### ANS 400
print('Interest is::::', interest)


def square(val):
    return val*val
def add(val1,val2):
    return val1+val2
p = add(square(4),24)
print(p)


print('Boolean return usage##############################')
def is_dividable(a, b):
    if a%b==0:
        return True
    else:
        return False
print(is_dividable(5, 2))
if is_dividable(100, 2):
    print('we can divided 100 by 2')