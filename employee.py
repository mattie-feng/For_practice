#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Oct 22, 2019
装饰器目的是返回一个函数对象，返回语句的对象一定是不带参数的函数名
@property装饰器，作用是将一个方法变成属性，使用'对象.方法'使用,方法后面不用加()
@author: loxoll
'''
#需下载
import requests

class Employee:
    """A samp Employee class """
    
    raise_amt = 1.05
    
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
        
    def monthly_schedule(self, month):
        #格式化字符串常量（formatted string literals），是Python3.6新引入的一种字符串格式化方法，主要目的是使格式化字符串的操作更加简便。f-string在形式上是以 f 或 F 修饰符引领的字符串（f'xxx' 或 F'xxx'），以大括号 {} 标明被替换的字段；f-string在本质上并不是字符串常量，而是一个在运行时运算求值的表达式
        #response = requests.get(f'http://company.com/{self.last}/{month}')  
        #response = requests.get(r'http://company.com/'+self.last+r'/'+month) 
        #response = requests.get('http://company.com/%s/%s' %(self.last, month)) 
        response = requests.get('http://company.com/{}/{}'.format(self.last, month)) 
        
        if response.ok:
            return response.text
        else:
            return "Bad Response!"      