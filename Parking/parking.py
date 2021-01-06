def main():

    numCases = int(input())
    for num in range(numCases):
        # This is a meaning less line but for Kattis input....
        numShops = input()

        shopLocations = [int(x) for x in input().split(' ')]

        # Sort from the closest to the furthest
        sortedLocations = sorted(shopLocations)

        # Add up distances between all shops
        walkDistance = 0
        for i in range(len(sortedLocations)-1):
            walkDistance += sortedLocations[i+1]-sortedLocations[i]

        # Add furthes shor to car distance
        walkDistance += sortedLocations[-1] - sortedLocations[0]

        print(walkDistance)


if __name__ == "__main__":
    main()
