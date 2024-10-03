from ui import FunVirusApp
import sys
import pychar
#[OTHER IMPORTS]


#Aidan, Peter, Modesto, & Ilya
#Software Engineering
#Professor Kenechukwu

def main():
#Run UI
    init_db()
    app = QApplication(sys.argv)
    ex = FunVirusApp()
    # Where the fun happens
    '''
    - Change Audio Output/Volume
    - Add Fun Image/Gifs
    - Change display coloring
    '''
    ex.show()
    sys.exit(app.exec_())


#run VIRUS-----------------------------------------------------------------!
'''
- take in credentials from user
- send credentials to VirusComp.py
- 
'''

###


if __name__ == '__main__':
    main()
    print("PETER")

