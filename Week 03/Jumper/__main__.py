"""

Author: Andres Dilan Salas Duran
Class: CSE 110
Section: 18
Teacher: Brother Brad Lythgoe
Purpose: The purpose of this activity is to develop and demonstrate your mastery of the following competencies
            3.0 Develop working software using the techniques of programming with classes.
            3.3 Develop a working program that controls access to class members.
Due:  Saturday by 11:59pm

"""

from game.director import Director

def main():
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()

"""

  ______           _          __   _   _                                                        
 |  ____|         | |        / _| | | | |                                                       
 | |__   _ __   __| |   ___ | |_  | |_| |__   ___   _ __  _ __ ___   __ _ _ __ __ _ _ __ ___    
 |  __| | '_ \ / _` |  / _ \|  _| | __| '_ \ / _ \ | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \   
 | |____| | | | (_| | | (_) | |   | |_| | | |  __/ | |_) | | | (_) | (_| | | | (_| | | | | | |_ 
 |______|_| |_|\__,_|  \___/|_|    \__|_| |_|\___| | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_(_)
                                                   | |               __/ |                      
                                                   |_|              |___/                       

"""