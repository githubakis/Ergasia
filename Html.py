
# kanw import thn vivliothiki h opoia mou epitrepei na anoiksw URL

import urllib.request
#ksekinaw zhtwntas apo ton xrhsth input mias html selidas
print("please insert a webpage") 

y=input()

#kathorizw thn morfh tou , thelw na einai https 
x="https://"+y



#anoigw to url mou me thn voitheia ths vivliothikis
open_url = urllib.request.urlopen(x)
mybytes = open_url.read()

decode_bytes = mybytes.decode("utf8")
   
open_url.close()
#elegxw ean einai odws kapoia html selida 
if(x=="https://"+y):
    #thn kanw print
    print(decode_bytes)
    #me thn voitheia ths count() metrw ta tags twn <p> ,<br> kai <href>
    print("<p> :"," ",decode_bytes.count("</p>")," "," <br> : "," ",decode_bytes.count("<br>")," ","<href>:"," ",decode_bytes.count("href"))
else:
    #ean den einai html selida 
    print("Please give a valid html page")

