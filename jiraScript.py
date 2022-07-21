
import groovy.json.JsonOutput
final externalUrl = "https://api.tvmaze.com/"
// Turn the data will be sent into JSON, the HTTP requests specify in the header to accept application/JSON
// If the API accepts different types then you can change this and format the data accordingly

// The host URL will be the consistent prefix to every request is made. i.e: https://<YOUR API HOST URL>/
// The endpoint will be the specific API method to hit. i.e: /GetResults
// The query will be the variable parameter the endpoint will use to get the data. i.e: /objectId=1
// The body is the JSON version of the data that will be sent to an API, only used for PUT and POST
def getResponse = get(externalUrl, "search/shows?q=postman")

// If GET response is successful then the response can be cast to a Map which will allow to interact with the data
if (getResponse) {
    def responseGetMap = getResponse as Map
    // A code to manage the resulted data can be inserted here, i.e iterate results with responseMap.each{}
    responseGetMap.each {}
   
    // In this case, status is returned as delete HTTP method responds an empty body
    assert responseStatus == 200
}
def get(def getResponse) {
    // If the API is token-based authenticated, token can be specified into this variable
    get("$getResponse")
        .header('Accept', 'application/JSON')
    // The 'Authorization' header is added
        .asObject(Map)
        .body
}

