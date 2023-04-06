
with open("file1") as file1:
    assert file1.read() == "data1"

with open("file2") as file2:
    assert file2.read() == "data2"
