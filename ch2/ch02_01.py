# ch02 -01
#  객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
#  규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
#  클래스 중심 -> 데이터 중심 -> 객체로 관리

#  일반적인 코딩

#  차량 1
from collections import namedtuple

car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'white'},
    {'horsepower': 400},
    {'price': 8000},
]

#  차량 2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'black'},
    {'horsepower': 270},
    {'price': 5000},
]

#  차량 3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'silver'},
    {'horsepower': 300},
    {'price': 6000},
]

# 리스트 구조
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'white', 'horsepower': 400, 'price': 8000},
    {'color': 'black', 'horsepower': 270, 'price': 5000},
    {'color': 'silver', 'horsepower': 300, 'price': 6000}
]

# 네임드 튜플
Car = namedtuple('Car', 'company color horsepower price')
car_companies = [
    Car('Ferrari', 'white', 400, 8000),
    Car('Bmw', 'black', 270, 5000),
    Car('Audi', 'silver', 300, 6000),
]

# 딕셔너리 구조
# 코드 반복 지속, 중첩문제(키), 키 조회 예외 처리 등
car_di = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'white', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'silver', 'horsepower': 300, 'price': 6000}}
]


# 클래스 구조
# 구조 설계 후 재상용성 증가, 코드 반복 최소화, 메소드 활용

class Car(object):
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # print 문으로 출력
    def __str__(self):
        return f'<str> {self._company}: {self._details}'

    # 객체를 그대로 표시할 때
    def __repr__(self):
        return f'<repr> {self._company}: {self._details}'


car1 = Car('Ferrari', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'silver', 'horsepower': 300, 'price': 6000})
print(car1)  # <str> Ferrari: {'color': 'white', 'horsepower': 400, 'price': 8000}
print(car1.__dict__)  # {'_company': 'Ferrari', '_details': {'color': 'white', 'horsepower': 400, 'price': 8000}}
print(dir(car1))

car_list = [car1, car2, car3]
# [
# <repr> Ferrari: {'color': 'white', 'horsepower': 400, 'price': 8000},
# <repr> Bmw: {'color': 'black', 'horsepower': 270, 'price': 5000},
# <repr> Audi: {'color': 'silver', 'horsepower': 300, 'price': 6000}
# ]
print(car_list)

# 반복(__str__)
for x in car_list:
    print(x)  # <str> Ferrari: {'color': 'white', 'horsepower': 400, 'price': 8000}
