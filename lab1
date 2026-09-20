import math

def taylor_exp(x : float, epselon : float) -> float:
    #e^x = 1 + x/1! + x^2/2!
    term = 1.0
    mnogochlen = term
    n = 1
    while abs(term) >= epselon:
        term *= x / n
        mnogochlen += term
        n += 1
    return mnogochlen

def taylor_exp_neg(x : float, epselon : float) -> float:
    #e^-x = 1 - x/1! + x^2/2!
    term = 1.0
    mnogochlen = term
    n = 1
    while abs(term) >= epselon:
        term *= -x / n
        mnogochlen += term
        n += 1
    return mnogochlen

def taylor_cos(x : float, epselon : float) -> float:
    #cos(x) = 1 - x^2/2! + x^4/4!
    term = 1.0
    mnogochlen = term
    n = 1
    while abs(term) >= epselon:
        term *= -x**2 / ((2*n - 1) * (2*n))
        mnogochlen += term
        n += 1
    return mnogochlen

def taylor_ln_1_plus_x(x : float, epselon : float) -> float:
    #ln(1+x) = x - x^2/2 + x^3/3 для x in (-1, 1]
    term = x
    mnogochlen = term
    n = 1
    while abs(term) >= epselon:
        n += 1
        term = ((-1)**(n-1)) * (x**n) / n
        mnogochlen += term
    return mnogochlen

def taylor_sin(x : float, epselon : float) -> float:
    #sin(x) = x - x^3/3! + x^5/5!
    term = x
    mnogochlen = term
    n = 1
    while abs(term) >= epselon:
        term *= -x**2 / ((2*n) * (2*n + 1))
        mnogochlen += term
        n += 1
    return mnogochlen

def main():
    print("лаб 1")
   #try:
    k = int(input("введите натур число k (k > 1): "))
    if k <= 1:
        print("k > 1")
        return
    epselon = 10**(-k)
    x = float(input("введите x: "))

    print(f"\nepselon = {epselon}")
    
    exp = taylor_exp(x, epselon)
    print(f"e^{x}:  {exp:.8f} | math.exp({x}):  {math.exp(x):.8f}")

    cos = taylor_cos(x, epselon)
    print(f"cos({x}): {cos:.8f} | math.cos({x}): {math.cos(x):.8f}")

    sin = taylor_sin(x, epselon)
    print(f"sin({x}): {sin:.8f} | math.sin({x}): {math.sin(x):.8f}")

    if -1 < x <= 1:
        ln = taylor_ln_1_plus_x(x, epselon)
        print(f"ln(1+{x}): {ln:.8f} | math.log(1+{x}): {math.log(1+x):.8f}")
   
main()