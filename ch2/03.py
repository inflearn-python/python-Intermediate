class Car(object):
    """
    Car class
    Author: Lee
    Date: 2021.08.21
    Description: Class, static, Instance Method
    """

    # 클래스 변수는 모든 인스턴스가 공유
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    # print 문으로 출력
    def __str__(self):
        return f'<str> {self._company}: {self._details}'

    # 객체를 그대로 표시할 때
    def __repr__(self):
        return f'<repr> {self._company}: {self._details}'

    # Instance Method
    # self: 객체으 고유한 속성 값을 사용함.
    def detail_info(self):
        print(f'current ID: {id(self)}')
        print(f'car Detail info: {self._company} {self._details["price"]}')

    # Instance Method
    def get_price(self):
        return f'Before Car Price -> Company: {self._company} price: {self._details["price"]}'

    # Instance Method
    def get_price_culc(self):
        return f'After Car Price -> Company: {self._company} price: {self._details["price"] * Car.price_per_raise}'

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or more')
            return

        cls.price_per_raise = per
        print('Succeed! price increased')

    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return f'OK! This car is {inst._company}'

        return 'Sorry. This car is not Bmw'

# self 의미
# 인스턴스
car1 = Car('Ferrari', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'black', 'horsepower': 270, 'price': 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

Car.raise_price(1.0)
Car.raise_price(1.6)
# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# static method
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car2))