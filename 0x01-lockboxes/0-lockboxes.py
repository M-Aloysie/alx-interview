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
