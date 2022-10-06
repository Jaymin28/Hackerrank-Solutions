def luckBalance(k, contests):
    # Write your code here
    imp = list()
    cmn = 0
    for x,y in contests:
        if y > 0:
            imp.append(x)
        else :
            cmn += x
    s = sorted(imp)
    if k < len(s):
        i = len(s) - k
        return cmn + sum(s[i:]) - sum(s[:i])
    return cmn + sum(s)