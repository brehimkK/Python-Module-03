#!/usr/bin/env python3


def return_values ()-> list:
	print("=== Game Analytics Dashboard ===")
	
	players = ["alice", "bob", "charlie"]
	scores = {
		"alice": 2300,
		"bob": 1800,
		"charlie": 2150,
		"diana": 2050
		}
	high_score = [name for name, score in scores.items()if score > 2000]
	doubled_scores = [score**2 for score in scores.values()]
	return high_score , doubled_scores

def main ():
	high_scores, double_scores = return_values()
	print(f"High scorers (>2000): {high_scores}")

if __name__ == "__main__":
	main()