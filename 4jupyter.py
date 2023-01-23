##map함수를 사용해 세제곱함수를 각각 요소에 넣어줌
def cube(n):
    return n ** 3
numbers = [1, 2, 3]
new_numbers = list(map(cube, numbers))
print(new_numbers)

""""""""""""""""""""
##두 정수를 입력받아 더한값 출력
x,y=list(map(int,input().split()))

#두수를 더해주는 함수
def plus(x,y):
    return x+y

s=plus(x,y)
print(s)