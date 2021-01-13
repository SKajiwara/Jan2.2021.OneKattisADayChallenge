def main():
    totalHits = 0

    atBats = int(input())
    hits = [int(x) for x in input().split(' ')]
    for hit in hits:
        if hit == -1:
            atBats += -1
        else:
            totalHits += hit

    print(totalHits/atBats)


if __name__ == '__main__':
    main()
