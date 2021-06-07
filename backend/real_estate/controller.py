from real_estate.dataset import Dataset
from real_estate.housing import Housing
import pandas as pd

class Controller(object):
    dataset = Dataset()
    housing = Housing()


    def preprocess(self, fname):
        housing = self.housing
        dataset = self.dataset
        dataset.house = housing.new_model(fname)

    @staticmethod
    def print_this(this):
        print(f'1.Test 의 type은\n {type(this.house)}')
        print(f'2.Test 의 column은\n {this.house.columns}')
        print(f'3.Test 의 상위 1개 행\n {this.house.head(1)}')
        print(f'4.Test 의 null 의 갯수\n {this.house.isnull().sum()}개')

if __name__ == '__main__':
    c = Controller
    c.preprocess("KB_housing")


# from real_estate.housing import Housing
# from real_estate.dataset import Dataset
#
#
# class Controller(object):
#
#     @staticmethod
#     def main():
#         while 1:
#             menu = input('0-Exit 1-모델생성 2-DF 생성')
#             if menu == '0':
#                 break
#             elif menu == '1':
#                 housing = Housing()
#                 dataset = Dataset()
#                 dataset.housing = housing.new_model('housing')
#                 Controller.print_this(dataset.housing)
#             else:
#                 continue
#
#
#
# # Controller.main()
# from real_estate.housing import Housing
# from real_estate.dataset import Dataset
#
#
# class Controller(object):
#
#     @staticmethod
#     def main():
#         while 1:
#             menu = input('0-Exit 1-모델생성 2-DF 생성')
#             if menu == '0':
#                 break
#             elif menu == '1':
#                 housing = Housing()
#                 dataset = Dataset()
#                 dataset.housing = housing.new_model('housing')
#                 Controller.print_this(dataset.housing)
#             else:
#                 continue
#
#     @staticmethod
#     def print_this(this):
#         print('*'*100)
#         print(f'1. Housing 의 type \n {type(this)} ')
#         print(f'2. Housing 의 column \n {this.columns} ')
#         print(f'3. Housing 의 상위 1개 행\n {this.head()} ')
#         print(f'4. Housing 의 null 의 갯수\n {this.isnull().sum()}개')
#
#         print('*' * 100)
#
# Controller.main()