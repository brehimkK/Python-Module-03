#!/usr/bin/env python3

def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter',
        'boss_slayer', 'speed_demon', 'perfectionist'
    }
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_achievements = alice.union(bob, charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}\n")
    
    rare_achievement = (
        alice.difference(bob, charlie).union(
            bob.difference(alice, charlie),
            charlie.difference(alice, bob)
        )
    )
    print(f"Rare achievements (1 player): {rare_achievement}\n")

    alice_vs_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_vs_bob}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()