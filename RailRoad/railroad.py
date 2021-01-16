def main():
    X, Y = [int(x) for x in input().split()]

    if (Y*3 + X*2) % 2 == 0:
        print('possible')
    else:
        print('impossible')


if __name__ == '__main__':
    main()
