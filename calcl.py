my_list=[-79.0159744408945,-68.8945686900959,-55.3226837060703,-28.1789137380192,4.71565495207668,36.9201277955272,69.814696485623,
         83.8466453674121,98.3386581469646,136.063897763579,160.447284345048,173.55910543131,-171.02875399361,-151.70607028754,-133.993610223642]
list=[]
for i in range(len(my_list) -1):

    if(my_list[i+1]<[0.0] & my_list[i]>[0.0]):
        b=[my_list[i + 1] - my_list[i]]
    else:
        c=my_list[i+1]
        list.append(c)


    mptx2=my_list[i + 1]
    mptx1=my_list[i]
    a=[my_list[i + 1]-my_list[i]]
    list.append(a)


for j in list:
    if(j>[-180]):
        mptx2 = mptx2 + 360
        mptx2new = mptx2 * 111391.491
        print("am lessthan 180 for ",j,"value",mptx2new)






