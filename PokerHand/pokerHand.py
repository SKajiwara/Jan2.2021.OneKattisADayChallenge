def main():
    answer = 0
    numbers = [card[0] for card in input().split(' ')]

    for number in numbers:
        if numbers.count(number) > answer:
            answer = numbers.count(number)

    print(answer)


if __name__ == '__main__':
    main()
