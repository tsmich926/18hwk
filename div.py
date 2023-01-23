#약수출력하기 예제
N= int(input())
while N<1 or N>1000:
    print("다시 입력")
    N= int(input())
for i in range(1,N+1):
    if N%i==0:
        print(i)