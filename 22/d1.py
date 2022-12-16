import io
from typing import List


def find_max_calories(elves: List[List[int]]) -> int:
    return max(
        map(
            lambda x: sum(x),
            elves,
        ),
    )

def find_max_calories_topn(elves: List[List[int]], nmax: int) -> List[int]:
    results = sorted(
        map(
            lambda x: sum(x),
            elves,
        ),
    )
    return sum(
        results[-nmax:],
    )

def parse_calories_file() -> List[List[int]]:

    calories: List[List[int]] = []
    calories_elf: List[int] = []

    with io.open("d1.txt") as fcalories:
        
        while True:

            line = fcalories.readline()
            if not line:
                break

            line = line.strip()
            if not line:
                calories += [
                    calories_elf,
                ]
                calories_elf = []
                continue

            calories_elf += [
                int(line),
            ]

    return calories

calories = parse_calories_file()
print(
    find_max_calories(calories),
    find_max_calories_topn(calories, 3),
)