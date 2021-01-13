def main():
    num = int(input())
    nList = []
    for i in range(num):
        nList.append(int(input()))
    nList.reverse()

    for n in nList:
        print(n)


if __name__ == '__main__':
    main()
