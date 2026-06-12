
def f_start_menu():
    
    print('''
         Start
         Exit
          ''')
          
    option = input("please make a selcetion ")
    if option.lower() not in ["start", "exit"]:
        print("Invalid option. Please try again")
        option = f_start_menu()

    return option
def f_charater_select():
    print('''
         Shit diger
         Shit eater
         Shit head
          ''')
          
    option = input("please make a selcetion ")
    if option.lower() not in ["shit digger", "shit eater", "shit head"]:
        print("Invalid option. Please try again")
        option = f_attack_menu()
    
    return option
def f_attack_menu():
    
    print('''
         Attack
         Duble Attack
         Tripple Attack
         Kill Shot
         Doge
          
          ''')
          
    option = input("please make a selcetion ")
    if option.lower() not in ["attack", "duble attack", "tripple attack",
                              "kill shot","doge"]:
        
        print("Invalid option. Please try again")
        option = f_attack_menu()
    
    return option
