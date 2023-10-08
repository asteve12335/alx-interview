#!/usr/bin/python3
"LockBoxes interview question"


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    # Check if the input list is None or empty.
    if boxes is None or len(boxes) == 0:
        return False

    # Create a list of keys, starting with the key to the first box.
    keys = [0]

    # Iterate over the list of keys, opening each box in turn.
    for key in keys:
        # Open the box with the current key.
        box = boxes[key]

        # Check if the key to the current box is already in the list of keys.
        if box not in keys:
            # If it is not, then add it to the list of keys.
            keys.append(box)

    # If the function was able to open all the boxes, then return True.
    if len(keys) == len(boxes):
        return True

    # Otherwise, return False.
    else:
        return False
