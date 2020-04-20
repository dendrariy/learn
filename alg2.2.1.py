def fib(n):
    if n <= 1:
        return 1
    else:
        res = [0]*(n + 1)
        res[0] = 0
        res[1] = 1
        for i in range(2, n + 1):
            res[i] = res[i-1] + res[i-2]
        return(res[i])        

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
