def main():

    # Take All Inputs
    s, t, n = [int(x) for x in input().split()]
    walkTimes = [int(x) for x in input().split()]
    rideTimes = [int(x) for x in input().split()]
    intervalTimes = [int(x) for x in input().split()]

    # Set starting time as s
    totalTime = s

    for i in range(n):
        # 1. add walk time
        totalTime += walkTimes[1]

        # 2. Take Interval Time into account
        if totalTime < intervalTimes[i]:
            totalTime += intervalTimes[i] - totalTime
        else:
            totalTime += totalTime % intervalTimes[i]

        # 3. Add Ride Time
        totalTime += rideTimes[i]

    # Adjusting by adding final walk
    totalTime += walkTimes[-1]

    # Print Answer
    if totalTime > t:
        print('no')
    else:
        print('yes')


if __name__ == '__main__':
    main()
