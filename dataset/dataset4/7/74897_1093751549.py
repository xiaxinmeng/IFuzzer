#Working code:
from struct import *
rawdata = 'A'*196
laserdata = list(unpack('2s2s29H',rawdata[14:76]))
laserdata += list(unpack('26f3L4s',rawdata[76:196]))					

#This code generates error:
from struct import *
rawdata = 'A'*196
laserdata = list(unpack('2s2s29H26f3L4s',rawdata[14:196]))
# Does not work due to python bug: unpack calculates wrong size 184 (should be 182) from format string and generates error: 