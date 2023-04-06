class html_patch(HTMLParser.HTMLParser):
    # Internal -- sets the proper tag terminator based on cdata element type
    def set_cdata_mode(self, tag):
        #We check if the script is either a style or a script
        #based on self.CDATA_CONTENT_ELEMENTS
        if tag=="style":
            self.interesting = endtagfind_style
        elif tag=="script":
            self.interesting = endtagfind_script
        else:
            self.error("Unknown cdata type:"+tag) # should never happen
        self.cdata_tag = tag 