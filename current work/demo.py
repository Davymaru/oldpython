def get_list(name):
    flag = True
    easter_basket = []
    print(f"Hi! {name}!")
    print("Please enter 'full' when you are done. ")
    while flag:
        candy = input("What kind of candy or toy do you want for easter:  ")
        if candy == 'full':
            break
        easter_basket.append(candy)
    basket = input("What kind of basket do you want? (plastic, wood, et.):  ")
    return easter_basket, basket

def main():
    name = input ("Hi! who are you?   ")
    my_list, basket = get_list()
    print(my_list)
    print(basket)



    main()

 


