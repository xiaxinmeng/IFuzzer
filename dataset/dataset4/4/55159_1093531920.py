import xmlrpc.client
import xml.etree

server = xmlrpc.client.ServerProxy('http://ws.audioscrobbler.com/2.0/')
parameters = {'api_key': 'b25b959554ed76058ac220b7b2e0a026', 'user': 'joanofarctan', 'page': 1}

tracks = server.library.getTracks(parameters)
tracks_xml = xml.etree.ElementTree.parse(tracks)