#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Employee:
    """A samp Employee class """

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    '''
    @property装饰器，作用是将一个方法变成属性，使用'对象.方法'使用,方法后面不用加()
    '''

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(
            'http://company.com/{}/{}'.format(self.last, month))

        if response.ok:
            return response.text
        else:
            return "Bad Response!"
