#!/usr/bin/env python3
import sys


def main():
    print("=== Player Score Analytics ===")

    if len(sys.argv) <= 1:
        print(f"No scores provided. Usage: python3 "
              f"{sys.argv[0]} <score1> <score2> ...")
        return

    scors = []
    total = 0

    try:
        for i in range(1, len(sys.argv)):
            num = int(sys.argv[i])
            scors.append(num)
            total += num
    except ValueError:
        print(f"oops, I typed '{sys.argv[i]}' instead of '1000'")
        return

    num_players = len(scors)

    print(f"Scores processed: {scors}")
    print(f"Total players: {num_players}")
    print(f"Total score: {total}")
    print(f"Average score: {total / num_players}")
    print(f"High score: {max(scors)}")
    print(f"Low score: {min(scors)}")
    print(f"Score range: {max(scors) - min(scors)}")


if __name__ == "__main__":
    main()
