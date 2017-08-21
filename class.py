from login import  loginDemo
loginDemo.loginBaidu()
class Toutiao:
    def __init__(self,logger = None):
        print("构造函数")  # 对象生成的时候会自动调用


toutiao = Toutiao()


class Human(object):

    laugh = 'hahahaha'
    __age = 12

    def __init__(self,name):
        self.name = name
        self.laugh = 'new laugh'
        print(self.__dict__)
        print('__init__ is called!')
        print(self.__age)

    def show_name(self):
        print('my name is :' + self.name)

    def __show_laugh(self):
        print(self.laugh)

    def laugh_10th(self):
        for i in range(10):
            self.show_laugh()

human=Human('gg')
human.show_name()
print(human.laugh)
