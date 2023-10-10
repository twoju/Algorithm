while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        print('error')
        break