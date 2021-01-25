def main():
    _ = int(input())
    nums = [int(x) for x in input().split(' ')]
    print(nums.index(min(nums)))


if __name__ == "__main__":
    main()
