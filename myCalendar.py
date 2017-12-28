### myCalendar.py
'''
Karl Honse 
Lab 4 
9-26-2017
'''
def main():
    runs = int(input("\nHow many Calendars do you want to make? "))
    for x in range(runs):
        n = int(input("Input the number of days in the month (28-31): ")) 
        while n < 28 or n > 31:
            n = int(input("Input the number of days in the month (28-31): "))
        
        d = int(input("Input the starting day (0=Sun, 1=Mon,...): "))
        while d < 0 or d > 6:
            d = int(input("Input the starting day (0=Sun, 1=Mon,...): "))
            
        m = str(input("Input the name of the Month: "))
        
        print("\n", m)
        
        for j in range(d):
            print("   ", end = "")
        
        i = 1
        while i <= n:
            if i < 10:
                print("",i,end = " ")
            else:
                print(i, end = " ")
                
            if (i + d) % 7 == 0:
                print(" ")

            i = i + 1
        print("\n")
main()