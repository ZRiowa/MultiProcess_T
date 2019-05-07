# -*- coding:utf-8 -*-
# staticmethod 用法 是将class类中的定义的function 的调用无需【先实例化class（instance）然后再调用】（这是一般情况下class类中定义function所调用的步骤-先实例化class，再调用function）表现为Module.class().function(); @staticmethod 介入后 Module.class.function()
import time
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
 

class EuroDate(Date):
    def __str__(self):
        return "year:%s month:%s day:%s"%(self.year,self.month,self.day)

e = EuroDate.now()
print(e)

# classmethod 传入的变量不是self,是class. function(class);调用classmethod的class是就是传入的变量。 
import time
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    #@staticmethod
    #def now():
    #    t = time.localtime()
    #    return Date(t.tm_year,t.tm_mon,t.tm_mday)
    @classmethod
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday
                    )
class EuroDate(Date):
    def __str__(self):
        return "year:{} month:{} day:{}".format(t.tm_year,t.tm_mon,t.tm_mday)

e = EuroDate.now()
print(e)

#__str__定义在类内部，必须返回一个字符串（str）类型
# 啥时候会触发它的执行呢？ 打印由这个类产生的对象(实例）时，会触发执行
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "<name:%s , age:%s>"%(self.name,self.age)
p = People('Zr',24)
print(p)
str(p)