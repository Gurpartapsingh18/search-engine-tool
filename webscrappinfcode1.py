from urllib.request import urlopen
fo=open("url.txt","r")
r=1
for i in fo.readlines():
    page=urlopen(i)
    #print(page.read())
    from bs4 import BeautifulSoup
    soup= BeautifulSoup(page,"html.parser")
    for script in soup(["script","style"]):
        script.extract()
    text=soup.get_text()
    #print(text)
    lines=(line.strip() for line in text.splitlines())
    l=[]
    l=text.split()
    #print(l)                                  #the text being converted to a list
    fo=open("ignore.txt","r")
    k=fo.read()
    p=k.split()
    #print(p)                                  #the list of ignored words which have to be removed/ignored from the text
    fo.close()
    flag=0
    q=[]
    for i in range(len(l)):
       flag=0
       for j in range(len(p)):
                       if(l[i]==p[j]):
                           flag=1
       if(flag==0):
          q.append(l[i])
      
    d={}

    #print(q)                                   #the new set of list which has been created excluding the ignored words
    for i in range(len(q)):
        a=q.count(q[i])
        d[q[i]]=a
    #print(d)                               #the initial dictionary of the words(unsorted)
    z={}    
    from operator import itemgetter

    for key,value in sorted(d.items(),key=itemgetter(1), reverse=True):
       # print(key,value)
        
         z[key]=value
    #print(z)                             #the 2nd dictionary which has been sorted 
    first5={k:z[k] for k in list(z)[:5]}  # the final dictionary which contains the final 5 keywords of a URL
    print("the keywords for the specific  site are" ,first5)

    import xlsxwriter
    
    seriesdata=[]
    valuedata=[]
    a1=list(first5.keys())
    b1=list(first5.values())
    if(r==1):
        
        workbook=xlsxwriter.Workbook("demo.xlsx")
        worksheet=workbook.add_worksheet()
        for i in range(len(a1)):
            seriesdata.append(a1[i])
            worksheet.write_column("A1",seriesdata)
        for j in range(len(b1)):
            valuedata.append(b1[j])
            worksheet.write_column("B1",valuedata)
            chart=workbook.add_chart({"type":"column"})
            chart.add_series({"values":"=Sheet1!$B$1:$B$5"})
            worksheet.insert_chart("C1",chart)
    workbook.close()
   
    if(r==2):
        
        workbook=xlsxwriter.Workbook("demo2.xlsx")
        worksheet=workbook.add_worksheet()
        for i in range(len(a1)):
            seriesdata.append(a1[i])
            worksheet.write_column("A1",seriesdata)
        for j in range(len(b1)):
            valuedata.append(b1[j])
            worksheet.write_column("B1",valuedata)
            chart=workbook.add_chart({"type":"column"})
            chart.add_series({"values":"=Sheet1!$B$1:$B$5"})
            worksheet.insert_chart("C1",chart)
    workbook.close()

    if(r==3):
        
        workbook=xlsxwriter.Workbook("demo3.xlsx")
        worksheet=workbook.add_worksheet()
        for i in range(len(a1)):
            seriesdata.append(a1[i])
            worksheet.write_column("A1",seriesdata)
        for j in range(len(b1)):
            valuedata.append(b1[j])
            worksheet.write_column("B1",valuedata)
            chart=workbook.add_chart({"type":"column"})
            chart.add_series({"values":"=Sheet1!$B$1:$B$5"})
            worksheet.insert_chart("C1",chart)
    workbook.close()
    r=r+1

    
               
              
         
