#!/usr/bin/env python

import urllib
#import urllib.request

#import urllib2

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError


import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

#start
#@app.route('/webhook', methods=['POST'])
#def webhook():
 #   req = request.get_json(silent=True, force=True)
 #   print("Request:")
 #  print(json.dumps(req, indent=4))

 #   res = makeWebhookResult(req)

 #   res = json.dumps(res, indent=4)
  #  print(res)
 #   r = make_response(res)
  #  r.headers['Content-Type'] = 'application/json'
   # return r

#def makeWebhookResult(req):
 #   if req.get("result").get("action") != "property_search":
  #      return {}
   # result = req.get("result")
    #parameters = result.get("parameters")
    #zone = parameters.get("city")
    #cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':400, 'islamabad':500}
    
	
   
    #speech = "The cost of shipping to " + zone + " is " + str(cost[zone]) +" euros. "

    #print("Response:")
#end comment

intent_name="string"
QR=['0','1','2','3','4','5','6','7']

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
#azqa










def processRequest(req):
    if req.get("result").get("action") != "property_search":
        return {}
    global city_names
    city_names=processlocation(req)
    global QR
    global intent_name
    intent_name=processIntentName(req)
    if "search_property" in intent_name:        
        QR[0]="Sector in "+city_names
        QR[1]="Other City?Specify"
        QR[2]="(Y)"
        QR[3]="Hot Property"
        QR[4]="Price Range"
        QR[5]="Land Area"
        QR[6]="Property Type"
   
    city_names=processlocation(req)
    property_type=processPropertyType(req)
    maximum_value=processMaximum(req)

   # project_name=processProjectName(req)
    #if minimum_value > maximum_value:
    #    minimum_value,maximum_value=maximum_value,minimum_value
    #else:
    # minimum_value,maximum_value=minimum_value,maximum_value    
    #baseurl = "https://aarz.pk/bot/index.php?city_name="+city_names+"&sector_name="+sector_names+"&minPrice="+maximum_value+"&type="+property_type+"&LatestProperties="+latest+"&UnitArea="+area_property+"&Unit="+unit_property+"&school="+school+"&airport="+airport+"&transport="+transport+"&security="+security+"&shopping_mall="+malls+"&fuel="+fuel
    #baseurl="https://www.aarz.pk/search/bot?postedBy=searchPage&view=&city_s="+city_names+"&price_min="+maximum_value+"&price_max=0estate_agent=&purpose=Sell&property_type="+property_type
    
#try:  
    baseurl="https://www.aarz.pk/search/bot?postedBy=searchPage&view=&city_s=city_names"

    result = urllib.request.urlopen(baseurl).read()
    #except HTTPError as e:
    #content = e.read()
    #print(content)
    print(result)
    data = json.loads(result)
    res = makeWebhookResult(data)
    return data



 
    #req = urllib2.Request(baseurl)
    #req.add_header('Accept', 'application/json')
    #result= urllib2.urlopen(baseurl).read()
    #data = json.loads(result)
    #res = makeWebhookResult(data)
    #return res
 

def processIntentName(req):
    result = req.get("result")
    parameters = result.get("metadata")
    intent = parameters.get("intentName")
    return intent

