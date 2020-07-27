#EX_8 Amir Mohammad EASLAMI

def yearnumber (day, month, year):
    month_list = [31 , 28, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31]
    year_type = None
    if year % 400 == 0:
        year_type = 'leap'
    elif (year % 4 == 0 and year % 100 != 0):
        year_type = 'leap'
    else:
        year_type = 'not leap'
    day_num = None
    day_num = sum(month_list[0:month-1]) + day
    if (year_type == 'leap' and month > 2):
        day_num +=1
        return day_num
    return day_num

    
    
