#!C:/Users/wwwfu/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\n")
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    # Your Python code here
    import requests

    # Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

    # JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

    # Populate 'pagespeed.txt' file with URLs to query against API.
    with open('./pagespeed.txt') as pagespeedurls:
        download_dir = 'pagespeed-results.csv'
        file = open(download_dir, 'w')
        content = pagespeedurls.readlines()
        content = [line.rstrip('\n') for line in content]

        columnTitleRow = "URL, First Contentful Paint, First Interactive, Largest Contentful Paint, Speed Index, Cumulative Layout Shift, Fisrt Meaningful Paint, Total Blocking Time, Max Potential FID"
        file.write(columnTitleRow)

        # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
        for line in content:
            # If no "strategy" parameter is included, the query by default returns desktop data.
            x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={line}&strategy=desktop'
            print(f'Requesting {x}...')
            r = requests.get(x)
            final = r.json()
            
            try:
                urlid = final['id']
                split = urlid.split('?') # This splits the absolute url from the api key parameter
                urlid = split[0] # This reassigns urlid to the absolute url
                ID = f'URL ~ {urlid}'
                ID2 = str(urlid)
                urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']  
                FCP = f'First Contentful Paint ~ {str(urlfcp)}'
                FCP2 = str(urlfcp)
                urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
                FI = f'First Interactive ~ {str(urlfi)}'
                FI2 = str(urlfi)
                urllcp = final['lighthouseResult']['audits']['largest-contentful-paint']['displayValue']
                LCP = f'Largest Contentful Paint ~ {str(urllcp)}'
                LCP2 = str(urllcp)
                urlsi = final['lighthouseResult']['audits']['speed-index']['displayValue']
                SI = f'Speed Index ~ {str(urlsi)}'
                SI2 = str(urlsi)
                urlcls = final['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']
                CLS = f'Cumulative Layout Shift ~ {str(urlcls)}'
                CLS2 = str(urlcls)
                urlfmp = final['lighthouseResult']['audits']['first-meaningful-paint']['displayValue']
                FMP = f'First Meaningful Paint ~ {str(urlfmp)}'
                FMP2 = str(urlfmp)
                urltbt = final['lighthouseResult']['audits']['total-blocking-time']['displayValue']
                TBT = f'Total Blocking Time~ {str(urltbt)}'
                TBT2 = str(urltbt).replace(',','')
                urlmpfid = final['lighthouseResult']['audits']['max-potential-fid']['displayValue']
                MPFID = f'Max Potential FID ~ {str(urlmpfid)}'
                MPFID2 = str(urlmpfid)

                # Remove non-breaking space character and comma, then convert milliseconds to seconds
                TBT_seconds = float(urltbt.replace('\xa0ms', '').replace(',', '')) / 1000
                TBT = f'Total Blocking Time ~ {TBT_seconds:.3f} seconds'
                TBT2 = str(TBT_seconds)

                MPFID_seconds = float(urlmpfid.replace('\xa0ms', '').replace(',', '')) / 1000
                MPFID = f'Max Potential FID ~ {MPFID_seconds:.3f} seconds'
                MPFID2 = str(MPFID_seconds)

            except KeyError:
                print(f'<KeyError> One or more keys not found {line}.')
            
            try:    
                row = f'\n{ID2},{FCP2},{FI2},{LCP2},{SI2},{CLS2},{FMP2},{TBT2},{MPFID2}'
                if row:
                    file.write(row)
            except NameError:
                print(f'<NameError> Failing because of KeyError {line}.')
                # file.write(f'\n')
            
            try:
                print(ID) 
                print(FCP)
                print(FI)
                print(LCP)
                print(SI)
                print(CLS)
                print(FMP)
                print(TBT)
                print(MPFID)
            except NameError:
                print(f'<NameError> Failing because of KeyError {line}.')

        file.close()


    
    def get_data(self, input_filename: str, output_filename: str):
        import csv
        with open(input_filename, 'r', newline='') as in_file, open(output_filename, 'w', newline='') as out_file:
            r = csv.reader(in_file, delimiter=',')
            w = csv.writer(out_file, delimiter=',')
            
            for line in r:
                trim = (field.replace(" ","").replace(" ms","").replace(" s","").replace("http:","").replace("https:","").replace("/","") for field in line)
                #trim2=(field[0].replace("http://","").replace("https://","").replace("/","") for field in trim)
                w.writerow(trim)
                
    input_filename = 'pagespeed-results.csv'
    output_filename = 'trimmed.csv'

    get_data(self='', input_filename=input_filename, output_filename=output_filename)

    # Return a response to the JavaScript
    response = {'message': 'Python code executed successfully.'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)