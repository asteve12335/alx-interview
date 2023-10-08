#!/usr/bin/python3
"""LockBoxes interview question"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    if boxes is None:
        return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys:
                if box < len(boxes):
                    keys.append(box)
    if len(keys) == len(boxes):
        return True
    else:
        return False
