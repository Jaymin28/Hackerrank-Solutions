def timeConversion(s):
    # Write your code here
    time = s.split(':')
    if s[-2:] == 'AM':
        if time[0] == '12':
            time[0] = '00'
    elif s[-2:] == 'PM':
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)
    s = ':'.join(time)
    return s[:-2]