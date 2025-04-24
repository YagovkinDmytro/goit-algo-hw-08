import heapq

def heap_min_costs(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        print(f"Combine {first} + {second} = {cost}, total costs: {total_cost}")

        heapq.heappush(cables, cost)
        print(cables)

length_cabels = [4, 7, 12, 32, 16, 70, 24]

heap_min_costs(length_cabels)