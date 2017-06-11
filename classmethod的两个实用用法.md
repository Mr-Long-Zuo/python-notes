> 用法一：classmethod 和 staticmethod 都可以不用实例化直接调用

```
class demo1:
    @classmethod
    def c_demo(cls):
        return 1

    @staticmethod
    def s_demo():
        return 2

print(demo1.c_demo())   #1
print(demo1.s_demo())   #2
```

> 用法二：在不改变已经写好的类里面的方法的情况下，对输入的数据进行处理，在外国论坛看到一个特别好的例子

```
# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

# 输出年月日，正常的情况下

class demo2:
    def __init__(self, year = 0, month = 0, day = 0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return "year:%d, month:%d, day:%d" % (self.year, self.month, self.day)

year = 2017
month = 7
day = 1

demo2 = demo2(year, month, day)
print(demo2.out_date())

# year:2017, month:7, day:1
```

```
# 如果用户输入的是2017-5-6格式，需要在输出前处理一下，就可以使用classmethod达到想要的效果

class demo3:
    def __init__(self, year = 0, month = 0, day = 0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return "year:%d, month:%d, day:%d" % (self.year, self.month, self.day)

    @classmethod
    def pre_out(cls, date_string):
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

date = "2017-5-6"
year = 2017
month = 7
day = 1

try:
    demo3 = demo3.pre_out(date)
except:
    demo3 = demo3(year, month, day)

print(demo3.out_date())

# year:2017, month:5, day:6
```