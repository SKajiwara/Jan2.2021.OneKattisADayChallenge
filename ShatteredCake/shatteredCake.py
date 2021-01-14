def main():
    W = int(input())
    N = int(input())
    area = 0
    for i in range(N):
        w, l = [int(x) for x in input().split()]
        area += w * l
    print(int(area/W))


if __name__ == '__main__':
    main()
