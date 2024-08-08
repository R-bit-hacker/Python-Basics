import statistics

price={'info':[600,630,620],'ril':[1430,1490,1567],'mtl':[234,180,160]}

def print_pr():
    for stock, pr in price.items():
        avg= statistics.mean(pr)
        print(stock,'==>',pr,'==>', 'avg:', round(avg,2))

def add_pr():
    add_s=input("Enter name of stock you want to add: ")
    add_p=int(input("Enter the price of new stock: "))
    if add_s in price:
        price[add_s].append(add_p)
        print_pr()
    else:
        price[add_s]=[add_p]
        print_pr()

def main():
    inp=input("Enter input for operations i.e; 'print' for printing stock prices and 'add' for adding new stock: ")
    if inp=='print':
        print_pr()
    elif inp=='add':
        add_pr()
    else:
        print("INVALID INPUT")

if __name__=="__main__":
    main()    