# class 베이스 스택 구현
    # stack이 비어 있는지 확인 하는 메서드
    # 생성자에 담을 건데
    # stack 이라는 자료형은 최대 크기가 지정
    def __init__(self, size):
        self.top = -1
        # stack의 크기
        # stack에 자료를 저장할 구조
        # stack에 최상단
    # stack이 비어 있는지 확인 하는 메서드
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    # stack이 가득 찼는지 확인하는 메서드
    def is_empty(self):
        if self.top == self.size:
            return True
        else:
            return False
    # stack에 값을 추가 하는 연산
    def push(self):
        self.top = 1
        #self.arr[self.top] = item
    # stack에 값을 제거 하는 연산



a = Stack(3)
