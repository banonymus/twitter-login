import http.client,  urllib.parse, urllib.error, json

headers = {
    # Request headers
    'aade-user-id': 'banonymus',
    'Ocp-Apim-Subscription-Key': '215f387cbda24252939a408538621d71',
}

params = urllib.parse.urlencode({
    # Request parameters
    'mark': '400000020277972',
})

try:
    conn = http.client.HTTPSConnection('mydata-dev.azure-api.net')
    conn.request("GET", "/RequestTransmittedDocs?%s" % params, "{body}", headers)
    response = conn.getresponse()

    data = response.read()
    print(data)
    #print(data.decode('utf-8'))
    #res = json.loads(data.decode('utf-8'))
    # print(res)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
