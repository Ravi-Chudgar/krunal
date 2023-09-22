def exercise_one():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0: # this are multiple of 5 and 3 respectively
            print("ThreeFive")
        elif num % 3 == 0: # this is for the multiple of 3 
            print("Three")
        elif num % 5 == 0: # this is for the multiple of 5
            print("Five")
        else:
            print(num)

if __name__ == "__main__":
    exercise_one()
