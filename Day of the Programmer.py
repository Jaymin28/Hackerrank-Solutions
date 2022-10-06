def dayOfProgrammer(year):
    # Write your code here
        if year == 1918:
            return '26.09.1918'
        elif 1918 < year <= 2700:
            if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                return ('12.09.'+ str(year))
            else :
                return ('13.09.'+ str(year))
        elif  1700 <= year < 1918:
            if year % 4 == 0:
                return ('12.09.'+ str(year))
            else :
                return ('13.09.'+ str(year))    