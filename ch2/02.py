class Car(object):
    """
    Car class
    Author: Lee
    Date: 2021.08.21
    """

    # 클래스 변수는 모든 인스턴스가 공유
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details
        Car.car_count += 1

    # print 문으로 출력
    def __str__(self):
        return f'<str> {self._company}: {self._details}'

    # 객체를 그대로 표시할 때
    def __repr__(self):
        return f'<repr> {self._company}: {self._details}'

    def detail_info(self):
        print(f'current ID: {id(self)}')
        print(f'car Detail info: {self._company} {self._details["price"]}')

    def __del__(self):
        Car.car_count -= 1


# self 의미
# 인스턴스
car1 = Car('Ferrari', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# DocString
print(car1.__doc__)

# 실행
print(id(car1))
print(car1.detail_info())

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))

# instance 를 직접 넣기
Car.detail_info(car1)

# 클래스 변수 확인
print(car1.car_count)
print(car2.car_count)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

# 삭제 메소드
del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))

