# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
import math

ticker='MA'
input_dir = r'D:\Program Files\Courses\BU\CS677\CS677\HW1'
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:   
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    """    your code for assignment 1 goes here
    """
    mon_total_return = []
    mon_neg_return = []
    mon_pos_return = []
    mon_total_SD = 0.0
    mon_neg_SD = 0.0
    mon_pos_SD = 0.0
    tue_total_return = []
    tue_neg_return = []
    tue_pos_return = []
    tue_total_SD = 0.0
    tue_neg_SD = 0.0
    tue_pos_SD = 0.0
    wed_total_return = []
    wed_neg_return = []
    wed_pos_return = []
    wed_total_SD = 0.0
    wed_neg_SD = 0.0
    wed_pos_SD = 0.0
    thur_total_return = []
    thur_neg_return = []
    thur_pos_return = []
    thur_total_SD = 0.0
    thur_neg_SD = 0.0
    thur_pos_SD = 0.0
    fri_total_return = []
    fri_neg_return = []
    fri_pos_return = []
    fri_total_SD = 0.0
    fri_neg_SD = 0.0
    fri_pos_SD = 0.0

    for i in range(1, len(lines)):
        new_list = lines[i].split(",")
        percentage_return = float(new_list[13])
        if i % 5 == 1:
            mon_total_SD += percentage_return**2
            mon_total_return.append(percentage_return)
            if percentage_return < 0:
                mon_neg_return.append(percentage_return)
                mon_neg_SD += percentage_return**2
            else:
                mon_pos_return.append(percentage_return)
                mon_pos_SD += percentage_return**2
        elif i % 5 == 2:
            tue_total_SD += percentage_return ** 2
            tue_total_return.append(percentage_return)
            if percentage_return < 0:
                tue_neg_return.append(percentage_return)
                tue_neg_SD += percentage_return ** 2
            else:
                tue_pos_return.append(percentage_return)
                tue_pos_SD += percentage_return ** 2
        elif i % 5 == 3:
            wed_total_SD += percentage_return ** 2
            wed_total_return.append(percentage_return)
            if percentage_return < 0:
                wed_neg_return.append(percentage_return)
                wed_neg_SD += percentage_return ** 2
            else:
                wed_pos_return.append(percentage_return)
                wed_pos_SD += percentage_return ** 2
        elif i % 5 == 4:
            thur_total_SD += percentage_return ** 2
            thur_total_return.append(percentage_return)
            if percentage_return < 0:
                thur_neg_return.append(percentage_return)
                thur_neg_SD += percentage_return ** 2
            else:
                thur_pos_return.append(percentage_return)
                thur_pos_SD += percentage_return ** 2
        elif i % 5 == 0:
            fri_total_SD += percentage_return ** 2
            fri_total_return.append(percentage_return)
            if percentage_return < 0:
                fri_neg_return.append(percentage_return)
                fri_neg_SD += percentage_return ** 2
            else:
                fri_pos_return.append(percentage_return)
                fri_pos_SD += percentage_return ** 2

    mon_total_mean = sum(mon_total_return) / len(mon_total_return)
    mon_neg_mean = sum(mon_neg_return) / len(mon_neg_return)
    mon_pos_mean = sum(mon_pos_return) / len(mon_pos_return)
    mon_total_SD = math.sqrt(mon_total_SD / len(mon_total_return) - mon_total_mean**2)
    mon_neg_SD = math.sqrt(mon_neg_SD / len(mon_neg_return) - mon_neg_mean**2)
    mon_pos_SD = math.sqrt(mon_pos_SD / len(mon_pos_return) - mon_pos_mean**2)
    tue_total_mean = sum(tue_total_return) / len(tue_total_return)
    tue_neg_mean = sum(tue_neg_return) / len(tue_neg_return)
    tue_pos_mean = sum(tue_pos_return) / len(tue_pos_return)
    tue_total_SD = math.sqrt(tue_total_SD / len(tue_total_return) - tue_total_mean ** 2)
    tue_neg_SD = math.sqrt(tue_neg_SD / len(tue_neg_return) - tue_neg_mean ** 2)
    tue_pos_SD = math.sqrt(tue_pos_SD / len(tue_pos_return) - tue_pos_mean ** 2)
    wed_total_mean = sum(wed_total_return) / len(wed_total_return)
    wed_neg_mean = sum(wed_neg_return) / len(wed_neg_return)
    wed_pos_mean = sum(wed_pos_return) / len(wed_pos_return)
    wed_total_SD = math.sqrt(wed_total_SD / len(wed_total_return) - wed_total_mean ** 2)
    wed_neg_SD = math.sqrt(wed_neg_SD / len(wed_neg_return) - wed_neg_mean ** 2)
    wed_pos_SD = math.sqrt(wed_pos_SD / len(wed_pos_return) - wed_pos_mean ** 2)
    thur_total_mean = sum(thur_total_return) / len(thur_total_return)
    thur_neg_mean = sum(thur_neg_return) / len(thur_neg_return)
    thur_pos_mean = sum(thur_pos_return) / len(thur_pos_return)
    thur_total_SD = math.sqrt(thur_total_SD / len(thur_total_return) - thur_total_mean ** 2)
    thur_neg_SD = math.sqrt(thur_neg_SD / len(thur_neg_return) - thur_neg_mean ** 2)
    thur_pos_SD = math.sqrt(thur_pos_SD / len(thur_pos_return) - thur_pos_mean ** 2)
    fri_total_mean = sum(fri_total_return) / len(fri_total_return)
    fri_neg_mean = sum(fri_neg_return) / len(fri_neg_return)
    fri_pos_mean = sum(fri_pos_return) / len(fri_pos_return)
    fri_total_SD = math.sqrt(fri_total_SD / len(fri_total_return) - fri_total_mean ** 2)
    fri_neg_SD = math.sqrt(fri_neg_SD / len(fri_neg_return) - fri_neg_mean ** 2)
    fri_pos_SD = math.sqrt(fri_pos_SD / len(fri_pos_return) - fri_pos_mean ** 2)

    print(format(mon_total_mean, '.2f'), format(mon_total_SD, '.2f'), len(mon_neg_return), format(mon_neg_mean, '.2f'),
          format(mon_neg_SD, '.2f'), len(mon_pos_return),
          format(mon_pos_mean, '.2f'), format(mon_pos_SD, '.2f'))
    print(format(tue_total_mean, '.2f'), format(tue_total_SD, '.2f'), len(tue_neg_return), format(tue_neg_mean, '.2f'),
          format(tue_neg_SD, '.2f'), len(tue_pos_return),
          format(tue_pos_mean, '.2f'), format(tue_pos_SD, '.2f'))
    print(format(wed_total_mean, '.2f'), format(wed_total_SD, '.2f'), len(wed_neg_return), format(wed_neg_mean, '.2f'),
          format(wed_neg_SD, '.2f'), len(wed_pos_return),
          format(wed_pos_mean, '.2f'), format(wed_pos_SD, '.2f'))
    print(format(thur_total_mean, '.2f'), format(thur_total_SD, '.2f'), len(thur_neg_return), format(thur_neg_mean, '.2f'),
          format(thur_neg_SD, '.2f'), len(thur_pos_return),
          format(thur_pos_mean, '.2f'), format(thur_pos_SD, '.2f'))
    print(format(fri_total_mean, '.2f'), format(fri_total_SD, '.2f'), len(fri_neg_return), format(fri_neg_mean, '.2f'),
          format(fri_neg_SD, '.2f'), len(fri_pos_return),
          format(fri_pos_mean, '.2f'), format(fri_pos_SD, '.2f'))

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)









