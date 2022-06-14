def conjec(x):
    while x > 1:
        print(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x+1


for x in range(100):
    print(f"NUMERO: ------ {x} -------")
    conjec(x)
    print("\n")
