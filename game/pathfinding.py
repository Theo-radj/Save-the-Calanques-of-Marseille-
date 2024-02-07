import heapq
def is_valid(map, position):
    x, y = position
    if not (0 <= y < len(map) and 0 <= x < len(map[y])):
        return False
    if map[y][x] > 1:
        return False
    else:
        return True



def get_neighbors(map, current):
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if not ((dx == 0 or dy == 0) and dx != dy):
                continue
            position = x + dx, y + dy
            if is_valid(map, position):
                yield position


def get_shorter_paths(tentative, positions, through):
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path

def find_path(map,origin,destination):
    tentative = {origin: []}
    candidates = [(0, origin)]
    certain = set()
    while destination not in certain and len(candidates) > 0:
        _ignored, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(map, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    if destination in tentative:
        return tentative[destination] + [destination]
    else:
        return False






