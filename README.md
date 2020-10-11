# GBF Packet Sniffer
 A workspace to sniff GBF packets for analysis.
 current solutions like cypher are chrome extensions which are technically against ToS.
 This project's goal it to get similar parsing results through packet sniffing to comply with ToS.

## Collecting Data
GBF battle data is both gzipped and probably fragmented. Because of this, it is difficult to retrieve and decode the battle data from packet sniffing with tools like wireshark. The data is properly grouped and decoded in sessions so the information will be retrieve using fiddler4 and fiddler script.

## Data Parsing
A sample of the typical attack reponse can be found in samples (attack_response.txt). More sample response bodies will be needed inorder to handle all types of responses
Potential solution to parsing is to send a post request to a locally hosted api using [FiddlerApplication.oProxy.SendRequest()](https://docs.telerik.com/fiddlercore/api/fiddler.proxy#collapsible-Fiddler_Proxy_SendRequest_Fiddler_HTTPRequestHeaders_System_Byte___System_Collections_Specialized_StringDictionary_). That way, any language can be used instead of staying on fiddler for processing.