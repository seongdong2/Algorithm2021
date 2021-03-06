#1초 = 1,000,000,000 (10억)

#DFS, O(N)
def dfs(gragh, start, visited):
    visited[start] = True
    for v in gragh[start] :
        #여기서 뭔가를 더 할 수 있음
        if not visited[v] :
            dfs(gragh, v, visited)


#BFS, O(N)
#DFS보다 빠른 탐색
from collections import deque
def bfs(gragh, start, visited):
    queue = deque([start])
    visited[start]= True
    while queue:
        v = queue.popleft()
        #여기서 뭔가를 더 할 수 있음
        for i in gragh[v]:
            if not visited[i] :
                queue.append(i)
                visited[i] = True



#선택정렬, O(N**2)
array = []
for i in range(len(array)) :
    min_index = i
    for j in range(1, i+1) :
        if array[min_index] > array[j] :
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]




#삽입정렬, O(N**2)
for i in range(1, len(array)):
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break




#퀵 정렬, O(NlogN) 
def quick(array):
    if len(array) <= 1 :
        return array
    pivot = array[0] #피벗은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 리스트
    left_side = [l for l in tail if l <=pivot]
    right_side = [r for r in tail if r > pivot]
    
    return q(left_side) + [pivot] +q(right_side)



#계수정렬, O(N+K)
def count(array):
    count = [0]*(max(array) + 1)
    #데이터를 인덱스로 저장하기
    for i in range(len(array)):
        count[array[i]] += 1
    
    #리스트 정보확인하기
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end='')


#key
array = [('바나나',2), ('사과', 5), ('당근', 3)]
def setting(data):
    return data[1]
result = sorted(array, key=setting)


#hash
def hash(participant, completion):
    dict={}
    for name in participant :
        if dict.get(name):
            dict[name] +=1
        else:
            dict[name] =1
    
    for name in completion:
        dict[name] -= 1
    
    for key in dict :
        if dict[key] > 0 :
            return key
    

#이진탐색, O(N)
def bi(array, target, start, end):
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return mid
        
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return None



#min_heapfy 정렬, O(NlogN)
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h=[]
    result = []
    #모든 원소를 차레대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result



#다이나믹프로그래밍 탑다운, O(N)
d = [0]*100
def DP(x):
    if x ==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = DP [x -1] + DP[x-2]
    return d[x]


#DP 보텀업, O(N)
def DP2(n):
    d=[0]*100
    d[1] = 1
    d[2] = 1

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    
    return d[n]


#아라토스테네스의 채
import math
def aratos(n):
    array = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True :
            j=2
            while i*j <=n:
                array[i*j]=False
                j += 1
    
    for i in range(2, n+1):
        if array[i]:
            print(i, end =' ')

