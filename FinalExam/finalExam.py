def main():
    score = 0
    tempAns = 'Z'

    numQuestions = int(input())

    for _ in range(numQuestions):
        ans = input()
        if tempAns == ans:
            score += 1
        tempAns = ans

    print(score)


if __name__ == '__main__':
    main()
