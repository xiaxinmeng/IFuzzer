
import xml.etree.ElementTree as ElementTree

xml_text = """
<ns0:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/"><ns0:Body><ns0:Fault><faultcode>a:ActionNotSupported</faultcode><faultstring xml:lang="en-US">The message with Action \'\' cannot be processed at the receiver, due to a ContractFilter mismatch at the EndpointDispatcher. This may be because of either a contract mismatch (mismatched Actions between sender and receiver) or a binding/security mismatch between the sender and the receiver.  Check that sender and receiver have the same contract and the same binding (including security requirements, e.g. Message, Transport, None).</faultstring></ns0:Fault></ns0:Body></ns0:Envelope>
"""

xml = ElementTree.fromstring(xml_text)
ele = xml.find('faultstring')
ele == None #True
