def main():
    totalVolume = 0
    thickness = 4

    # Take Inputs
    cakeWidth, hCut, vCut = [int(x) for x in input().split(' ')]
    width = hCut
    height = vCut

    if hCut < (cakeWidth/2):
        width = cakeWidth - hCut

    if vCut < (cakeWidth/2):
        height = cakeWidth - vCut

    totalVolume = thickness * height * width
    print(totalVolume)


if __name__ == "__main__":
    main()
