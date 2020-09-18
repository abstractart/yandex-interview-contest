from queue import Queue

# distance between cities
def s(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def main():
    # Read data
    n = int(input())
    coord = []
    for i in range(n):
        row = input().split()
        coord.append([int(row[0]), int(row[1])])

    k = int(input())

    row = input().split()
    (departure, arrival) = (int(row[0]) - 1, int(row[1]) - 1)

    # Breadth first search using queue
    q = Queue()
    q.put((departure, 0))
    visited = dict()
    visited[departure] = True

    while(q.qsize() > 0):
        curr_city, curr_city_roads = q.get()
        if curr_city == arrival: return curr_city_roads
		
        for city in range(n):
            if s(coord[city], coord[curr_city]) <= k and not visited.get(city):
                q.put((city, curr_city_roads + 1))
                visited[city] = True

        


    return -1

print(main())
