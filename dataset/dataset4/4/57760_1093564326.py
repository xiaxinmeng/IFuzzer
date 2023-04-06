class MyDOM(PullDOM):
    def startElement(self, name, attrs):
        PullDOM.startElement(self, name, attrs)
        if name[:3]=="my_":
            curNode = self.elementStack[-1]
            parentNode = self.elementStack[-2]
            parentNode.appendChild(curNode)