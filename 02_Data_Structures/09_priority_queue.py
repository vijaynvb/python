import heapq

patients = []

heapq.heappush(patients, (1, "Critical Patient"))
heapq.heappush(patients, (2, "Serious Patient"))
heapq.heappush(patients, (3, "Normal Patient"))

print("Patient Being Treated:")

while patients:
    print(heapq.heappop(patients)[1])
 
