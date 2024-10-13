#!/usr/bin/python3
"""Solves the lock boxes puzzle."""

def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    for key in keys:
        for k in boxes[key]:
            if k < n and not opened[k]:
                opened[k] = True
                keys.append(k)

    return all(opened)
