#!/usr/bin/env python3
from typing import Generator
import time


def fibonacci_gen() -> Generator:
    a = 0
    b = 1
    while 1:
        yield a
        a, b = b, a + b


def prime_gen() -> Generator:
    a = 2
    while 1:
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            yield a
        a += 1


def event_generator(count: int) -> Generator:
    actions = ["killed monster", "found treasure", "leveled up"]
    players = ["alice", "bob", "charlie"]
    for i in range(1, count + 1):
        event = {
            "id": i,
            "player": players[i % len(players)],
            "level": (i * 7) % 12 + 5,
            "action": actions[i % len(actions)]
        }
        yield event


def main() -> None:
    gen = event_generator(1000)
    total_processed = 0
    high_level_players = 0
    treasures = 0
    level_ups = 0
    start_time = time.time()
    print("Processing 1000 game events...\n")
    for event in gen:
        total_processed += 1
        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasures += 1
        if event["action"] == "leveled up":
            level_ups += 1
        if event["id"] <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        elif event["id"] == 4:
            print("...")
    end_time = time.time()
    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_ups}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    fib = fibonacci_gen()
    fibbo_numbers = ""
    for i in range(10):
        if fibbo_numbers == "":
            fibbo_numbers = fibbo_numbers + str(next(fib))
        else:
            fibbo_numbers = fibbo_numbers + ", " + str(next(fib))
    print(f"Fibonacci sequence (first 1): {fibbo_numbers}")
    prime = prime_gen()
    prime_numb = ""
    for i in range(5):
        if prime_numb == "":
            prime_numb = prime_numb + str(next(prime))
        else:
            prime_numb = prime_numb + ", " + str(next(prime))
    print(f"Prime numbers (first 5): {prime_numb}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    main()
