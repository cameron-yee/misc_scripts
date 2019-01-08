#!/usr/local/bin/python3
from openpyxl import Workbook, load_workbook
from datetime import date, datetime, timedelta
import sys
import re
#from tkinter import *

def inputPercentage():
    percentage = input('Enter percentage: ')
    m = re.search('[a-zA-Z]', percentage)
    if m is not None:
        print('Enter valid percentage')
        return inputPercentage()
    return percentage


def inputProjectCode():
    inp = input('Enter project code: ')
    code = inp.lower()
    if code not in codes:
        print('Not a valid code')
        return inputProjectCode()

    return code


def getTimePeriod():
    #today = date.today().strftime('%m-%d-%y')
    today = datetime.today()
    return today


def getPayPeriod():
    pay_periods = [
        '12/16/18',
        '12/30/18',
        '01/13/19',
        '01/27/19',
        '02/10/19',
        '02/24/19',
        '03/10/19',
        '03/24/19',
        '04/07/19',
        '04/21/19',
        '05/05/19',
        '05/19/19',
        '06/02/19',
        '06/16/19',
        '06/30/19',
        '07/14/19',
        '07/28/19',
        '08/11/19',
        '08/25/19',
        '09/08/19',
        '09/22/19',
        '10/06/19',
        '10/20/19',
        '11/03/19',
        '11/17/19',
        '12/01/19',
    ]

    today = getTimePeriod()

    previous_pay_period = '12/16/18'
    cell_value = None
    pay_period = None

    for date in pay_periods:
        if today < datetime.strptime(date, '%m/%d/%y') and today > datetime.strptime(previous_pay_period, '%m/%d/%y'):
            #pay_period = previous_pay_period #date as str
            pay_period = date #date as str
            #cell_value = pay_periods[previous_pay_period] #value of last dict key
            print(type(pay_period))
            return pay_period


def getTurnInDate(pay_period_date):
    m = re.findall('([1-9]+)', pay_period_date)
    month = m[0]
    day = m[1]
    year = '20{}'.format(m[2])
    turn_in_date = (date(int(year), int(month), int(day)) + timedelta(days=13)).strftime('%m-%d-%y')

    return turn_in_date


def editExcel(workbook, percentage, code, pay_period, turn_in_date):
    hours_excel = workbook
    ws = hours_excel.active

    ws['E7'] = pay_period

    #Gets active projects and sorts alphabetically
    def sortProjects():
        count = 0
        active_projects = {}

        for r in range(12,28):
            if ws['C{}'.format(r)].value is not None:
                active_projects[ws['B{}'.format(r)].value] = ws['C{}'.format(r)].value
                count += 1

        if code.upper() in active_projects:
            active_projects[code.upper()] += percentage #(float(hours)/float(80)*float(100))
        else:
            active_projects[code.upper()] = percentage #(float(hours)/float(80)*float(100))

        sorted_projects = sorted(active_projects.items(), key=lambda a: a[0])
        return sorted_projects

    sorted_projects = sortProjects()

    #TODO: Refactor 3 for loops into 1-2
    #Alphabetically edits rows with active projects and hours
    row=12
    for pair in sorted_projects: 
        ws['B{}'.format(row)].value = pair[0]
        ws['C{}'.format(row)].value = pair[1]
        row += 1

    #Sets values for all empty rows
    for i in range(row, 28):
        ws['B{}'.format(i)].value = 'Active Project'
        ws['C{}'.format(i)].value = None

    hours_excel.save('/Users/cyee/Documents/Timesheets/Timesheet_Cyee_{}.xlsx'.format(turn_in_date))


def addPercentage(percentage, code):
    pay_period = getPayPeriod()

    turn_in_date = getTurnInDate(pay_period)

    try:
        hours_excel = load_workbook('/Users/cyee/Documents/Timesheets/Timesheet_Cyee_{}.xlsx'.format(turn_in_date))
    except:
        hours_excel = clearWorkbook()

    editExcel(hours_excel, percentage, code, pay_period, turn_in_date)


def clearWorkbook():
    pay_period = getPayPeriod()
    turn_in_date = getTurnInDate(pay_period)
    hours_excel = load_workbook('/Users/cyee/Documents/Timesheets/template.xlsx')
    hours_excel.save('/Users/cyee/Documents/Timesheets/Timesheet_Cyee_{}.xlsx'.format(turn_in_date))
    return hours_excel


def loopScript(clear=None):
    try:
        if clear == 'clear':
            clearWorkbook()

        percentage = inputPercentage()
        code = inputProjectCode()
        addPercentage(percentage, code)

        loopScript()
    except KeyboardInterrupt:
        print('\nGoodbye Sir')


if __name__ == '__main__':
    codes = ['comm','web','prod','3dmss','hlit','psspt','vatl','prch1']

    try:
        loopScript(sys.argv[1]) if len(sys.argv) > 1 else loopScript()
    except KeyboardInterrupt:
        print('\nGoodbye Sir')









#def fix_template():
#    hours_excel = load_workbook('/Users/cyee/Documents/Timesheets/template.xlsx')
#    ws = hours_excel.active
#    ###ENTER FIX HERE
#    hours_excel.save('/Users/cyee/Documents/Timesheets/template.xlsx')


