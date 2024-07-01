#!C:/Users/wwwfu/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\n")

import csv
import hierarchial_ad
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data =hierarchial_ad.sorted_dclusters

rows=[]
with open('trimmed.csv', 'r') as csv_file:
    
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    rows = list(reader)[1:] #skip header row

for row in rows:
    for i in range(len(row)):
        try:
            row[i] = float(row[i])
        except ValueError:
            pass


@app.route('/get_list')
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
    print(best,"\n",worst)
    
    # Call param_grading() and capture its output
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        param_grading(rows[0])
    grading_output = f.getvalue()
    
    # Return both the best and worst websites and the grading output
    return jsonify(best, worst, grading_output)


def param_grading(l): #Ranks a single website's parameters [GOOD,NEEDS IMPROVEMENT,POOR]
    
    print("Parameter Grading for" , l[0])
    for i in range(1, len(l)):
        try:
            l[i] = float(l[i])
        except ValueError:
            pass
    
    if l[1]<=1.8:#FCP 
        print("• Your First Contentful score is Good")
    elif l[1]<3:
        print("• Your First Contentful score needs improvement")
    else:
        print("• Your First Contentful score is Poor")

    if l[2]<=3.8:#FI 
        print("• Your FirstInteractive score is Good")
    elif l[2]<=7.3:
        print("• Your FirstInteractive score needs improvement")
    else:
        print("• Your FirstInteractive score is Poor")

    if l[3]<=2.5: #LCP
        print("• Your LargestContentfulPaint score is Good")
    elif l[3]<=4:
        print("• Your LargestContentfulPaint score needs improvement")
    else:
        print("• Your LargestContentfulPaint score is Poor")

    if l[4]<=3.4: #SI
        print("• Your SpeedIndex score is Good")
    elif l[4]<=5.8:
        print("• Your SpeedIndex score needs improvement")
    else:
        print("• Your SpeedIndex score is Poor")

    if l[5]<=0.1: #CLS 
        print("• Your Cumulative Layout Shift score is Good")
    elif l[5]<=0.25:
        print("• Your Cumulative Layout Shift score needs improvement")
    else:
        print("• Your Cumulative Layout Shift score is Poor")

    if l[6]<=2: #FMP 
        print("• Your First Meaningful Paint score is Good")
    elif l[6]<=4:
        print("• Your First Meaningful Paint score needs improvement")
    else:
        print("• Your First Meaningful Paint score is Poor")    
    
    if l[7]<=200:#TBT 
        print("• Your Total Blocking Time score is Good")
    elif l[7]<=600:
        print("• Your Total Blocking Time score needs improvement")
    else:
        print("• Your Total Blocking Time score is Poor")
    
    if l[8]<=130: #Max FID
        print("• Your First Input Delay score is Good")
    elif l[8]<250:
        print("• Your First Input Delay score needs improvement")
    else:
        print("• Your First Input Delay score is Poor")

param_grading(rows[0]) # Pass entire row as argument

#individual parameter comparasion alomg with best and worst and parameters for all 
if __name__ == "__main__":
    app.run(debug=True)
