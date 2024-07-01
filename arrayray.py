import csv
import hierarchial_ad

data =hierarchial_ad.sorted_dclusters

#print(x,y)
rows=[]
with open('trimmed2.csv', 'r') as csv_file:
    
    # csv_reader = csv.reader(csv_file)
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    rows = list(reader)[1:] #skip header row


def best_and_worst_website():# Returns best and worst websites
    firstKey = data[0] 
    lastKey = data[list(data.keys())[-1]]
    best=[]
    worst=[]
    if type(firstKey) == list:  
        for i in firstKey:
            best.append(rows[i])#best row
    else:
        best.append(rows[firstKey])
    
    if type(lastKey) == list:  
        for i in lastKey:
            worst.append(rows[i])#worst row
    else:
        worst.append(rows[lastKey])  

    return best,worst  
    #if()
    #print(rows[[data[6][0],data[6][1]][0]],rows[[data[6][0],data[6][1]][1]])#worst rows
best,worst=best_and_worst_website()

print(best,"\n",worst)


def param_grading(l): #Ranks a single website's parameters [GOOD,NEEDS IMPROVEMENT,POOR]
    
    print("Parameter Grading for" ,str(l[0]))
    l[0]=0
    l=list(map(float, l))
    if float(l[1])<=1.8:#FCP 
        print("Your First Contentful score is Good")
    elif l[1]<3:
        print("Your First Contentful score needs improvement")
    else:
        print("Your First Contentful score is Poor")

    if l[2]<=3.8:#FI 
        print("Your FirstInteractive score is Good")
    elif l[2]<=7.3:
        print("Your FirstInteractive score needs improvement")
    else:
        print("Your FirstInteractive score is Poor")

    if l[3]<=2.5: #LCP
        print("Your LargestContentfulPaint score is Good")
    elif l[3]<=4:
        print("Your LargestContentfulPaint score needs improvement")
    else:
        print("Your LargestContentfulPaint score is Poor")

    if l[4]<=3.4: #SI
        print("Your SpeedIndex score is Good")
    elif l[4]<=5.8:
        print("Your SpeedIndex score needs improvement")
    else:
        print("Your SpeedIndex score is Poor")

    if l[5]<=0.1: #CLS 
        print("Your Cumulative Layout Shift score is Good")
    elif l[5]<=0.25:
        print("Your Cumulative Layout Shift score needs improvement")
    else:
        print("Your Cumulative Layout Shift score is Poor")

    if l[6]<=2: #FMP 
        print("Your First Meaningful Paint score is Good")
    elif l[6]<=4:
        print("Your First Meaningful Paint score needs improvement")
    else:
        print("Your First Meaningful Paint score is Poor")    
    
    if l[7]<=200:#TBT 
        print("Your Total Blocking Time score is Good")
    elif l[7]<=600:
        print("Your Total Blocking Time score needs improvement")
    else:
        print("Your Total Blocking Time score is Poor")
    
    if l[8]<=130: #Max FID
        print("Your First Input Delay score is Good")
    elif l[8]<250:
        print("Your First Input Delay score needs improvement")
    else:
        print("Your First Input Delay score is Poor")

param_grading(rows[0]) # Pass entire row as argument

def parameter_comparasion():
    #fcp=[],fi=[],lcp=[],si=[],cls=[],fmp=[],tbt=[],mpfid=[]
    id, fcp, fi, lcp, si, cls, fmp, tbt, mpfid = list(), list(), list(), list(), list(), list(), list(), list(), list()

    with open("trimmed2.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)[1:] #skip header row
        for x in rows:
            id.append(str(x[0]))
            fcp.append(x[1])
            fi.append(x[2])
            lcp.append(x[3])
            si.append(x[4])
            cls.append(x[5])
            fmp.append(x[6])
            tbt.append(x[7])
            mpfid.append(x[8])
    return id,fcp,fi,lcp,si,cls,fmp,tbt,mpfid        

id ,fcp, fi, lcp, si, cls, fmp, tbt, mpfid=parameter_comparasion()
print(id ,fcp, fi, lcp, si, cls, fmp, tbt, mpfid)



#Insights for your website compared with best and worst values for paramaters
customer_website=rows[0]
print(customer_website[1],max(fcp),min(fcp))
print(customer_website[2],max(fi),min(fi))
print(customer_website[3],max(lcp),min(lcp))
print(customer_website[4],max(si),min(si))
print(customer_website[5],max(cls),min(cls))
print(customer_website[6],max(fmp),min(fmp))
print(customer_website[7],max(tbt),min(tbt))
print(customer_website[8],max(mpfid),min(mpfid))


# comparing params to state whose is best or worst

# 
#URL,FirstContentfulPaint,FirstInteractive,LargestContentfulPaint,SpeedIndex,CumulativeLayoutShift,FisrtMeaningfulPaint,TotalBlockingTime,MaxPotentialFID
# https://www.bungie.net/7,1.4,1.6,2.7,2.5,0.004,1.4,40,160
# https://pccegoa.edu.in/,1.3,7.8,1.7,4.3,0.392,2.0,170,120
# https://dbcegoa.ac.in/,0.8,0.8,2.0,3.2,0.687,0.8,0,50
# https://aitdgoa.edu.in/,1.1,5.1,1.6,3.6,0.002,1.1,70,100
# https://paruluniversity.ac.in/,1.1,3.2,2.6,3.1,0.001,1.1,120,100

#individual parameter comparasion alomg with best and worst and parameters for all 