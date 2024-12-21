def solution(n, k):
    answer = 0
    free_drinks = n // 10
    paid_drinks = k - free_drinks
    answer = (n * 12000) + (paid_drinks * 2000)
    
    return answer