class Animal:
    """A simple animal class"""    
    def __init__(self,name): 
        elephant=("I have exceptional memory",
                  "I am the largest land-living mammal in the world",
                  "I can swim and use my trunk to brathe like a snorkel.");
        tiger=("I am the biggest cat",
               "I come in black and white or orange and black",
               "We are good swimmers and can swim up to 6 kilometres");
        bat=("We are the only flying mamals",
            "I can live for a long time.",
            "I use echo-location");
        self.animal_name = name;
        self.facts = {"elephant":elephant, "tiger":tiger,"bat":bat}
        
    def guess_who_am_i(self):
        temp = self.facts[self.animal_name] ;
        tries = 0 ;
        for fact in temp:
            print(fact);
            attempted_answer = input("Who am I? ");
            if attempted_answer == self.animal_name:
                print("You got it! I am a", self.animal_name);
                break ;
            else:
                tries = tries + 1 ; 
                if tries == 3:
                    print("I'm out of hints! The answer is", self.animal_name)
                else:
                    print("Nope, try again");
                continue ;
                
e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()