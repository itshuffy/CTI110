#CTI-110
#M6T1
#Jesse Huff
#10/26/2017

#define main
def main():
    km_in=float(input("Enter kilometers: "))
    show_miles(km_in)

#defines show_miles
def show_miles(km):
    miles = km * 0.6214
    print(km, "kilometers is equal to", miles, "miles")

#run main
main()
