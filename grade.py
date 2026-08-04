while True:
    try:
        a = float(input("Enter grade for subject 1: "))
        b = float(input("Enter grade for subject 2: "))
        c = float(input("Enter grade for subject 3: "))
        d = float(input("Enter grade for subject 4: "))
        e = float(input("Enter grade for subject 5: "))
        f = float(input("Enter grade for subject 6: "))
        g = float(input("Enter grade for subject 7: "))
        h = float(input("Enter grade for subject 8: "))
    
        average = (a + b + c + d + e + f + g + h) / 8
        average = round(average)

        if average >= 97.5 and average <= 100:
            print("With Highest Honors", average)
            break
        elif average >= 94.5 and average <= 97.4:
            print("With High Honors", average)
            break
        elif average >= 89.5 and average <= 94.4:
            print("With Honors", average)
            break
        elif average >= 0 and average <= 74.4:
            print("FAIL", average)
            break
        elif average >= 74.5 and average <= 89.4:
            print("PASSED", average)
            break
        else:
            print("Invalid input, please enter valid grades.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
