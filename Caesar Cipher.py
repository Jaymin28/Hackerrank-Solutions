def caesarCipher(s, k):
    # Write your code here
    l_s = [chr(i) for i in range(ord('a'),ord('z')+1)]
    u_s = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    str = ''
    for i in s:
        if i in l_s:
            str += l_s[(l_s.index(i) + k) % 26]
        elif i in u_s:
            str += u_s[(u_s.index(i) + k) % 26]
        else:
            str += i
    return str