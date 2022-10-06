def taumBday(b, w, bc, wc, z):
    # Write your code here
    if bc + z < wc:
        return (b * bc) + (w * (bc + z))
    elif wc + z < bc:
        return (w * wc) + (b * (wc + z))
    else :
        return (b * bc) + (w * wc)