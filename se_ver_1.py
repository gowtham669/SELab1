# -*- coding: utf-8 -*-
"""SE Ver 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T7qMEdLKScE5E5RfMxp5wEbYHLu_MheQ
"""

with open('/content/Data.txt', 'r') as file:
    a = float(file.readline())
    b = float(file.readline())
    c = float(file.readline())
    x = float(file.readline())
y = a * x * x + b * x + c
print('The value of y is:', y)