def good_vs_evil(good, evil):
    g_w = [1,2,3,3,4,10]
    e_w = [1,2,2,2,3,5,10]
    good_count = []
    evil_count = []
    g_worth = 0
    e_worth = 0


    m = ""
    for i in range (0,len(good)):
        if good[i] != " " and i+1!=len(good):
            m += good[i]
        elif good[i] != " " and i+1==len(good):
            m += good[i]
            good_count.append(int(m))
            m = ""
        else:
            good_count.append(int(m))
            m = ""

    for i in range (0,len(evil)):
        if evil[i] != " " and i+1!=len(evil):
            m += evil[i]
        elif evil[i] != " " and i+1==len(evil):
            m += evil[i]
            evil_count.append(int(m))
            m = ""
        else:
            evil_count.append(int(m))
            m = ""

    for i in range (0,len(g_w)):
        g_worth += g_w[i] * good_count[i]
    for i in range (0,len(e_w)):
        e_worth += e_w[i] * evil_count[i]

    if g_worth>e_worth:
        return ("Battle Result: Good triumphs over Evil")
    elif g_worth==e_worth:
        return ("Battle Result: No victor on this battle field")
    else:
        return ("Battle Result: Evil eradicates all trace of Good")


  