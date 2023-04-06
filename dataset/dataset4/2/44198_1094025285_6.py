def CheckServerVersion():
    # Checking for server build
    if GetServerBuild() < MIN_SERVER_BUILD:
        printLog( "YOU ARE TRYING TO RUN PYTHON SCRIPTS ON OUTDATED SERVER BUILD!\
\nREQUIRED SERVER BUILD: %s\
\nPlease Update your server core before running server!\
\nScripting Engine will be Shut Down!"\
        % (MIN_SERVER_BUILD), PRINT_ERROR )

        killScripting()
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
def GetScriptsVersion():
	return SCRIPTS_VERSION