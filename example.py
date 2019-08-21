from collections import deque
graph = {'you': ['alice', 'jack', 'mike'], 'alice': [
    'peggy'], 'jack': ['peggy'], 'peggy': [], 'mike': ['mangom']}


def find(graph):
    queue = deque()
    queue += graph['you']
    count = 0
    while len(queue):
        count += 1
        person = queue.popleft()
        if queue[0][-1] == 'm':
            return 'FInd mangom'+str(count)
        else:
            print(queue)
            queue += graph[person]
    return None


find(graph)
# def qsort(list):
#     if len(list) < 2:
#         return list
#     pivot = list[0]
#     less = [x for x in list if x < pivot]
#     more = [x for x in list if x > pivot]
#     return qsort(less) + [pivot] + qsort(more)


# print(qsort(list))
