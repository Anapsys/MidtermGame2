import pygame as pg
import sys
import time
import logging
from OpenGL.GL import *
from OpenGL.GLU import *

def tutorial():
    print("Commands: N, E, S, W, look, talk, attack, ?")

def updatePosition():
    for Element in NPCs:
        if (Element._posX == Player1._posX and Element._posY == Player1._posY):
            print("There is a " + Element._name + " here.")
            
def findEntityAt(x, y):
    for Element in NPCs:
        if (Element._posX == x and Element._posY == y):
            return Element
    return None

def lookAround(x, y):
    entity = findEntityAt(x+1, y)
    if entity:
        print("To the east: a " + entity._name)
        
    entity = findEntityAt(x+1, y+1)
    if entity:
        print("To the northeast: a " + entity._name)
        
    entity = findEntityAt(x, y+1)
    if entity:
        print("To the north: a " + entity._name)
        
    entity = findEntityAt(x-1, y+1)
    if entity:
        print("To the northwest: a " + entity._name)
        
    entity = findEntityAt(x-1, y)
    if entity:
        print("To the west: a " + entity._name)
        
    entity = findEntityAt(x-1, y-1)
    if entity:
        print("To the southwest: a " + entity._name)
        
    entity = findEntityAt(x, y-1)
    if entity:
        print("To the south: a " + entity._name)
        
    entity = findEntityAt(x+1, y-1)
    if entity:
        print("To the southeast: a " + entity._name)

class Entity(object):
    _name = "DEFAULT"
    _posX = 5
    _posY = 5
    _command = ""
    _attack = 2
    _defense = 1
    _health = 4
    def __init__(self, x, y, name):
        self._posX = x
        self._posY = y
        self._name = name
    def getCommand(self):
        self._command = input("> ").lower()
        return self._command
    #accessors
    def interact(self, instigator):
        if self._name == "Ellie the Tutorial Fairy":
            print("Hello " + instigator._name + " and welcome to the Parking Lot!")
            print("Of Destiny!")
            print("Type TALK to interact with the colourful characters!")
        if self._name == "Gorlok the Garlic Destroyer":
            print("I'm going to bite you " + instigator._name + "!")
        if self._name == "A cricket":
            print("Chirp.")
    #mutators
    def move(self, command):
        if command == "n" or command == "north":
            self._posY += 1
            print("Moved north. Y = " + str(self._posY))
            return
        if command == "s" or command == "south":
            self._posY -= 1
            print("Moved south. Y = " + str(self._posY))
            return
        if command == "e" or command == "east" or command == "r" or command == "right":
            self._posX += 1
            print("Moved east. X = " + str(self._posX))
            return
        if command == "w" or command == "west" or command == "l" or command == "left":
            self._posX -= 1
            print("Moved west. X = " + str(self._posX))
            return
    def update(self):
        if self._health <= 0:
            self.die()
    def damage(self, instigator):
        self._health -= (instigator._attack - self._defense)
        print(self._name + " took " + str(instigator._attack - self._defense) + " damage!")
        print(self._name + " has " + str(self._health) + " health left.")
    def die(self):
        print("ARG YOU HAVE BESTED ME")
        logging.critical('CRITICAL SYSTEM FAILURE DELETING SYSTEM 32')
        print(self._name + " has died.")

###
#EXECUTION
###

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')

NPCs = []
NPCs.append(Entity(3, 6, "Gorlok the Garlic Destroyer"))
NPCs.append(Entity(5, 5, "Ellie the Tutorial Fairy"))
NPCs.append(Entity(0, 0, "A cricket"))
Other = None

if __name__ == '__main__':
    command = ""
    Player1 = Entity(5, 5, input("Choose your name: "))
    tutorial()
    
    while 1:
        Other = None
        Player1.update()
        for NPC in NPCs:
            NPC.update()
            if (NPC._health <= 0):
                NPCs.remove(NPC)
            
        updatePosition()
        command = Player1.getCommand()

        if command == "exit" or command == "die":
            print("Game exiting")
            logging.debug('This is a log message.')
            break

        elif command == "n" or command == "north" or command == "s" or command == "south" or command == "e" or command == "east" or command == "r" or command == "right" or command == "w" or command == "west" or command == "l" or command == "left":
            Player1.move(command)

        elif command == "talk":
            try:
                Other = findEntityAt(Player1._posX, Player1._posY)
                Other.interact(Player1)
            except:
                logging.debug('No entity found at current position.')
                print("It is not insanity to speak to oneself.")
                print("It is only insanity to speak to one who is not there.")
        elif command == "attack":
            try:
                Other = findEntityAt(Player1._posX, Player1._posY)
                Other.damage(Player1)
            except:
                logging.debug('No entity found at current position.')
                print("You wildly swing your sword for no reason!")
                print("The air takes 1 damage. It has 985027507289520965283698725390008083274 health left.")

        elif command == "look":
            try:
                lookAround(Player1._posX, Player1._posY)
            except:
                logging.debug('Looking failure????')
        elif command == "?":
            tutorial()
