print("Dwse arithmo")
# arxikopoiw se mia metavlhth x ton input apo ton xrhsth
x=int(input())
#eksetazw ean o arithmos pou dothike einai entos tou zhtoumenou diasthmatos
while (x>1000000):
    print("Dwse arithmo mikrotero apo to 1000000")
    x=int(input())
#arxikopoihsh ginomenou (to opoio thelw na ginei iso me th metavlhth dothike)
p=1
#arxikopoihsh enos string to opoio tha mou dwsei to zhtoumeno ginomeno
String=""
#loop to opoio mas dinei arithmous ews to 1.000.000(to i einai bash kai j o ektheths)
for i in range(2,1000000):
    #ean h bash mou einai ews 1000
    if(i<=1000):
        #orizw ektheth to j o opoios kumenetai apo 1-30(anapoda)
      for j in range(30,0,-1):
          #
          if((i%3!=0 and i%5!=0 and i%7!=0 and i%2!=0) or( i==2 or i==3 or i==5 or i==7)):
          #ean to mod tou x me to i^j einai 0 (to opoio arxikopoiw se mia metavlhth)
           y=i**j
          if(x%y==0 ) :
              #ftiaxnw to string tou output mou 
              String+="("+str(i)+"**"+str(j)+")"
              #pollaplasiazw to p me thn dunamh mexri na ftasw ston arithmo mou(x)
              p*=y
              #diairw to input me th dunamh kai ftiaxnw neo x
              x/=y
    else:
        if((i%3!=0 and i%5!=0 and i%7!=0 and i%2!=0) or( i==2 or i==3 or i==5 or i==7)):
        #omoiws to else otan h bash einai megaluterh tou 1000 kai o ektheths 1
             j=1
             if(x%y==0) :
              String+="("+str(i)+"**"+str(j)+")"
              p*=y
              x/=y
              #elegxw ean to x pou exw den einai 1 kai to lopi den einai keno!! emafanise to parakatw
if(x!=1 and String!=""):
 print("O arithmos autos "+str(String)+" san apotelesma o xwrismos ginetai "+str(x)+" kai den borei na diairethei me allous arithmous")
if(String!=""):
 print(String,p )
else:
 print("Den exw apotelesma")

