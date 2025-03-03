class Student:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age
    
    def introduce(self):  # 메서드
        return f"안녕하세요, 저는 {self.name}이고, 나이는 {self.age}입니다."

# 객체 생성
student1 = Student("철수", 20)
student2 = Student("영희", 22)

# 메서드 호출
print(student1.introduce())  # 출력: 안녕하세요, 저는 철수이고, 나이는 20입니다.
print(student2.introduce())  # 출력: 안녕하세요, 저는 영희이고, 나이는 22입니다.