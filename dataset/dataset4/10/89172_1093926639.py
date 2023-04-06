
root_dir = "/dbfs/mnt/ADLS1/LANDING/parent"

def get_directories(root_dir):

    for child in Path(root_dir).iterdir():

        if child.is_file():
            print(child, datetime.fromtimestamp(getmtime(child)).date())
      
        else:
            print(child, datetime.fromtimestamp(getmtime(child)).date())
            get_directories(child)
