from common import read_input

"""list(set(list1).intersection(list2))"""


def split_input(lines: str) -> list[dict[str, str]]:
    """Split every input line into a dictionary."""
    tickets = []
    for line in lines:
        winning_nums, your_nums = [part.strip() for part in line.split("|")]
        game = {
            "winning_nums": winning_nums.split(":")[1].strip(),
            "your_nums": your_nums,
        }
        tickets.append(game)
    return tickets


def get_values_as_numbers(game: dict[str, str]) -> tuple[list[int], list[int]]:
    """Get the winning numbers and your numbers as lists of integers."""
    winning_nums = game["winning_nums"].split(" ")
    your_nums = game["your_nums"].split(" ")

    cleaned_winning_nums = [item for item in winning_nums if item != ""]
    cleaned_your_nums = [item for item in your_nums if item != ""]

    return cleaned_winning_nums, cleaned_your_nums


def get_intersect_length(list1: list[int], list2: list[int]) -> int:
    """Get the length of the intersection of two lists."""
    return len(list(set(list1).intersection(list2)))


def initalize_counts(tickets: list[dict[str, str]]) -> dict[int, int]:
    """Initialize the original dictionary.

    At the beginning, we have 1 of every ticket.
    """
    return {i + 1: 1 for i in range(len(tickets))}


def solution_1(tickets: list[dict[str, str]]) -> int:
    """Calculate the total points for all tickets.

    Get the winning numbers and your numbers as lists of integers.
    Get the length of the intersection of the two lists.
    Use the given formula to calculate the points for each ticket.
    """
    points = 0
    for ticket in tickets:
        cleaned_winning_nums, cleaned_your_nums = get_values_as_numbers(ticket)
        intersect_length = get_intersect_length(cleaned_winning_nums, cleaned_your_nums)
        if intersect_length > 0:
            points += 1 * 2 ** (intersect_length - 1)
    return points


def solution_2(tickets: list[dict[str, str]]) -> int:
    """Calculate the total won tickets.

    Get the winning numbers and your numbers as lists of integers.
    Get the length of the intersection of the two lists.
    Add the value of the current ticket to the next N tickets value where N is the
    length of the intersect.
    """
    counts = initalize_counts(tickets)
    for index, ticket in enumerate(tickets):
        cleaned_winning_nums, cleaned_your_nums = get_values_as_numbers(ticket)
        intersect_length = get_intersect_length(cleaned_winning_nums, cleaned_your_nums)
        for i in range(1, intersect_length + 1):
            counts[index + 1 + i] += counts[index + 1]

    return sum(counts.values())


if __name__ == "__main__":
    path = "inputs/day4.txt"
    lines = read_input(path)
    tickets = split_input(lines)
    print(solution_2(tickets))
