class Multifunctioncall():

    def Subfields():
        SubfieldsInAI=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for Subfields in SubfieldsInAI:
            print("Sub-fields in AI are")
            return SubfieldsInAI

    def OddREven():
        num=int(input("Enter a number: "))
        if num % 2 == 0:
            print(num, 'is Even number')
        else:
            print("Odd Number")

    def MarriageEligibility():
        Gender=input("Your Gender: ")
        Age=int(input("Your Age: "))
        if (Gender =='Male') and (Age>=21):
            print("Your Eligible for Marriage")
        elif (Gender =='Female') and (Age>=18):
            print("Your Eligible for Marriage")       
        else:
            print("Not Eligible for Marriage")

    def MarkPercentage():
        Subject_1 = int(input("Subject_1 = "))
        Subject_2 = int(input("Subject_2 = "))
        Subject_3 = int(input("Subject_3 = "))
        Subject_4 = int(input("Subject_4 = "))
        Subject_5 = int(input("Subject_5 = "))
    
        Total = Subject_1 + Subject_2 + Subject_3 + Subject_4 + Subject_5
        Percentage = (Total / 500) * 100  # assuming each subject is out of 100
    
        print("Total =", Total)
        print("Percentage =", Percentage)

    def AreaANDPerimeter():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        Area=(Height*Breadth)/2
        print("Area of Triange: ",Area)
        Height_1 = int(input("Height_1: "))
        Height_2 = int(input("Height_2: "))
        Breadth_1=int(input("Breadth_1: "))
        Perimeter = (Height_1 + Height_2 + Breadth_1)
        print("Perimeter of Triangle: ",Perimeter)