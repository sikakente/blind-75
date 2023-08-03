def solution(A):

    max_num = max(A)
    A = sorted(A)

    if max_num <= 0:
        return 1

    left = 0
    n = len(A)

    print(A)

    result = 1
    for i in range(n):
        if (i+1) != A[i]:
            return i+1
    
    return result
  
if __name__ == '__main__':
  tests = [
    [[1, 3, 6, 4, 1, 2], 5],
    [[1, 2, 3], 4]
  ]