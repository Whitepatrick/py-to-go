lower_bound = 40
upper_bound = 60
def cigar_party(cigars, is_weekend):
    if cigars < lower_bound:
        print "Shitty party!"
    elif cigars >= lower_bound and is_weekend == True:
        print "Rippin' weekend party!"
    else:
        print "Rippin' weekday party!"

cigar_party(30, False) # False
cigar_party(50, False) # True
cigar_party(70, True) # True
