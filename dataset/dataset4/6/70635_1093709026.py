code = bytes (
	chr(opmap["JUMP_FORWARD"]) + chr(0) + chr(255) + 
	chr(EXTENDED_ARG) + chr(1) + chr(1) + 
	chr(opmap["JUMP_FORWARD"]) + chr(0) + chr(0) +
	chr(EXTENDED_ARG) + chr(1) + chr(0) +
	chr(opmap["JUMP_ABSOLUTE"]) + chr(0) + chr(1) +
	chr(opmap["RETURN_VALUE"]),
	encoding="latin-1"
	)