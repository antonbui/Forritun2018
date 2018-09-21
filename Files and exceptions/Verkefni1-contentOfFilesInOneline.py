with open("test.txt", "r") as testfile:
    testfile = testfile.read()
    testfile = testfile.replace(" ", "")
    testfile = testfile.replace("\n", "")
    
print(testfile)

