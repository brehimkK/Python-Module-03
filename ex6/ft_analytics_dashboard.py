#!/usr/bin/env python3


def return_values() -> tuple:
    print("=== List Comprehension Examples ===")

    players = ["alice", "bob", "charlie"]
    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
        }
    high_score = [name for name, score in scores.items() if score > 2000]
    doubled_scores = [score*2 for score in scores.values()]
    return high_score, doubled_scores, players


def Dict_Comprehension_Examples() -> tuple:
    print("\n=== Dict Comprehension Examples ===")
    players_scors = {'alice': 2300, 'bob': 1800, 'charlie': 2150}
    Score_cat = {'high': 0, 'meduim': 0, 'low': 0}
    print(f" Player scores {players_scors}")
    for score in players_scors.values():
        if score >= 1800:
            Score_cat["high"] += 1
        if score >= 2150:
            Score_cat["meduim"] += 1
        if score >= 2300:
            Score_cat["low"] += 1
    print(f"Score categories: {Score_cat}")
    Achievemen = {'alice': 5, 'bob': 3, 'charlie': 7}
    print(f"Achievement counts: {Achievemen}")
    return Achievemen, players_scors


def Comprehension() -> None:
    print("\n=== Set Comprehension Examples ===")
    players = {'alice', 'bob', 'charlie', 'diana'}
    print(f"Unique players: {players}")
    achievement = {'first_kill', 'level_10', 'boss_slayer'}
    print(f"Unique achievements: {achievement}")
    Active_regions = {'north', 'east', 'central'}
    print(f"Active regions: {Active_regions}")
    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")


def main() -> None:
    high_scores, double_scores, players = return_values()
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {double_scores}")
    print(f"Active players: {players}")
    t_acheivement, av_score = Dict_Comprehension_Examples()
    Comprehension()
    total = 0
    for score in t_acheivement.values():
        total += score
    print(f"Total unique achievements: {total}")
    total_av_score = 0
    for score in av_score.values():
        total_av_score += score
    print(f"Average score: {total_av_score / len(av_score):.1f}")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    main()
