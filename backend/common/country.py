class Country(object):
    name = 'Country Name'
    population = 'Population'
    capital = 'Capital'

    def show(self):
        print('Country Class Method')


class Korea(Country):

    def show_name(self):
        print(f'Country Name is {self.name}')

def execute():  ##함수형 프로그래밍  위와 같은 방식을 함수형!!
    k = Korea()
    k.name = "대한민국"
    k.show_name()

execute()##실행문