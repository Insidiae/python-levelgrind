times = input("How many times do I have to tell you? ")
times = int(times) if times.isnumeric() else 0

if times > 0:
    for time in range(times):
        print("CLEAN UP YOUR ROOM!!!")
