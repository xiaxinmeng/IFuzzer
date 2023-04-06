def sendFiles(request): 
    fileName = request.GET['fileName']

    pathToFile = os.path.join(filesDir, fileName)
    response = FileResponse(open(pathToFile, 'rb'))