def processlocation(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("city")
    return city


def processMaximum(req):
    result = req.get("result")
    parameters = result.get("parameters")
    maximum = parameters.get("PriceRange")
    return maximum


def processPropertyType(req):
    result = req.get("result")
    parameters = result.get("parameters")
    propertyType = parameters.get("PropertyType")
    return propertyType


def processProjectName(req):
    result = req.get("result")
    parameters = result.get("parameters")
    project_name = parameters.get("ProjectName")
    return project_name 





def makeWebhookResult(data):
    i=0
    length=len(data)
    varibale1='344'
    variable2='322'
    variable3='4332'
    variable4='4321'
    row_id=['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
    row_title=['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
    row_location=['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
    row_price=['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
    row_slug=['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
    row_number=['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
    row_image=['test','test1','test2','test3','test4','test5','test6','test7','test8','test9','test10']
    while (i <length):
        row_id[i]=data[i]['property_id']
        row_title[i]=data[i]['title']
        row_location[i]=data[i]['address']
        row_price[i]=data[i]['price']
        row_slug[i]=data[i]['slug']
        row_number[i]=data[i]['number']
        row_image[i]=data[i]['image']
        i+=1
    variable1=str(row_number[0])
    variable2=str(row_number[1])
    variable3=str(row_number[2])
    variable4=str(row_number[3]) 
    
    speech = "Here are some properties with your choice: https://www.aarz.pk/property-detail/"+row_slug[0] + " https://www.aarz.pk/property-detail/"+row_slug[1] +" Type: 'Hot Property','Price Range','Land Area','Change Location','Buy Property' "
    if "unable" in row_title[0]:
        message={
         "text":row_title[0],
         "quick_replies": [
           
                 {
                "content_type":"text",
                "title": "Buy Property",
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            }
        ]
           
    }
    elif length==1:
                 message={
                   "attachment":{
                    "type":"template",
                       "payload":{
            "template_type":"generic",
            "elements":[
          {
             "title":row_title[0],
                "item_url": "https://www.aarz.pk/property-detail/"+row_slug[0],               
               "image_url":"https://www.aarz.pk/"+row_image[0] ,
             "subtitle":row_location[0],
             "buttons":[
              {
              "type":"phone_number",
              "title":"Call Agent",
              "payload":"+92"+variable1[1:]
              },
                 {
                "type":"element_share"
                  }
            ]
          }
        ]
      }
    },
                      "quick_replies": [
            {
                "content_type":"text",
                "title": QR[0],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[1],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[2],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[3],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[4],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[5],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                  {
                "content_type":"text",
                "title": QR[6],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": "Buy Property",
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            }
        ]
  }
    elif length==2:
         message= {
         "attachment": {
           "type": "template",
            "payload": {
               "template_type": "generic",
               "elements": [{
               "title": row_title[0],
               "subtitle": row_location[0],
                "item_url": "https://www.aarz.pk/property-detail/"+row_slug[0],               
               "image_url":"https://www.aarz.pk/"+row_image[0]  ,
                "buttons": [{
                "type":"phone_number",
              "title":"Call Agent",
             "payload":"+92"+variable1[1:]
                },
                    {
                "type":"element_share"
                    
                    }, 
                   ],
          }, 
                   {
                "title": row_title[1],
                "subtitle": row_location[1],
                 "item_url": "https://www.aarz.pk/property-detail/"+row_slug[1],               
               "image_url":"https://www.aarz.pk/"+row_image[1]  ,
                "buttons": [{
                "type":"phone_number",
              "title":"Call Agent",
             "payload":"+92"+variable2[1:]
            },
                     {
                "type":"element_share"
                    
                    }, 
                   ]
          }]
            
        }
      },
             "quick_replies": [
            {
                "content_type":"text",
                "title": QR[0],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[1],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[2],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[3],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[4],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                  {
                "content_type":"text",
                "title": QR[5],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                  {
                "content_type":"text",
                "title": QR[6],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": "Buy Property",
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            }
        ]
    }
    else:
         message= {
         "attachment": {
           "type": "template",
            "payload": {
               "template_type": "generic",
               "elements": [
                   {
               "title": row_title[0],
               "subtitle": row_location[0],
                "item_url": "https://www.aarz.pk/property-detail/"+row_slug[0],               
               "image_url":"https://www.aarz.pk/"+row_image[0]  ,
                "buttons": [{
                "type":"phone_number",
              "title":"Call Agent",
              "payload":"+92"+variable1[1:]
                },
                    {
                "type":"element_share"
                  
            }, 
                   ],
          }, 
                   {
               "title": row_title[1],
               "subtitle": row_location[1],
                "item_url": "https://www.aarz.pk/property-detail/"+row_slug[1],               
               "image_url":"https://www.aarz.pk/"+row_image[1]  ,
                "buttons": [{
                "type":"phone_number",
              "title":"Call Agent",
              "payload":"+92"+variable2[1:]
            }, 
                     {
                "type":"element_share"
                    
                    }, 
                   ],
          }, 
                   {
               "title": row_title[2],
               "subtitle": row_location[2],
                "item_url": "https://www.aarz.pk/property-detail/"+row_slug[2],               
               "image_url":"https://www.aarz.pk/"+row_image[2]  ,
                "buttons": [{
               "type":"phone_number",
              "title":"Call Agent",
              "payload":"+92"+variable3[1:]
            }, 
                     {
                "type":"element_share"
                    
                    }, 
                   ],
          }, 
                   {
                "title": row_title[3],
                "subtitle": row_location[3],
                 "item_url": "https://www.aarz.pk/property-detail/"+row_slug[3],               
               "image_url":"https://www.aarz.pk/"+row_image[3]  ,
                "buttons": [{
               "type":"phone_number",
              "title":"Call Agent",
              "payload":"+92"+variable4[1:]
            },
                     {
                "type":"element_share"
                    
                    }, 
                   ]
          }]
            
        }
      },
             "quick_replies": [
            {
                "content_type":"text",
                "title": QR[0],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[1],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[2],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[3],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": QR[4],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                  {
                "content_type":"text",
                "title": QR[5],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                  {
                "content_type":"text",
                "title": QR[6],
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            },
                 {
                "content_type":"text",
                "title": "Buy Property",
                "payload": "YOUR_DEFINED_PAYLOAD_FOR_NEXT_IMAGE"
            }
        ]
    }
            

#//////////
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "data": {},
        "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }



if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
