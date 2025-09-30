
"""
Questions I would ask to help understand question:
1. Do we mean priority queue or just queue?
2. What happens for empty list?

Plan in plain English (pseudocode):
I will use a priority queue instead of a regular queue to save time. I will add the requests to the priority queue, and pop them off and add them to the result list in that order to get the result.

Begin problem:
"""
import heapq

def process_performance_requests(requests):
    pq = []
    
    # Push all requests into a max-heap (use negative priority for max-heap)
    for priority, performance in requests:
        heapq.heappush(pq, (-priority, performance))
    
    result = []
    while pq:
        _, performance = heapq.heappop(pq)
        result.append(performance)
    
    return result

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))