# File name 23212326.py
# This program is  is to help the researchers in analysing eight geodesic (surface) and eight 3D Euclidian distances 
# between a few facial landmarks across four expressions 'Neutral', 'Angry', 'Disgust', 'Happy'.
# Important variable : adultID, Expression, Diatance, Gdis,Ldis
# Author: Lili Liu
# Finish data: 16/09/2022

def main(csvfile, adultID, Option):
    try:#if any error during reading a file data, it will be error and return the empty list 
        with open('ExpData_Sample.csv','r') as myfile:
            a = myfile.readlines()
        
            
        b = a[0][:-1].split(',')# read the the first line remove the last chr'\n", split string into list, output the title list
        x = b.index('ID')#get the ID index in the title list
        y = b.index('Expression')#get Expression index in the title list
        z = b.index('Distance')# get Distance index in the title list
        m = b.index('Gdis') #get Gdis index in the title list
        n = b.index('Ldis') #get Ldis index in the title list   
        
        #make a new list for each column
        idlist = []# make an empty list for later to append value in 
        expressionlist = []
        distancelist = []
        Gdislist = []
        Ldislist = []
        for line in a:
            listall= line.split(',')# list all lines, each line become a list
            
            idlist.append(listall[x])#all lines element which index=x and turns it into lower case, append it to the new list idlist
            expressionlist.append(listall[y].lower())#all lines element which index=y, append it to the new list expressionlist
            distancelist.append(listall[z])#all lines element which index=z, append it to the new list distancelist
            Gdislist.append(listall[m])#all lines element which index=m, append it to the new list Gdislist
            Ldislist.append(listall[n]) # all lines element which index=n, append it to the new list Ldislist
       
        
        for i in range(1,len(Gdislist)):
            if float(Gdislist[i])<0 or float(Gdislist[i])==0:
                Gdislist[i]=50 #replace vaule with 50 if distance < or =0
        
        for i in range(1,len(Ldislist)):
            if float(Ldislist[i])<0 or float(Ldislist[i])==0:
                Ldislist[i]=50#replace vaule with 50 if distance < or =0
    except:#if any error during reading a file data, it will be error and return the empty list 
        idlist = [] 
        expressionlist = []
        distancelist = []
        Gdislist = []
        Ldislist = []
          
    if Option == "stats":
        try:#if any error for option stats, it will return empty list for OP1,OP2,OP3,OP4
        
            OP1 = []
            OP2 = [[],[],[],[]]# Op2 is a big list which include 4 small list, each small list have 8 value for one expression Gdis and Ldis difference
            OP3 = []
            OP4 = []
            for n in range(1,9):   
                k = OP11(adultID,idlist,distancelist,Gdislist,Ldislist,n)# call function OP11
                OP1.append(k)#storage for distance n in range (1,9), 8 times of l result into OP1 list

                O1,O2,O3,O4=OP22(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist,n)#call function OP22
                OP2[0].append(O1)#for expression=Neutral, storage the 8 distance difference of Gdis and Ldis into Op1 index 0
                OP2[1].append(O2)#for expression=Angry, storage the 8 distance difference of Gdis and Ldis into Op1 index 1
                OP2[2].append(O3)#for expression=Disgust, storage the 8 distance difference of Gdis and Ldis into Op1 index 2
                OP2[3].append(O4)#for expression=Happy, storage the 8 distance difference of Gdis and Ldis into Op1 index 3
                
                q=OP33(adultID,idlist,distancelist,Gdislist,n)#call function OP33
                OP3.append(q)#storage for distance n in range (1,9), 8 times of q result into Op3 list
                
                r=OP44(adultID,idlist,distancelist,Ldislist,n)#call function OP44
                OP4.append(r)#storage for distance n in range (1,9), 8 times of r result into Op4 list
                
            return OP1,OP2,OP3,OP4
        except:#if any error for option stats, it will return empty list for OP1,OP2,OP3,OP4
            return[],[],[],[]
            
    if Option == "FR":
        try:#If any error for FR , it will return empty string for ID , and zero for cossim

                aa=A(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function A
                aa1=A1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function A1
                bb=B(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function B
                bb1=B1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function B1
                cc=C(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function C
                cc1=C1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function C1
                dd=D(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function D
                dd1=D1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist)#call function D1
              
                x1= aa1.index('1')# make x1 is the index number for distance= '1' in aa1 list
                x2= aa1.index('2')# make x2 is the index number for distance= '2' in aa1 list
                x3= aa1.index('3')# make x3 is the index number for distance= '3' in aa1 list
                x4= aa1.index('4')# make x4 is the index number for distance= '4' in aa1 list
                x5= aa1.index('5')# make x5 is the index number for distance= '5' in aa1 list
                x6= aa1.index('6')# make x6 is the index number for distance= '6' in aa1 list
                x7= aa1.index('7')# make x7 is the index number for distance= '7' in aa1 list
                x8= aa1.index('8')# make x8 is the index number for distance= '8' in aa1 list
                
                y1= bb1.index('1')# make y1 is the index number for distance= '1' in bb1 list
                y2= bb1.index('2')# make y2 is the index number for distance= '2' in bb1 list
                y3= bb1.index('3')# make y3 is the index number for distance= '3' in bb1 list
                y4= bb1.index('4')# make y4 is the index number for distance= '4' in bb1 list
                y5= bb1.index('5')# make y5 is the index number for distance= '5' in bb1 list
                y6= bb1.index('6')# make y6 is the index number for distance= '6' in bb1 list
                y7= bb1.index('7')# make y7 is the index number for distance= '7' in bb1 list
                y8= bb1.index('8')# make y8 is the index number for distance= '8' in bb1 list
                
                z1= cc1.index('1')# make z1 is the index number for distance= '1' in cc1 list
                z2= cc1.index('2')# make z2 is the index number for distance= '2' in cc1 list
                z3= cc1.index('3')# make z3 is the index number for distance= '3' in cc1 list
                z4= cc1.index('4')# make z4 is the index number for distance= '4' in cc1 list
                z5= cc1.index('5')# make z5 is the index number for distance= '5' in cc1 list
                z6= cc1.index('6')# make z6 is the index number for distance= '6' in cc1 list
                z7= cc1.index('7')# make z7 is the index number for distance= '7' in cc1 list
                z8= cc1.index('8')# make z8 is the index number for distance= '8' in cc1 list
                
                w1= dd1.index('1')# make w1 is the index number for distance= '1' in dd1 list
                w2= dd1.index('2')# make w2 is the index number for distance= '2' in dd1 list
                w3= dd1.index('3')# make w3 is the index number for distance= '3' in dd1 list
                w4= dd1.index('4')# make w4 is the index number for distance= '4' in dd1 list
                w5= dd1.index('5')# make w5 is the index number for distance= '5' in dd1 list
                w6= dd1.index('6')# make w6 is the index number for distance= '6' in dd1 list
                w7= dd1.index('7')# make w7 is the index number for distance= '7' in dd1 list
                w8= dd1.index('8')# make w8 is the index number for distance= '8' in dd1 list           
                
                # calculate the cossim similarity for referenced ID between itself Neutral with itself Angry 
                similarityAB=(aa[x1]*bb[y1]+aa[x2]*bb[y2]+aa[x3]*bb[y3]+aa[x4]*bb[y4]+aa[x5]*bb[y5]+aa[x6]*bb[y6]+aa[x7]*bb[y7]+aa[x8]*bb[y8])/(((aa[x1]**2+aa[x2]**2+aa[x3]**2+aa[x4]**2+aa[x5]**2+aa[x6]**2+aa[x7]**2+aa[x8]**2)**0.5)*((bb[y1]**2+bb[y2]**2+bb[y3]**2+bb[y4]**2+bb[y5]**2+bb[y6]**2+bb[y7]**2+bb[y8]**2)**0.5))
                # calculate the cossim similarity for referenced ID between itself Neutral with itself Disgust 
                similarityAC=(aa[x1]*cc[z1]+aa[x2]*cc[z2]+aa[x3]*cc[z3]+aa[x4]*cc[z4]+aa[x5]*cc[z5]+aa[x6]*cc[z6]+aa[x7]*cc[z7]+aa[x8]*cc[z8])/(((aa[x1]**2+aa[x2]**2+aa[x3]**2+aa[x4]**2+aa[x5]**2+aa[x6]**2+aa[x7]**2+aa[x8]**2)**0.5)*((cc[z1]**2+cc[z2]**2+cc[z3]**2+cc[z4]**2+cc[z5]**2+cc[z6]**2+cc[z7]**2+cc[z8]**2)**0.5))
                # calculate the cossim similarity for referenced ID between itself Neutral with itself Happy 
                similarityAD=(aa[x1]*dd[w1]+aa[x2]*dd[w2]+aa[x3]*dd[w3]+aa[x4]*dd[w4]+aa[x5]*dd[w5]+aa[x6]*dd[w6]+aa[x7]*dd[w7]+aa[x8]*dd[w8])/(((aa[x1]**2+aa[x2]**2+aa[x3]**2+aa[x4]**2+aa[x5]**2+aa[x6]**2+aa[x7]**2+aa[x8]**2)**0.5)*((dd[w1]**2+dd[w2]**2+dd[w3]**2+dd[w4]**2+dd[w5]**2+dd[w6]**2+dd[w7]**2+dd[w8]**2)**0.5))                                                                                                                
        
                
                # calculate all ID expression= Neutral with reference ID cossim similarity value
               
                Netural_list=[[] for x in range(int((len(idlist)-1)/32))]
                for n in range(1,9):
                    ee=E(adultID,idlist,expressionlist,Gdislist,distancelist,n)
                   
                #call function E, list all adultID's Expression=Netural 8 distance Gdis
                    for m in range (int((len(idlist)-1)/32)):
                        Netural_list[m].append(ee[m])
                
                #Netural_list=[neturallist[i:i+8] for i in range(0, len(ee),8)]#split the ee per adultID,each small list have 8 value for one adultID
                similaritylist = []
                if len(Netural_list)==1:#if only one ID data in the file, the most similar ID is itself, and the cossim is the other expression of this ID
                    h=0
                else:
                    for ff in Netural_list:
                       similarity=(aa[x1]*ff[0]+aa[x2]*ff[1]+aa[x3]*ff[2]+aa[x4]*ff[3]+aa[x5]*ff[4]+aa[x6]*ff[5]+aa[x7]*ff[6]+aa[x8]*ff[7])/(((aa[x1]**2+aa[x2]**2+aa[x3]**2+aa[x4]**2+aa[x5]**2+aa[x6]**2+aa[x7]**2+aa[x8]**2)**0.5)*((ff[0]**2+ff[1]**2+ff[2]**2+ff[3]**2+ff[4]**2+ff[5]**2+ff[6]**2+ff[7]**2)**0.5))
                       #similarity=round(similarity,4)
                       similaritylist.append(similarity)#list all similarity value , all adultID's 8 Gdis similarity  with the reference adultID, included the reference adultID itself
                    
                    similaritylist.remove(max(similaritylist))# the adultID itself similarity vaule will be 1, remove from the list, the max of rest value will be the most similar of other ID
                    
                    h=max(similaritylist)
                # the most similar other ID cossim has to compare with referenced ID other 3 experssion similarity
                cossim=max(h,similarityAB,similarityAC,similarityAD)
                if cossim==similarityAB or similarityAC or similarityAD:
                    ID= adultID# if cossim value equal one of referenced ID other 3 expression, the ID will be the reference ID itself
                if cossim== h :# if cossim value is the other ID similarity value h, will try to get index of other ID in the similaritylist
                    index=similaritylist.index(h)# because the current similaritylist has been removed the referenced ID value
                    
                    if (index*32+1)< idlist.index(adultID):# if the reference ID is advanced than "other ID",the index of "other ID" in idlist willbe its index in similaritylist time 32
                        newindex=index*32+1
                    else:
                        newindex=(1+index)*32+1# if the reference ID is after "other ID", the "otehr ID" index in idlist will be its index in similaritylist times 32 add 1
                    ID= idlist[newindex]# make sure the ID output is uppercase
                return ID,round(cossim,4)
        except:#If any error for FR , it will return empty string for ID , and zero for cossim
            return "",0
            
                                   
   
   
#This function OP11 :A big list of small lists containing the minimum (non-zero) and maximum GDis and LDis of each distance across the four expressions.
def OP11(adultID,idlist,distancelist, Gdislist,Ldislist,distance):
   
    a_gdis_list = []#creat a empty list 
    for j in range (1,len(idlist)):#when input adultID and distance could locate the Gdis vaule in Gdislist
        if idlist[j]==str(adultID) and distancelist[j]==str(distance):#the Gdis vaule index in Gdislist same with the input ID in idlist
            a_gdis_list.append(float(Gdislist[j]))#append all 4 vaule of one expression into  list a_gdis_list
            a_gdis=round(min( a_gdis_list),4)# get the minimumGDis from the a_gdis_list
            b_gdis=round(max( a_gdis_list),4)# get the maxmumGDis from the a_gdis_list
   
    c_ldis_list = []
    for k in range (1,len(idlist)):
        if idlist[k]==str(adultID) and distancelist[k]==str(distance):
            c_ldis_list.append(float(Ldislist[k]))
            c_ldis=round(min( c_ldis_list),4)#get the minimumLDis from the c_ldis_list
            d_ldis=round(max( c_ldis_list),4)#get the maxmumLDis from the c_ldis_list
   
    list_e= [a_gdis,b_gdis,c_ldis,d_ldis]# create a new list list_e, which included all 4 value
    return list_e

# This function OP22:A list of lists containing the difference between the geodesic and 3D Euclidean distances for each expression
def OP22(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist,distance):
    
    for i in range (1,len(idlist)):
        if idlist[i]==str(adultID) and distancelist[i]==str(distance):
            if expressionlist[i]=="neutral":#calculate the difference when expression= Neutral,index=i
                difference1=float(Gdislist[i])-float(Ldislist[i])
            elif expressionlist[i]=="angry":#calculate the difference when expression= Angry,index=i
                difference2=float(Gdislist[i])-float(Ldislist[i])
            elif expressionlist[i]=="disgust":#calculate the difference when expression= Disgust,index=i
                difference3=float(Gdislist[i])-float(Ldislist[i])
            elif expressionlist[i]=="happy":#calculate the difference when expression= Happy,index=i
                difference4=float(Gdislist[i])-float(Ldislist[i])
    return round(difference1,4), round(difference2,4), round(difference3,4), round(difference4,4)# round all difference to 4 decimal places

# This function OP33:Average geodesic distance of the eight distances across the four expressions
def OP33(adultID,idlist,distancelist, Gdislist,distance):
    a_gdis_list = []
    for p in range (1,len(idlist)):
        if idlist[p]==str(adultID) and distancelist[p]==str(distance):
            a_gdis_list.append(float(Gdislist[p]))
            
    average_gdis=sum(a_gdis_list)/4# the average equal to sum 4 expression value of one distance divide 4
    return round(average_gdis,4) #round amount to 4 decimal places

# This function OP44: A list containing the standard deviation of the 3D Euclidean distance of the eight distances across the four expressions.
def OP44(adultID,idlist,distancelist, Ldislist,distance):
    c_ldis_list = []
    for p in range (1,len(idlist)):
        if idlist[p]==str(adultID) and distancelist[p]==str(distance):
            c_ldis_list.append(float(Ldislist[p]))#list Ldis value of 4 expression for same adultID same distance which index=p.After append,this list will have 4 value
    
    mean=sum(c_ldis_list)/4
    # using formula to calculate the standard deviation
    std_dev=(((c_ldis_list[0]-mean)**2+(c_ldis_list[1]-mean)**2+(c_ldis_list[2]-mean)**2+(c_ldis_list[3]-mean)**2)/4)**0.5
    
    return round(std_dev,4)


#This function A is to make a Gdis list for given ID and espression is Neutral
def A(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
    a=[]# make an empty list a

    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="neutral":
             a.append(float(Gdislist[i]))#store data into a for given ID,expression= Neutral,which have 8 Gdis value for distance 1-8
    
    return a
#This function A1 is to make a distance list for given ID when its expression is neutral
def A1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
   
    a1=[]#make a new distance list for given ID, expression = Neutral  ,which will have 8 distance text
    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="neutral":
          
             a1.append(distancelist[i])
    return a1

#This function B is to make a Gdis list for given ID and espression is Angry
def B(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
    b=[]
  
    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="angry":
             b.append(float(Gdislist[i]))#store data into b for given ID,expression= Angry,which have 8 Gdis value for distance 1-8
         
    return b
#This function B1 is to make a distance list for given ID when its expression is angry
def B1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
 
    b1=[] #make a new distance list for given ID, expression = Angry  ,which will have 8 distance text
    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="angry":
            
             b1.append(distancelist[i])
    return b1
#This function C is to make a Gdis list for given ID and espression is disgust
def C(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
    c=[]
   
    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="disgust":
             c.append(float(Gdislist[i]))#store data into c for given ID,expression= Disgust,which have 8 Gdis value for distance 1-8
           
    return c
#This function C1 is to make a distance list for given ID when its expression is disgust
def C1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
 
    c1=[]# make a new distance list for given ID, expression = Disgust ,which will have 8 distance text
    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="disgust":
          
             c1.append(distancelist[i])
    return c1

#This function D is to make a Gdis list for given ID and espression is Happy
def D(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
    d=[]
   
    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="happy":
             d.append(float(Gdislist[i]))#store data into d for given ID,expression= Happy,which have 8 Gdis value for distance 1-8
           
    return d
#This function D1 is to make a distance list for given ID when its expression is Happy
def D1(adultID,idlist,expressionlist,distancelist,Gdislist,Ldislist):
  
    d1=[]# make a new distance list for given ID, expression = Happy ,which will have 8 distance text
    for  i in range (1,len(idlist)):
         if idlist[i]==str(adultID) and expressionlist[i]=="happy":
                        d1.append(distancelist[i])
    return d1

def E(adultID,idlist,expressionlist,Gdislist,distancelist,distance):
    e=[]
    for  i in range (1,len(idlist)):
         if expressionlist[i]=="neutral" and distancelist[i]==str(distance):
             e.append(float(Gdislist[i]))# store data into e for all ID, expression = Nuetral， 8 distance value
    return e


