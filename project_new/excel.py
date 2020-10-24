import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlwt import Workbook;
from xlutils.copy import copy
from pathlib import Path
import time

'''style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')
'''
count=0
my_file = Path('attendance_files/sheets/'+str(datetime.now().date())+'.xls');
if my_file.is_file():
    rb = open_workbook('attendance_files/sheets/'+str(datetime.now().date())+'.xls');
    book = copy(rb);
    sh = book.get_sheet(0)
    # file exists
else:
    book = xlwt.Workbook()
    sh = book.add_sheet('class 1')
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    #variables = [x, y, z]
    #x_desc = 'Display'
    #y_desc = 'Dominance'
    #z_desc = 'Test'
    #desc = [x_desc, y_desc, z_desc]
    # sh.write(0,0,datetime.now().date(),style1);


    col1_name = 'Name'
    col2_name = 'Lec 1'
    col3_name = 'Lec 2'
    col4_name = 'Lec 3'
    col5_name = 'Lec 4'
    col6_name = 'Lec 5'

    sh.write(0,0,col1_name,style0)
    sh.write(0, 1, col2_name,style0)
    sh.write(0, 2, col3_name, style0)
    sh.write(0, 3, col4_name, style0)
    sh.write(0, 4, col5_name, style0)
    sh.write(0, 5, col6_name, style0)

def output(filename, sheet,num, name, present):
    print("label",num)
    print("name",name)


    t = time.localtime()
    hour = time.strftime("%H", t)
    min = time.strftime("%M", t)
    if (int(hour) > 12):
        hour = int(hour)
        hour = hour - 12
    main_time = str(hour) + ":" + str(min)
    print('main time excel:',main_time)
    sh.write(num-1,0,name)
    if ((main_time >= "8:40" and main_time <= "8:50")):
        sh.write(num - 1, 1, present)
    elif((main_time >= "9:45" and main_time <= "9:50")):
        sh.write(num - 1, 2, present)
    elif((main_time >= "11:30" and main_time <= "11:35")):
        sh.write(num - 1, 3, present)
    elif((main_time >= "12:30" and main_time <= "12:35")):
        sh.write(num - 1, 4, present)
    elif((main_time >= "1:30")):
        sh.write(num - 1, 5, present)
    else:
        print("in else excel")
        print(sh.write(num - 1, 1, present))

    # elif((main_time >= "4:00" and main_time <= "6:35")):
    #     sh.write(num-1, 1, present)
    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    fullname=filename+' '+str(datetime.now().date())+'.xls';
    book.save('attendance_files/sheets/'+fullname)
    return fullname;
