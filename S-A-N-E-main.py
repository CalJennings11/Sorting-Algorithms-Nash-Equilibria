import random
import time

def merge_sort(arr):
    # Implement the Merge Sort algorithm
    if len (arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def selection_sort(arr):
    # Implement the Selection Sort algorithm
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    # Implement the Bubble Sort algorithm
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def play_game(player1_choice, player2_choice, arr, sorting_algorithms):
    # Record start time for player 1
    start_time_player1 = time.time()
    player1_algorithm = sorting_algorithms.get(player1_choice, 'Quick Sort')
    if player1_algorithm == 'Merge Sort':
        sorted_arr_player1 = merge_sort(arr)
    elif player1_algorithm == 'Selection Sort':
        sorted_arr_player1 = selection_sort(arr)
    elif player1_algorithm == 'Bubble Sort':
        sorted_arr_player1 = bubble_sort(arr)

    end_time_player1 = time.time()

    # Record start time for player 2
    start_time_player2 = time.time()
    player2_algorithm = sorting_algorithms.get(player2_choice, 'Quick Sort')
    if player2_algorithm == 'Merge Sort':
        sorted_arr_player2 = merge_sort(arr)
    elif player2_algorithm == 'Selection Sort':
        sorted_arr_player2 = selection_sort(arr)
    elif player2_algorithm == 'Bubble Sort':
        sorted_arr_player2 = bubble_sort(arr)

    end_time_player2 = time.time()

    # Calculate the execution times for both players
    player1_time = end_time_player1 - start_time_player1
    player2_time = end_time_player2 - start_time_player2

    return player1_time, player2_time

def find_nash_equilibrium(num_elements, sorting_algorithms, player_choices, num_rounds):
    nash_equilibria = []
    lowest_total_time = float('inf')

    for round in range(num_rounds):
        choice1 = random.choice(player_choices)
        choice2 = random.choice(player_choices)

        # Generate a list with random elements
        arr = [random.randint(1, 100) for _ in range(num_elements)]
        player1_time, player2_time = play_game(choice1, choice2, arr, sorting_algorithms)

        # Print the results for each round
        print(f"Round {round + 1}: Player 1 ({choice1}): {player1_time:.6f} seconds, Player 2 ({choice2}): {player2_time:.6f} seconds")

        total_time = player1_time + player2_time

        # Check for Nash Equilibrium conditions
        if total_time < lowest_total_time:
            nash_equilibria = [(choice1, choice2)]
            lowest_total_time = total_time
        elif total_time == lowest_total_time:
            nash_equilibria.append((choice1, choice2))

    if not nash_equilibria:
        print("No Nash Equilibria found.")
    else:
        print("\nNash Equilibria:")
        for eq in nash_equilibria:
            print(f"Player 1: {eq[0]}, Player 2: {eq[1]}")

    return nash_equilibria

if __name__ == "__main__":
    sorting_algorithms = {
        'Merge Sort': 'Merge Sort',
        'Selection Sort': 'Selection Sort',
        'Bubble Sort': 'Bubble Sort',  # Add more sorting algorithms as needed
    }
    player_choices = list(sorting_algorithms.keys())

    num_elements = int(input("Enter the number of elements in the list to be sorted: "))
    num_rounds = int(input("Enter the number of rounds: "))

    nash_equilibria = find_nash_equilibrium(num_elements, sorting_algorithms, player_choices, num_rounds)

    print("\nNash Equilibria:")
    for eq in nash_equilibria:
        print(f"Player 1: {eq[0]}, Player 2: {eq[1]}")