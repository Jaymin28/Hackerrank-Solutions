def gradingStudents(grades):
    # Write your code here
    l = list()
    for i in grades:
        if i < 38:
            l.append(i)
        elif i >= 38:
            x = i%5
            y = 5-x
            if y < 3:
                l.append(int(i + y))
            else:
                l.append(i)
    return l
