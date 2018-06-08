def my_for(max):
    total=0
    print(2, "is a prime number")

    for i in range(3,max+1):
        for j in range(2, i):
            if (i % j == 0):
                break
            if(j==i-1):
                total+=1
                print(i,"is a prime number")

    print("There are",total+1,"primes in 0 ~",max)


max=int(input("Please enter upper limit\n"))
my_for(max)
