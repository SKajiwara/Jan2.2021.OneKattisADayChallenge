def readInput():
    line = input()
    return line


def splitBySemicolon(line):
    items = line.split(";")
    return items


def countProblem(item):
    if '-' in item:
        midPtn = item.find('-')
        lastNum = int(item[midPtn+1:])
        firstNum = int(item[:midPtn])
        return lastNum - firstNum + 1

    return 1


def main():
    answer = 0

    line = readInput()
    items = splitBySemicolon(line)

    for item in items:
        answer = answer + countProblem(item)

    print(answer)


if __name__ == "__main__":
    main()
