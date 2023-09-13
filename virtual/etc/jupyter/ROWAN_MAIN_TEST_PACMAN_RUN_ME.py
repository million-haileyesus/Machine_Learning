# goPac.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, (4) you provide clear attribution 
# to RowanRobots: http://www.rowan.edu/robots
# 
# Attribution Information: Written by Jennifer S. Kay
# kay@rowan.edu to facilitate running the Berkeley python projects in
# python 3 using ipython3
#

import sys
from pacman import go_pac
from pacman import readCommand

if __name__ == '__main__':
    rowanArgs = sys.argv[1:] # Get game components based on input
    go_pac(rowanArgs)
    
