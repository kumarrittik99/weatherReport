import re
import urllib.request
from urllib.request import Request

url = "https://www.google.co.in/search?q=weather+report+"

try:
 city = input("Enter the name of the city.\n")
 url = url + city

 newUrl = Request(url,headers={"User-Agent":"Mozilla/5.0"})
 dataInByte = urllib.request.urlopen(newUrl).read()
 actualData = dataInByte.decode("utf-8")

#print(actualData)

 t = re.search('<span class="wob_t" style="display:inline">',actualData)
 print("Temperature of "+city+": "+actualData[t.start()+43:t.end()+4])


#<td style="white-space:nowrap;padding-right:0px;vertical-align:top;color:#666">Humidity: 82%</td>

 h = re.search('<td style="white-space:nowrap;padding-right:0px;vertical-align:top;color:#666">',actualData)
 print(actualData[h.start()+79:h.start()+92])

#at <span class="wob_t" style="display:inline">11 km/h

 w = re.search('at <span class="wob_t" style="display:inline">',actualData)
 print("Wind Speed: "+actualData[w.start()+46:w.start()+53])

except:
  print("Enter a valid city name!!! Program is unable to find the mentioned city.")
