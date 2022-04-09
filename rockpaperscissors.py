import random

gestures: list = ["paper", "lizard", "scissors", "rock", "spock"]

def random_gesture() -> str:
	return random.choice(gestures)

def bound(index) -> int:
	return index % len(gestures)

def get_losers(gesture) -> list:
	index: int = gestures.index(gesture)
	return [gestures[bound(index - 1)], gestures[bound(index - 2)]]

def get_winners(gesture) -> list:
	index: int = gestures.index(gesture)
	return [gestures[bound(index + 1)], gestures[bound(index + 2)]]

if __name__ == "__main__":
	while True:
		rival_gesture: str = random_gesture()

		print("Write your selection (rock / paper / scissors / lizard / spock)")
		player_gesture: str = input()

		player_gesture_index: int = gestures.index(player_gesture)
		rival_gesture_index: int = gestures.index(rival_gesture)

		print("Rival chose: ", rival_gesture)

		if rival_gesture in get_losers(player_gesture):
			print("You win!")
		elif rival_gesture in get_winners(player_gesture):
			print("You lose!")
		else:
			print("Draw!")
	