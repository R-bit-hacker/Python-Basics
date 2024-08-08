population={'China':143,
            'India':136,
            'USA':32,
            'Pakistan':21}
def printdic():
    for country, pop in population.items():
        print (country,"==>",pop)
def add_country():
    addc=input("Enter country name you want to add: ")
    if addc in population:
        print("---Country already Exists---")
    else:
        addp=int(input("Enter population for this new country: "))
        population[addc]=addp
        printdic()
def remove_country():
    remc=input("Enter country name you want to remove: ")
    if remc in population:
        population.pop(remc)
        printdic()
    else:
        print("Country does not exist in dictionary!!")
def query_country():
    queryc=input("Enter country name for population: ")
    print(population.get(queryc, "Country does not exist!!"))

def main():
    inp=input("Enter input i.e;\na) print: for printing dictionary\nb)add: for adding new country\nc)remove: for removing existing country\nd)query: for population of specific country\n")
    if inp=='print':
        printdic()
    elif inp=='add':
        add_country()
    elif inp=='remove':
        remove_country()
    elif inp=='query':
        query_country()
    else:
        print("Invalid Input")

if __name__=="__main__":
    main()