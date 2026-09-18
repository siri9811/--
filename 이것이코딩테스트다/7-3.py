# 떡볶이 떡 만들기
def solution(tteoks, M):
    
    answer = 0
        
    def slice_tteok(tteoks, M, start, end):
        nonlocal answer
        
        if start > end:
            return
        
        height = (start + end) // 2
        total = 0
        
        for tteok in tteoks:
            if tteok > height:
                total += tteok - height
                
        if total >= M:
            answer = height
            return slice_tteok(tteoks, M, height + 1, end)
        
        else:
            return slice_tteok(tteoks, M, start, height - 1)
        
    slice_tteok(tteoks, M, 0, max(tteoks))
    
    return answer

test_cases = [
    (
        [19, 15, 10, 17],
        6,
        15
    ),
    (
        [4, 42, 40, 26, 46, 12, 18],
        20,
        36
    ),
    (
        [10, 10, 10, 10],
        20,
        5
    ),
    (
        [1, 2, 3, 4, 100],
        10,
        90
    ),
    (
        [5, 8, 12, 15],
        10,
        8
    )
]


for i, (tteok, M, expected) in enumerate(test_cases, 1):

    result = solution(tteok, M)

    if result == expected:
        print(f"테스트 {i}: 통과 ✅")
    else:
        print(f"테스트 {i}: 실패 ❌")
        print(f"내 결과: {result}")
        print(f"정답: {expected}")
