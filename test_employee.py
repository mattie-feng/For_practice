#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Oct 23, 2019

@author: loxoll
'''
import unittest
#在Python2.x 中 mock是一个单独模块，需要单独安装。在Python3.x中，mock已经被集成到了unittest单元测试框架中，所以，可以直接使用。
#from unittest.mock import patch
from mock import patch
from employee import Employee
from sched import scheduler

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print ("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print ("tearDownClass\n")
        
    def setUp(self):
        print ("setUp")
        self.emp_1 = Employee('Corey', 'Schafer', 5000)
        self.emp_2 = Employee('Sue', 'Smith', 6000)


    def tearDown(self):
        print ("tearDown\n")


    def test_email(self):
        print ("test_email")
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
        
    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 6300)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May') 
            self.assertEqual(schedule, 'Success')
            
        
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    