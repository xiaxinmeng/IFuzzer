class Folders:
    def __init__(self, path, parent_folder_name):
        self.path = path + parent_folder_name + '\\'
        self.parent_folder_name = parent_folder_name

    def showFolders(self):
        folders = [lst.lstrip(self.path) for lst in  g.glob(self.path + '*')]
        print('Path: '+self.path+ ', List: ',folders)
    pass

if __name__ == "__main__":
	obj = Folders(path='.\\', parent_folder_name='parent')
	obj.showFolders()