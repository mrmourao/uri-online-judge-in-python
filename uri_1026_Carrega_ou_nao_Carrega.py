while True:
    try:
        v = input().split(" ")
        n1, n2 = v
        print(int(n1)^int(n2))
    except (EOFError):
        break