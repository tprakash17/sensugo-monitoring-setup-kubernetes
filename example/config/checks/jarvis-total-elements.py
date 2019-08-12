#!/usr/local/bin/python3.7
 
## Importing dependent python libraries
import json
import requests
 
## Import existing python library to format the output into graphite_db format.
from sensu_plugin import SensuPluginMetricGraphite
 
class MyGraphiteMetric (SensuPluginMetricGraphite):
 
## Define functional logic
    def run(self):
 
        auth_token='******'
        hed = {'Authorization': 'Bearer ' + auth_token}
 
        url = 'https://jarvis-integration.mediaiqdigital.com/miq/api/de-geo-country/'
        res = requests.get(url, headers=hed) ## Get method using requests
 
        ## Read totalElements from JSON response
        totalElements = res.json()['totalElements']
 
        if totalElements > 0
            self.ok('JarvisCampaignOk', totalElements) ## default method (class SensuPluginMetricGraphite) being used to send metrics to influxDB in GraphitDB format.
        else
            self.ok('JarvisCampaignOk', totalElements)
 
if __name__ == "__main__":
    metric = MyGraphiteMetric()
