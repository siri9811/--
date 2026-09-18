# 부품찾기
def solution(parts, requests):
    answer = []
    parts.sort()
    def binary_s(parts,target,start,end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        
        if parts[mid] == target:
            return True
        
        elif parts[mid] > target:
            return binary_s(parts,target,start, mid - 1)
        else:
            return binary_s(parts,target,mid+1,end)
        
    for request in requests:
        if binary_s(parts,request,0,len(parts) - 1):
            answer.append(1)
        else:
            answer.append(0)
        
        
        
    # 여기에 작성
    
    return answer


# 테스트 케이스
test_cases = [
    (
        [10, 3, 7, 1, 15, 20, 8],
        [7, 10, 5, 20]
    ),
    (
        [50, 10, 30, 70, 90, 20, 40],
        [10, 90, 50, 5]
    ),
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 5, 10, 11, 0]
    ),
    (
        [13, 27, 42, 56, 71, 88, 99],
        [1, 27, 30, 56, 72, 88, 100]
    ),
    (
        [25, 3, 17, 42, 8, 31, 56, 12, 67, 90],
        [67, 3, 100, 12, 25, 1, 90, 42]
    )
]


for parts, requests in test_cases:
    print(solution(parts, requests))
