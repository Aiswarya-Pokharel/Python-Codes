import heapq

patients = []

heapq.heappush(patients, (2, "Patient B"))
heapq.heappush(patients, (1, "Patient A"))
heapq.heappush(patients, (3, "Patient C"))

print("Next Patient:", heapq.heappop(patients))
