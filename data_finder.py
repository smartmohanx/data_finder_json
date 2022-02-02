import json 

database = "prize.json"

file = open(database).read()

data = json.loads(file)


print("""
1.Search a Nobel prize winner by name?
2.Find out Nobel prize winner in a year input by him?
3.Search Prize winner based on the year and  category?
4.Show a list of all winners in alphabetical order with year and category?
""")

inputx = input("choose 1/2/3/4:")
if inputx == '1':
    print("Search a Nobel prize winner by name?")

    byName = input("Enter name:")

    lis = []

    for i in data['prizes']:
        laureates = i['laureates']

        for j in i['laureates']:
            name = j['firstname'] + " " + j['surname']
            lis.append(name)
    count = 0
    for i in lis:
        if i == byName:
            print("data found: "+ byName)
            count = 1
            break
    if count == 0:
        print("Not found!")

elif inputx == '2':
    print("Find out Nobel prize winner in a year input by him?")
    byName = input("Enter name:")

    for i in data['prizes']:
        year = i['year']
        laureates = i['laureates']

        for j in i['laureates']:
            name = j['firstname'] + " " + j['surname']
            if name == byName:
                print(byName + " received in " + year)

elif inputx == '3':
    print("Search Prize winner based on the year and  category?")
    byYear = input("enter year:")
    byCategory = input("enter category:")

    for i in data['prizes']:
        year = i['year']
        category = i['category']
        laureates = i['laureates']

        if byYear == year and byCategory == category:
            for j in i['laureates']:
                name = j['firstname'] + " " + j['surname']
                print(name)
 
elif inputx == '4':
    print("Show a list of all winners in alphabetical order(with year and category.")

    lis = []

    for i in data['prizes']:
        year = i['year']
        category = i['category']
        laureates = i['laureates']
            
        for j in i['laureates']:
            all_winner = j['firstname'] + " " + j['surname'] + " received in " + category + " in " + year
            lis.append(all_winner)
    lis.sort()
    print(lis)

else:
    print("Please enter a proper digit! 1/2/3/4.")
