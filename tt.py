
N = 5
K = 3


def create_userlist(N):
    if N <= 0:
        raise "There can not be zero or less people."
    return list(range(1, N + 1))


def the_rhyme(N, steps):
    userlist = create_userlist(N)
    if len(userlist) == 1:
        return userlist
    orderedlist = []
    steps -= 1
    iterator = 0
    while N > 1:
        iterator += steps
        while iterator >= N:
            iterator -= N
        orderedlist.append(userlist[iterator])
        userlist.pop(iterator)
        N -= 1
    orderedlist.append(userlist[0])
    return orderedlist

K = int(input("Enter the amount of silibels you want to count!: "))
N = int(input("Enter the amount of People you want to count out!: "))
print("The winner is {}".format(the_rhyme(N, K)[-1]))
