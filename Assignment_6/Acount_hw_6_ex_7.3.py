#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:44:25 2018

@author: francisabari
"""

class Account:

   def __init__(self):

       self.id = 0;

       self.balance = 100;

       self.annualInterestRate = 0;

   def set_id(self,iden):

       self.id = iden;

   def set_balance(self,bal):

       self.balance = bal;

   def set_rate(self,r):

       self.annualInterestRate = r;

   def get_id(self):

       return self.id;

   def get_balance(self):

       return self.balance;

   def get_rate(self):

       return self.rate;

   def getMonthlyInterestRate(self):

       return self.annualInterestRate/12;

   def getMonthlyInterest(self):

       return self.balance*self.getMonthlyInterestRate()

   def withdraw(self,w):

       if (w > self.balance):

           print ("Insufficient balance, try again")

       else:

           self.balance -= w;

   def deposit(self,d):

       self.balance += d;

acc = Account()

acc.set_id(1122);

acc.set_balance(20000);

acc.set_rate(4.5);

acc.withdraw(2500);

acc.deposit(3000);

print ("ID is "+str(acc.id))

print ("balance is "+str(acc.balance))

print ("Monthly interest rate is "+str(acc.getMonthlyInterestRate()))

print ("Monthly interest is "+str(acc.getMonthlyInterest()))