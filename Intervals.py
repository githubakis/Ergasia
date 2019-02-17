def sumIntervals(*List): 
    #Arxikopoiw to ano meros tou pinaka (aristero meros diasthmatos)
 first=[] 
 #Arxikopoiw to katw meros tou pinaka (deksi meros diasthmatos)
 last=[]
 try:
  i=0
  #gemizw tous arxikopoihmenous pinakes
  while(List[0][i]):
    ko=array[0][i]
    last.append(ko[1])
    first.append(ko[0])
    i+=1

 except:
        last.sort()
        first.sort()
        max=last[-1]
        min=first[0]
        sum1=0
        #ypologizw athroisma
        for n in range(0,i):
            sum1+=(List[0][n][1]-List[0][n][0])
            #vriskw min max
        for o in range(min,max+1): 
            #metraw poses fores emfanizontai  oi arithmoi
            counter=0
            for p in range(0,i):                
                #
                #elegxw an uparxei idios arithmos
                for k in range(List[0][p][0],List[0][p][1]):
                    #an vrethei idios tote meiwnw to sum mou kata 1
                    if(o==k and counter!=0):
                        sum1-=1
                    if(o==k and counter==0):
                        counter+=1
        print(sum1)

