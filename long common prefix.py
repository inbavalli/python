l=[[9,8,0], [9,8,0,4,5], [9,8,0,2,3], [9,8,0,5,1,7,2]]
newl=l[0]
if len(l)>1:
    for li in l[1:]:
    newl=[x for x in newl if x in li]
