def grade(score):
    if score < 0 or score > 100:
        return "Value Out of Range!"
    elif score >= 90:
        return "Grade is A"
    elif score >= 80:
        return "Grade is B"
    elif score >= 70:
        return "Grade is C"
    elif score >= 60:
        return "Grade is D"
    else:
        return "Grade is F"

def main():
    start = True
    while start:
        score = int(input('Please Enter a Score Between 0 and 100 (Enter - 1 To End This Program ): '))
        if score == -1:
            print("You have Chosen to End This Program. Thank you for Using This Program.")
            start = False
        else:
            print(grade(score))

main()