#!/usr/local/bin/python3
from openpyxl import Workbook, load_workbook
from datetime import date, timedelta
import sys
import re
#from tkinter import *

def inputHours():
    hours = input('Enter hours: ')
    m = re.search('[a-zA-Z]', hours)
    if m is not None:
        print('Enter valid hours')
        return inputHours()
    return hours


def inputProjectCode():
    inp = input('Enter project code: ')
    code = inp.lower()
    if code not in codes:
        print('Not a valid code')
        return inputProjectCode()

    return code


def getTimePeriod():
    today = date.today().strftime('%m-%d-%y')
    return today


def getPayPeriod():
    pay_periods = {
        '06-17-18': '=S21',
        '07-01-18': '=S22',
        '07-15-18': '=S23',
        '07-29-18': '=S24',
        '08-12-18': '=S25',
        '08-26-18': '=S26',
        '09-09-18': '=S27',
        '09-23-18': '=S28',
        '10-07-18': '=S29',
        '10-21-18': '=S30',
        '11-04-18': '=S31',
        '11-18-18': '=S32',
        '12-02-18': '=S33',
    }

    today = getTimePeriod()

    previous_pay_period = '06-17-18'
    cell_value = None
    pay_period = None

    for key, value in sorted(pay_periods.items()):
        if today < key and today > previous_pay_period:
            pay_period = previous_pay_period #date as str
            cell_value = pay_periods[previous_pay_period] #value of last dict key
            return pay_period, cell_value

        previous_pay_period = key


def getTurnInDate(pay_period_date):
    m = re.findall('([1-9]+)', pay_period_date)
    month = m[0]
    day = m[1]
    year = '20{}'.format(m[2])
    turn_in_date = (date(int(year), int(month), int(day)) + timedelta(days=13)).strftime('%m-%d-%y')

    return turn_in_date


def editExcel(workbook, hours, code, pay_period, turn_in_date):
    hours_excel = workbook
    ws = hours_excel.active

    edit_cell = ws['C{ROW}'.format(ROW=codes[code])]

    edit_cell.value = 0 if edit_cell.value == None else edit_cell.value
    previous_value = float(edit_cell.value)
    new_value = previous_value + (float(hours)/float(80)*float(100))
    rounded_value = round(new_value, 1)
    edit_cell.value =  rounded_value

    #percent_dist_cell = ws['F{ROW}'.format(ROW=codes[code])]
    #percent_dist_cell.value = 'No Time' if edit_cell.value == 0 else percent_dist_cell.value + '%'

    ws['E7'] = pay_period[1]

    hours_excel.save('/Users/cyee/Documents/Timesheets/Timesheet_Cyee_{}.xlsx'.format(turn_in_date))


def addHours(hours, code):
    pay_period = getPayPeriod()

    turn_in_date = getTurnInDate(pay_period[0])

    try:
        hours_excel = load_workbook('/Users/cyee/Documents/Timesheets/Timesheet_Cyee_{}.xlsx'.format(turn_in_date))
    except:
        hours_excel = clearWorkbook()

    editExcel(hours_excel, hours, code, pay_period, turn_in_date)


def clearWorkbook():
    pay_period = getPayPeriod()[0]
    turn_in_date = getTurnInDate(pay_period)
    hours_excel = load_workbook('/Users/cyee/Documents/Timesheets/template.xlsx')
    hours_excel.save('/Users/cyee/Documents/Timesheets/Timesheet_Cyee_{}.xlsx'.format(turn_in_date))
    return hours_excel


def loopScript(clear=None):
    try:
        if clear == 'clear':
            clearWorkbook()

        hours = inputHours()
        code = inputProjectCode()
        addHours(hours, code)

        loopScript()
    except KeyboardInterrupt:
        print('\nGoodbye Sir')


def fix_template():
    hours_excel = load_workbook('/Users/cyee/Documents/Timesheets/template.xlsx')
    ws = hours_excel.active
    ###ENTER FIX HERE
    hours_excel.save('/Users/cyee/Documents/Timesheets/template.xlsx')


if __name__ == '__main__':
    codes = {
            'comm': 12,
            'pow2': 15,
            'prod': 18,
            '3dmss': 13,
            'mnstl': 14,
            #'hlit': ,
            'psspt': 16,
            'vatl': 17
            }

    try:
        loopScript(sys.argv[1]) if len(sys.argv) > 1 else loopScript()
    except KeyboardInterrupt:
        print('\nGoodbye Sir')
