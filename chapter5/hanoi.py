# a에 있는 n개의 원판을 b를 이용해 c로 옮김
def move(n, a, b, c):
    if n > 0:
        move(n - 1, a, b, c)
        print("Move a disk from %s to %s" %(a, c))
        move(n - 1, b, a, c)

move(3, 'a', 'b', 'c')
