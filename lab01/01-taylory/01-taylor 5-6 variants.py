import math

def taylor_ln_1_plus_x(x : float, epselon : float) -> float:
    #ln(1+x) = x - x^2/2 + x^3/3 для x in (-1, 1]
    if not (-1 < x <= 1):
            raise ValueError("ряд сходится только при x в интервале (-1, 1]")
    term = x
    mnogochlen = term
    n = 1
    while abs(term) >= epselon:
        n += 1
        term = ((-1)**(n-1)) * (x**n) / n
        mnogochlen += term
    return mnogochlen

def taylor_ln_div(x : float, epselon : float) -> float:
    # ln((1+x)/(1-x)) = 2 * (x + x^3/3 + x^5/5 + ...) для x in (-1, 1)
    if not (-1 < x < 1):
        raise ValueError("ряд сходится только при x в интервале (-1, 1)")

    term = x
    mnogochlen = term
    k = 0
    x_squared = x * x
    
    while abs(term) >= epselon:
        k += 1
        term = term * x_squared * (2 * k - 1) / (2 * k + 1)
        mnogochlen += term
        
    return 2 * mnogochlen


def main():
    print("lab 1")
    try:
        try:
            k = int(input("input natural number k (k > 1): "))
            if k <= 1:
                raise ValueError("k > 1!!!")
        except ValueError as e:
            print(f"{e}")
            return
        
        epselon = 10**(-k)
        x = float(input("input x: "))

        print(f"\nepselon = {epselon}")

        ln = taylor_ln_1_plus_x(x, epselon)
        print(f"ln(1+{x}): {ln:.8f} | math.log(1+{x}): {math.log(1+x):.8f}")
        ln_ = taylor_ln_div(x, epselon)
        print(f"ln((1+{x})/(1-{x})): {ln_:.8f} | math.log((1+{x})/(1-{x})): {math.log((1+x)/(1-x)):.8f}")

    except ValueError as e:
            print(f"bad input: {e}")
   
if __name__ == "__main__":
    main()
