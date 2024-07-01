import requests
import json

# Set the API endpoint URLs
pagespeed_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
backlinks_url = "https://api.majestic.com/api/json"
script_url = "https://sonarwhal.com/scanner/"

# Set the webpage to analyze
webpage_url = "https://www.example.com"

# Set the API keys
#pagespeed_api_key = "YOUR_PAGESPEED_API_KEY_HERE"
#backlinks_api_key = "YOUR_BACKLINKS_API_KEY_HERE"

# Set the parameters for the PageSpeed Insights API request
pagespeed_params = {
    "url": webpage_url,
    "strategy": "mobile", # or "desktop"
    #"key": pagespeed_api_key # optional
}

# Send the PageSpeed Insights API request and retrieve the response
pagespeed_response = requests.get(pagespeed_url, params=pagespeed_params)
pagespeed_data = json.loads(pagespeed_response.text)

# Print the PageSpeed Insights data analytics
print("Webpage URL:", pagespeed_data['lighthouseResult']['finalUrl'])
print("Performance Score:", pagespeed_data['lighthouseResult']['categories']['performance']['score'])
print("First Contentful Paint (FCP) time (ms):", pagespeed_data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['percentile'])
#print("Speed Index (SI) time (ms):", pagespeed_data['loadingExperience']['metrics']['SPEED_INDEX']['percentile'])

# Set the parameters for the backlinks API request
backlinks_params = {
   # "app_api_key": backlinks_api_key,
    "cmd": "GetBackLinkData",
    "item": webpage_url,
    "datasource": "fresh"
}

# Send the backlinks API request and retrieve the response
backlinks_response = requests.get(backlinks_url, params=backlinks_params)
backlinks_data = json.loads(backlinks_response.text)

# Print the backlinks data
print("Backlinks Data:")
print("Total Backlinks:", backlinks_data['DataTables']['BackLinks']['TotalBackLinks'])
print("Referring Domains:", backlinks_data['DataTables']['BackLinks']['RefDomains'])

# Send a request to analyze the script that runs on the webpage
script_response = requests.post(script_url, json={'url': webpage_url})
script_data = json.loads(script_response.text)

# Print the script analysis data
print("Script Analysis Data:")
print("Total Issues Found:", len(script_data['issues']))
for issue in script_data['issues']:
    print("Issue Type:", issue['ruleId'])
    print("Description:", issue['message'])
    print("Details:", issue['description'], "\n")
