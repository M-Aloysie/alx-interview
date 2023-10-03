def canUnlockAll(boxes):
    if not boxes:
        return True
    
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box (index 0)

    while stack:
        box_index = stack.pop()
        visited[box_index] = True

        for key in boxes[box_index]:
            if not visited[key]:
                stack.append(key)

    return all(visited)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
