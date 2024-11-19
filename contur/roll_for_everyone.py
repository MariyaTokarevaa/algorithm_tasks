def main():
    friends_rolls = input().split()
    N = int(friends_rolls[0])
    T = int(friends_rolls[1])

    min_roll = sum(map(int, input().split()))
    max_roll = sum(map(int, input().split()))
    if min_roll <= T <= max_roll:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()