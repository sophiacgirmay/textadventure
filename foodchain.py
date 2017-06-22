print("It's lunch time and ya feelin' kind of hungry.")
print("Do you have any dietary restrictions?.")
print("type 'yes' or 'no'")
user_input = input()
if user_input == "yes":
    print("Are you vegetarian or gluten free?")
    print("Type 'vegetarian' or 'gluten free'")
    user_input = input()
    if user_input == "vegatarian":
        print("You go to a salad bar and enjoy the crsippiness of the lettuce!")
    elif user_input == "gluten free":
        print("Do you want pizza or pasta?")
        print("Type 'pizza' or 'pasta'")
        user_input = input()
        if user_input == "pizza":
            print("You do not notice that there are mushrooms on the pizza and you have an allergic reaction to it! :(")
        elif user_input == "pasta":
            print("You enjoy it because there are worse options")
        else:
            print("Sorry there are not enough food options availiable for you. Go home!")
    else:
         print("Sorry there are no options availiable for you. Go home!")

elif user_input == "no":
    print("Do you want to eat a healthy meal or not healthy?")
    print("Type 'healthy' or 'not healthy'")
    user_input = input()
    if user_input == "healthy":
        print("Would you like your meal to be expensive or cheap?")
        print("Type 'expensive' or 'cheap'")
        user_input = input()
        if user_input == "expensive":
            print("Your option is Whole Foods, have a yummy meal!")
        elif user_input == "cheap":
            print("You go to Subway and have a yummy sandwich!")
    elif user_input == "not healthy":
        print("Would you like to go to McDonald's or Burger King?")
        print("Type 'McDonald's' or 'Burger King'")
        user_input = input()
        if user_input == "McDonald's":
            print("You get a happy meal!")
            print("You later get food poisioning!!")
        elif user_input == "Burger King":
            print("Enjoy your lovely meal of fries and a burger")
        else:
            print("Sorry there is too much traffic. Go back home")










     # finished the story by writing what happens
