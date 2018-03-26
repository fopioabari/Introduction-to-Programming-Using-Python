#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:53:24 2018

@author: francisabari
"""

class LinearEquation:

            def __init__(self, a, b, c, d, e, f):

                        self.a=a
                        self.b=b
                        self.c=c
                        self.d=d
                        self.e=e
                        self.f=f

            def getA(self):
                        return self.a

            def getB(self):
                        return self.b

            def getC(self):
                        return self.c

            def getD(self):
                        return self.d

            def getE(self):
                        return self.e

            def getF(self):
                        return self.f

            def isSolvable(self):
                        deno=(self.getA()*self.getD())-(self.getB()*self.getC())

                        if deno==0:
                                    return False

                        else:
                                    return True

            def getX(self):

                        x_num=(self.getE()*self.getD())-(self.getB()*self.getF())

                        x_deno=(self.getA()*self.getD())-(self.getB()*self.getC())

                        x=x_num/x_deno

                        return x

            def getY(self):

                        y_num=(self.getA()*self.getF())-(self.getE()*self.getC())

                        y_deno=(self.getA()*self.getD())-(self.getB()*self.getC())

                        y=y_num/y_deno

                        return y

def main():

            print("Algebra 2 x 2 linear equation")
            print("The equations are: ")
            print("ax + by = e")
            print("cx + dy = f")
            print("To solve the equations, enter the co-efficient values.")
            a=int(input("Enter value of a: "))
            b=int(input("Enter value of b: "))
            c=int(input("Enter value of c: "))
            d=int(input("Enter value of d: "))
            e=int(input("Enter value of e: "))
            f=int(input("Enter value of f: "))
            linear = LinearEquation(a, b, c, d, e, f)    
            if linear.isSolvable():   

                        print("x is = ",linear.getX(), " and y is = ",linear.getY()  )
            else:
                        print("The equation has no solution.")

main()


