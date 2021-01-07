def readLine():
    return input()


def makeEs(greeting):
    return 'e' * (len(greeting) - 2)


def writeResponse(greeting, es):
    return greeting[:1] + es + greeting[1:]


def main():
    greeting = readLine()

    es = makeEs(greeting)

    response = writeResponse(greeting, es)

    print(response)


if __name__ == "__main__":
    main()
