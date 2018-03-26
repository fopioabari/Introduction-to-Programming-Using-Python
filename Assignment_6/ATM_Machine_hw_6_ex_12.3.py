#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:20:13 2018

@author: francisabari
"""

class Account:
   def __init__(self, id, balance = 100, annualInterestRate = 0):
       self.__id = id
       self.__balance = balance
       self.__annualInterestRate = annualInterestRate
   def getId(self):
       return self.__id
   def getBalance(self):
       return self.__balance
   def getAnnualInterestRate(self):
       return self.__annualInterestRate
   def getMonthlyInterestRate(self):
       return self.__annualInterestRate / 12
   def setPreviousPrice(self, previousPrice):
       self.previousPrice = previousPrice
   def setCurrentPrice(self, currentPrice):
       self.currentPrice = currentPrice
   def withdraw(self, amount):
       self.__balance -= amount
   def deposit(self, amount):
       self.__balance += amount
   def getMonthlyInterest(self):
       return self.__balance * self.getMonthlyInterestRate()

def main():
   accounts = [];
   for i in range(0, 10):
       account = Account(i, 100);
       accounts.append(account);
       
   while True:
       id = int(input("\n Enter an account id: "));
       while id < 0 or id > 9:
           id = int(input("\n Invalid Id.. Re-enter: "));
       while True:
           print ("\n Main menu")
           print (" 1: check balance") 
           print (" 2: withdraw")
           print (" 3: deposit")
           print (" 4: exit") 
           selection = int(input("\n Enter your selection: "));

           for acc in accounts:
               if acc.getId() == id:
                   accountObj = acc;
                   break;
           if selection == 1:
               print(" Your current balance is: $", accountObj.getBalance());
              
           elif selection == 2:
               amt = float(input(" Enter amount to withdraw: $"));
               accountObj.withdraw(amt);
               print(" Updated Balance: $" + str(accountObj.getBalance()));
              
           elif selection == 3:
               amt = float(input(" Enter amount to deposit: $"));
               accountObj.deposit(amt);
               print(" Updated Balance: $" + str(accountObj.getBalance()));
          
           else:
               break;
          
main()
    