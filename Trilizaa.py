import random
#arxikopoihsh enos string
str=["up","low","mid"]
#to up,mid,down einai oi grammes tis trillizas
up=[0,0,0]

mid=[0,0,0]

down=[0,0,0]
#arxikopoihsh enos string gia ton nikhth
winner=""
#play einai to botaki,play1 einai o user
play=False
#orizw boolean metavlhth gia thn isopalia
draw=False
while(winner=="" and draw==False):     
     #metraw gia ton an oi sthles einai gemates
    K=0
    for i in range(0,3):
        if(up[i]!=0 and mid[i]!=0 and down[i]!=0):
            K+=1
    #ean einai kai oi 3 gemates tote exw isopalia
    if (K==3):
        print ("We have a draw")
        draw=True
        play=True
    while(play==False):
        #dialegw ena random keli sth seira vash tou str
        line=random.choice(str)    
        if(line=="up"):
            column=random.randint(0,2)
            #arxikopoihsh metrhth i o opoios mas dinei posa kelia elegxthikan sth sugekrimenh seira
            i=0
            while((up[column]=="x" or up[column]=="o") and i<=2):

                column=random.randint(0,2)   
                i+=1
                #to if auto mas dinei ton guro tou paixth kai to pws paizei , dhladh randomly (dialegei tuxaia pou tha paiksei)
            if(i<3):
                up[column]="x"
                play=True
        elif(line=="mid"):
            column=random.randint(0,2)
            i=0
            while(mid[column]=="x" or mid[column]=="o" and i<=2):
                column=random.randint(0,2)   
                i+=1
            if(i<3):
                mid[column]="x"
                play=True
        else:
            column=random.randint(0,2)
            i=0
            while(down[column]=="x" or down[column]=="o" and i<=2):
                column=random.randint(0,2)   
                i+=1
            if(i<3):
                down[column]="x"
                play=True
        print(up)
        print(mid)
        print(down)
        print("  ")
        print("  ")
     #metraw gia ton an oi sthles einai gemates
    K=0
    for i in range(0,3):
        if(up[i]!=0 and mid[i]!=0 and down[i]!=0):
            K+=1
    #ean einai kai oi 3 gemates tote exw isopalia
    if (K==3):
        print ("We have a draw")
        draw=True
    # play1 einai o user
    play1=False   
    # pairnw periptwseis nikhs me to X
    if(draw==True):
        play1=True


    if((up[1]=="x" and up[2]=="x" and up[0]=="x")or(mid[0]=="x"and mid[1]=="x" and mid[2]=="x") or (down[0]=="x" and down[1]=="x" and down[2]=="x") or(up[0]=="x" and mid[0]=="x" and down[0]=="x") or (up[1]=="x"and mid[1]=="x" and down[1]=="x") or (up[2]=="x" and mid[2]=="x" and down[2]=="x") or(up[0]=="x" and mid[1]=="x" and down[2]=="x") or (up[2]=="x" and mid[1]=="x"and down[1]=="x")):                                                                                                 
            play1=True
            winner="the winner is cpu"
    while(play1==False):      
        print("please select the line you want,Insert up for the first line,mid for the second line and down for the third line")
        select1=input()
        #elegxos egkurothtas gia ton input tou xrhsth oswn afora th epilogh up,down,mid mias grammhs
        while(select1!="mid" and select1!="up" and select1!="down"): #giati na mhn ta valw isa?
            print("please select the line you want,Insert up for the first line,mid for the second line and down for the third line")
            select1=input()
            #pairnw tis 3 periptwseis mou
        if(select1=="mid"):
            print("select the square of the line.Insert 0 for the first square, 1 for the second and 2 for the third")
            #arxikopoihsh metavlhths select2 gia thn epilogh sthlhs
            select2=int(input())
            #elegxw ean h metavlhth einai anamesa sto 0-2(3 sthles) kai sunexizw elegxontas gia to pio koutaki tha dialeksei o xrhsths,epishs opote dialegw koutaki h boolean metavlhth tou user(play1) ginetai true,dhladh oti epekse
            while(select2<0 or select2>2):
                print("select the square of the line.Insert 0 for the first square, 1 for the second and 2 for the third")
                select2=int(input())
            if(mid[select2]!="o" and mid[select2]!="x"):
                play1=True
                mid[select2]="o"
        elif(select1=="up"):
            print("select the square of the line.Insert 0 for the first square, 1 for the second and 2 for the third")
            select2=int(input())
            while(select2<0 or select2>2):
                print("select the square of the line.Insert 0 for the first square, 1 for the second and 2 for the third")
                select2=int(input())

            if(up[select2]!="o" and up[select2]!="x"):
                 play1=True
                 up[select2]="o"
        else:
            print("select the square of the line.Insert 0 for the first square, 1 for the second and 2 for the third")
            select2=int(input())
            while(select2<0 or select2>2):
                print("select the square of the line.Insert 0 for the first square, 1 for the second and 2 for the third")
                select2=int(input())
            if (down[select2]!="o" and down[select2]!="x"):
                play1=True
                down[select2]="o"
    
        print(up)
        print(mid)
        print(down)
        print("  ")
        print("  ")
                
    play=False
    #elegxw pali loipon pote uparxei nikhths me to O
    if((up[1]=="o" and up[2]=="o" and up[0]=="o")or(mid[0]=="o"and mid[1]=="o" and mid[2]=="o") or (down[0]=="o" and down[1]=="o" and down[2]=="o") or(up[0]=="o" and mid[0]=="o" and down[0]=="o") or (up[1]=="o"and mid[1]=="o" and down[1]=="o") or (up[2]=="o" and mid[2]=="o" and down[2]=="o") or(up[0]=="o" and mid[1]=="o" and down[2]=="o") or (up[2]=="o" and mid[1]=="o"and down[0]=="o")):                                                                                                 
            play=True
            winner="the winner is player"
   

print(winner)
