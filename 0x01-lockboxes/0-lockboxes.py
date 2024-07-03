#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists, where each inner list represents the keys
        in a particular box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is already unlocked

    stack = [0]  # Start with the first box
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
