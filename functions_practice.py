

def hello():
    print('Well Hello There.')
    print('_________________')

def pack(food, side, drink):
    lunch = [food, side, drink]
    print(f'i packed: {food, side, drink}')
    return lunch

def eat_lunch(lunch):

    if len(lunch) == 0:
        print("my lunchbox is empty!")
    elif len(lunch) == 1 :
        print(f"I have {lunch[0]}")
    else: 
        i=0
        while i < len(lunch):
            if i == 0:
                print(f"first i'll eat a {lunch[i]}")
                i+=1
            else:
                print(f"Then i'll have some {lunch[i]}")
                i+=1

hello()
lunch = pack("pizza", "dr. pepper", "bbq chips")
eat_lunch(lunch)