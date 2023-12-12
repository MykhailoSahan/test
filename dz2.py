from typing import Optional


def exercise_3(array: list[int], positive: bool = True) -> Optional[int]:
    if not array:
        print("Empty element")
        return None

    for i, el in enumerate(array):
        if not isinstance(el, int):
            print("All elements must be an int")
            return None

        if positive:
            if el > 0:
                return i
        else:
            if el < 0:
                return i