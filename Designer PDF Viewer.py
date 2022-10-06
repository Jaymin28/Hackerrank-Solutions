def designerPdfViewer(h, word):
    # Write your code here
    import string
    maxi = 0
    alph = string.ascii_lowercase
    for i in word:
        x = alph.index(i)
        maxi  = max(maxi, h[x])
    
    return maxi * len(word)