from pymongo import MongoClient
myclient = MongoClient("mongodb+srv://mongodb+srv://tonte:xlr8@cluster0.6wtya.mongodb.net/test?")

mydb = myclient["out_of_school_children"]

mycol = mydb ["out of school children 2015"]

while True:
    print("                                       ")
    print("FETEPIGI AYEBATONTE 17CJ022495 CEN414")
    print("Out of School Children")
    print ("Search for Out of School Children population:")
    deinput = input()
    search = deinput.upper()
    myquery = { "State": search }



    mydoc = mycol.find(myquery)

    for x in mydoc:
        Y = str(x["Out of School Children"])
        print(search + " out of school children," + Y + " people")
        print("                                       ")
    res = input("Search Again Y/N:")
    if res == "N" or res == "n":
        break
    



