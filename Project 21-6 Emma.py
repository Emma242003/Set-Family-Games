import pygame
import os
import random
pygame.init()


class Kaart:
    def __init__(self, kaart_kleur=0, kaart_vulling=0, kaart_vorm=0, kaart_aantal=0):
        self.kleur = kaart_kleur
        self.vulling = kaart_vulling
        self.vorm = kaart_vorm
        self.aantal = kaart_aantal

    def __isset__(self, other1, other2):
        a = (self.kleur+other1.kleur+other2.kleur) % 3
        b = (self.vulling+other1.vulling+other2.vulling) % 3
        c = (self.vorm+other1.vorm+other2.vorm) % 3
        d = (self.aantal+other1.aantal+other2.aantal) % 3
        return all(s == 0 for s in (a, b, c, d))

    def __str__(self):
        return '('+str(self.kleur)+','+str(self.vulling)+','+str(self.vorm)+','+str(self.aantal)+')'

    def __random__(self):
        r = Kaart()
        r.kleur = random.randint(0, 2)
        r.vulling = random.randint(0, 2)
        r.vorm = random.randint(0, 2)
        r.aantal = random.randint(0, 2)
        return r

    def __kaarten__(self, n=12):
        self.kaarten = random.sample(Kaart.__combinaties__(), n)
        lijst_kaarten = []
        for i in range(0, len(self.kaarten)):
            lijst_kaarten.append(str(self.kaarten[i]))
        # print(lijst_kaarten)
        return self.kaarten

    def __combinaties__():
        return [Kaart(kaart_kleur, kaart_vulling, kaart_vorm, kaart_aantal)  # .__str__()
                      for kaart_kleur in (0, 1, 2)
                      for kaart_vulling in (0, 1, 2)
                      for kaart_vorm in (0, 1, 2)
                      for kaart_aantal in (0, 1, 2)]

    def __lijstsets__(self):
        sets = []
        self.kaarten = Kaart().__kaarten__()
        lijst_kaarten = []
        for i in range(0, len(self.kaarten)):
            lijst_kaarten.append(str(self.kaarten[i]))
        # print(lijst_kaarten)
        for i in range(0, len(self.kaarten)-2):
            for j in range(i+1, len(self.kaarten)-1):
                for k in range(i+2, len(self.kaarten)):
                    if self.kaarten[i].__isset__(self.kaarten[j], self.kaarten[k]):
                        sets.append((str(self.kaarten[i]), str(
                            self.kaarten[j]), str(self.kaarten[k])))
        return lijst_kaarten, sets

def checkset(kaarten):
    sets=[]
    s=0
    kaarten2 = list(kaarten)
    for i in range(0,len(kaarten)):
        kaarten2[i]=kaarten2[i].replace('(','')
        kaarten2[i]=kaarten2[i].replace(',','')
        kaarten2[i]=kaarten2[i].replace(')','')
    for i in range(0,len(kaarten2)-2):
        for j in range(i+1,len(kaarten2)-1):
            for k in range(i+2,len(kaarten2)):
                    if all( (int(kaarten2[i][p])+int(kaarten2[j][p])+int(kaarten2[k][p]))%3==0 for p in range(0,4)):
                        sets.append([])
                        sets[s].append(kaarten[i])
                        sets[s].append(kaarten[j])
                        sets[s].append(kaarten[k])
                        s+=1
    return sets



Color_Background = (129, 218, 232)

display_width = 1000
display_height = 655

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Set! Family Games')

dictionary = {'(0,0,0,0)': pygame.image.load(os.path.join('kaarten', 'greendiamondempty1.gif')),
            '(0,0,0,1)': pygame.image.load(os.path.join('kaarten', 'greendiamondempty2.gif')),
            '(0,0,0,2)': pygame.image.load(os.path.join('kaarten', 'greendiamondempty3.gif')),
            '(0,2,0,0)': pygame.image.load(os.path.join('kaarten', 'greendiamondfilled1.gif')),
            '(0,2,0,1)': pygame.image.load(os.path.join('kaarten', 'greendiamondfilled2.gif')),
            '(0,2,0,2)': pygame.image.load(os.path.join('kaarten', 'greendiamondfilled3.gif')),
            '(0,1,0,0)': pygame.image.load(os.path.join('kaarten', 'greendiamondshaded1.gif')),
            '(0,1,0,1)': pygame.image.load(os.path.join('kaarten', 'greendiamondshaded2.gif')),
            '(0,1,0,2)': pygame.image.load(os.path.join('kaarten', 'greendiamondshaded3.gif')),
            '(0,0,1,0)': pygame.image.load(os.path.join('kaarten', 'greenovalempty1.gif')),
            '(0,0,1,1)': pygame.image.load(os.path.join('kaarten', 'greenovalempty2.gif')),
            '(0,0,1,2)': pygame.image.load(os.path.join('kaarten', 'greenovalempty3.gif')),
            '(0,2,1,0)': pygame.image.load(os.path.join('kaarten', 'greenovalfilled1.gif')),
            '(0,2,1,1)': pygame.image.load(os.path.join('kaarten', 'greenovalfilled2.gif')),
            '(0,2,1,2)': pygame.image.load(os.path.join('kaarten', 'greenovalfilled3.gif')),
            '(0,1,1,0)': pygame.image.load(os.path.join('kaarten', 'greenovalshaded1.gif')),
            '(0,1,1,1)': pygame.image.load(os.path.join('kaarten', 'greenovalshaded2.gif')),
            '(0,1,1,2)': pygame.image.load(os.path.join('kaarten', 'greenovalshaded3.gif')),
            '(0,0,2,0)': pygame.image.load(os.path.join('kaarten', 'greensquiggleempty1.gif')),
            '(0,0,2,1)': pygame.image.load(os.path.join('kaarten', 'greensquiggleempty2.gif')),
            '(0,0,2,2)': pygame.image.load(os.path.join('kaarten', 'greensquiggleempty3.gif')),
            '(0,2,2,0)': pygame.image.load(os.path.join('kaarten', 'greensquigglefilled1.gif')),
            '(0,2,2,1)': pygame.image.load(os.path.join('kaarten', 'greensquigglefilled2.gif')),
            '(0,2,2,2)': pygame.image.load(os.path.join('kaarten', 'greensquigglefilled3.gif')),
            '(0,1,2,0)': pygame.image.load(os.path.join('kaarten', 'greensquiggleshaded1.gif')),
            '(0,1,2,1)': pygame.image.load(os.path.join('kaarten', 'greensquiggleshaded2.gif')),
            '(0,1,2,2)': pygame.image.load(os.path.join('kaarten', 'greensquiggleshaded3.gif')),


            '(1,0,0,0)': pygame.image.load(os.path.join('kaarten', 'purplediamondempty1.gif')),
            '(1,0,0,1)': pygame.image.load(os.path.join('kaarten', 'purplediamondempty2.gif')),
            '(1,0,0,2)': pygame.image.load(os.path.join('kaarten', 'purplediamondempty3.gif')),
            '(1,2,0,0)': pygame.image.load(os.path.join('kaarten', 'purplediamondfilled1.gif')),
            '(1,2,0,1)': pygame.image.load(os.path.join('kaarten', 'purplediamondfilled2.gif')),
            '(1,2,0,2)': pygame.image.load(os.path.join('kaarten', 'purplediamondfilled3.gif')),
            '(1,1,0,0)': pygame.image.load(os.path.join('kaarten', 'purplediamondshaded1.gif')),
            '(1,1,0,1)': pygame.image.load(os.path.join('kaarten', 'purplediamondshaded2.gif')),
            '(1,1,0,2)': pygame.image.load(os.path.join('kaarten', 'purplediamondshaded3.gif')),
            '(1,0,1,0)': pygame.image.load(os.path.join('kaarten', 'purpleovalempty1.gif')),
            '(1,0,1,1)': pygame.image.load(os.path.join('kaarten', 'purpleovalempty2.gif')),
            '(1,0,1,2)': pygame.image.load(os.path.join('kaarten', 'purpleovalempty3.gif')),
            '(1,2,1,0)': pygame.image.load(os.path.join('kaarten', 'purpleovalfilled1.gif')),
            '(1,2,1,1)': pygame.image.load(os.path.join('kaarten', 'purpleovalfilled2.gif')),
            '(1,2,1,2)': pygame.image.load(os.path.join('kaarten', 'purpleovalfilled3.gif')),
            '(1,1,1,0)': pygame.image.load(os.path.join('kaarten', 'purpleovalshaded1.gif')),
            '(1,1,1,1)': pygame.image.load(os.path.join('kaarten', 'purpleovalshaded2.gif')),
            '(1,1,1,2)': pygame.image.load(os.path.join('kaarten', 'purpleovalshaded3.gif')),
            '(1,0,2,0)': pygame.image.load(os.path.join('kaarten', 'purplesquiggleempty1.gif')),
            '(1,0,2,1)': pygame.image.load(os.path.join('kaarten', 'purplesquiggleempty2.gif')),
            '(1,0,2,2)': pygame.image.load(os.path.join('kaarten', 'purplesquiggleempty3.gif')),
            '(1,2,2,0)': pygame.image.load(os.path.join('kaarten', 'purplesquigglefilled1.gif')),
            '(1,2,2,1)': pygame.image.load(os.path.join('kaarten', 'purplesquigglefilled2.gif')),
            '(1,2,2,2)': pygame.image.load(os.path.join('kaarten', 'purplesquigglefilled3.gif')),
            '(1,1,2,0)': pygame.image.load(os.path.join('kaarten', 'purplesquiggleshaded1.gif')),
            '(1,1,2,1)': pygame.image.load(os.path.join('kaarten', 'purplesquiggleshaded2.gif')),
            '(1,1,2,2)': pygame.image.load(os.path.join('kaarten', 'purplesquiggleshaded3.gif')),


            '(2,0,0,0)': pygame.image.load(os.path.join('kaarten', 'reddiamondempty1.gif')),
            '(2,0,0,1)': pygame.image.load(os.path.join('kaarten', 'reddiamondempty2.gif')),
            '(2,0,0,2)': pygame.image.load(os.path.join('kaarten', 'reddiamondempty3.gif')),
            '(2,2,0,0)': pygame.image.load(os.path.join('kaarten', 'reddiamondfilled1.gif')),
            '(2,2,0,1)': pygame.image.load(os.path.join('kaarten', 'reddiamondfilled2.gif')),
            '(2,2,0,2)': pygame.image.load(os.path.join('kaarten', 'reddiamondfilled3.gif')),
            '(2,1,0,0)': pygame.image.load(os.path.join('kaarten', 'reddiamondshaded1.gif')),
            '(2,1,0,1)': pygame.image.load(os.path.join('kaarten', 'reddiamondshaded2.gif')),
            '(2,1,0,2)': pygame.image.load(os.path.join('kaarten', 'reddiamondshaded3.gif')),
            '(2,0,1,0)': pygame.image.load(os.path.join('kaarten', 'redovalempty1.gif')),
            '(2,0,1,1)': pygame.image.load(os.path.join('kaarten', 'redovalempty2.gif')),
            '(2,0,1,2)': pygame.image.load(os.path.join('kaarten', 'redovalempty3.gif')),
            '(2,2,1,0)': pygame.image.load(os.path.join('kaarten', 'redovalfilled1.gif')),
            '(2,2,1,1)': pygame.image.load(os.path.join('kaarten', 'redovalfilled2.gif')),
            '(2,2,1,2)': pygame.image.load(os.path.join('kaarten', 'redovalfilled3.gif')),
            '(2,1,1,0)': pygame.image.load(os.path.join('kaarten', 'redovalshaded1.gif')),
            '(2,1,1,1)': pygame.image.load(os.path.join('kaarten', 'redovalshaded2.gif')),
            '(2,1,1,2)': pygame.image.load(os.path.join('kaarten', 'redovalshaded3.gif')),
            '(2,0,2,0)': pygame.image.load(os.path.join('kaarten', 'redsquiggleempty1.gif')),
            '(2,0,2,1)': pygame.image.load(os.path.join('kaarten', 'redsquiggleempty2.gif')),
            '(2,0,2,2)': pygame.image.load(os.path.join('kaarten', 'redsquiggleempty3.gif')),
            '(2,2,2,0)': pygame.image.load(os.path.join('kaarten', 'redsquigglefilled1.gif')),
            '(2,2,2,1)': pygame.image.load(os.path.join('kaarten', 'redsquigglefilled2.gif')),
            '(2,2,2,2)': pygame.image.load(os.path.join('kaarten', 'redsquigglefilled3.gif')),
            '(2,1,2,0)': pygame.image.load(os.path.join('kaarten', 'redsquiggleshaded1.gif')),
            '(2,1,2,1)': pygame.image.load(os.path.join('kaarten', 'redsquiggleshaded2.gif')),
            '(2,1,2,2)': pygame.image.load(os.path.join('kaarten', 'redsquiggleshaded3.gif')),
            }


def display_kaarten(kaarten):

    distance_x = 100
    distance_y = 200

    # Display van kaarten & extra's :
    gameDisplay.fill(Color_Background)
    gameDisplay.blit(dictionary[kaarten[0]], (15, 10))
    gameDisplay.blit(dictionary[kaarten[1]],
                     (2*15 + 1*distance_x, 10 + 0*distance_y))
    gameDisplay.blit(dictionary[kaarten[2]],
                     (3*15 + 2*distance_x, 10 + 0*distance_y))
    gameDisplay.blit(dictionary[kaarten[3]],
                     (4*15 + 3*distance_x, 10 + 0*distance_y))
    gameDisplay.blit(dictionary[kaarten[4]],
                     (1*15 + 0*distance_x, 2*10 + 1*distance_y))
    gameDisplay.blit(dictionary[kaarten[5]],
                     (2*15 + 1*distance_x, 2*10 + 1*distance_y))
    gameDisplay.blit(dictionary[kaarten[6]],
                     (3*15 + 2*distance_x, 2*10 + 1*distance_y))
    gameDisplay.blit(dictionary[kaarten[7]],
                     (4*15 + 3*distance_x, 2*10 + 1*distance_y))
    gameDisplay.blit(dictionary[kaarten[8]],
                     (1*15 + 0*distance_x, 3*10 + 2*distance_y))
    gameDisplay.blit(dictionary[kaarten[9]],
                     (2*15 + 1*distance_x, 3*10 + 2*distance_y))
    gameDisplay.blit(dictionary[kaarten[10]],
                     (3*15 + 2*distance_x, 3*10 + 2*distance_y))
    gameDisplay.blit(dictionary[kaarten[11]],
                     (4*15 + 3*distance_x, 3*10 + 2*distance_y))
    
    gameDisplay.blit(pygame.transform.scale((pygame.image.load(
        os.path.join('kaarten', 'SET.png'))), (300, 166.667)), (500, 15))
    font = pygame.font.SysFont(None, 30)
    
    pygame.draw.rect(gameDisplay, (181, 134, 181), (500, 220, 170, 40))
    pygame.draw.rect(gameDisplay, (0, 0, 0), (500, 220, 170, 40), 3)  
   
    button1 = font.render('Nieuwe kaarten', True, (0, 0, 0))
    gameDisplay.blit(button1, (510,230))
    
# def display_instellingen():


def deck():

    
    # Alle kaarten in de pot, weergegeven als een string
    pot=Kaart.__combinaties__()
    for i in range(0,len(pot)):
        pot[i] = str(pot[i])

    kaarten = random.sample(pot,12)
    print(kaarten) # test of dit goed gaat 
    
    run=True
    clock = pygame.time.Clock()

    FPS= 60
    
    distance_x=100
    distance_y=200
    
    mogelijk_set=[]
    index_set = []
    
    scores=0
    newcards = True
    
    # main loop :
    while run:
        clock.tick(FPS)
        
        #verwijdert kaarten die op display zijn van de pot 
        if newcards:
            for display_kaart in kaarten:
                if display_kaart in pot:
                    pot.remove(display_kaart)
            newcards = False
           
        # Display van kaarten & extra's :
        display_kaarten(kaarten)
        
        
    
        font = pygame.font.SysFont(None, 30)
        score=font.render('Score:'+str(scores), True, (0,0,0))
        gameDisplay.blit(score, (700, 230))
        
        display_pot=font.render('Kaarten in de pot :'+str(len(pot)),True,(0,0,0))
        gameDisplay.blit(display_pot, (500,400))

        # event loop met alle mogelijke gebeurtenissen :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # verteld het programma te stoppen wanneer het scherm gesloten wordt
                run=False
            if event.type == pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if 15 < pos[0] < 115 and 10 < pos[1] < 210:
                    mogelijk_set.append(kaarten[0])
                    index_set.append(0)
                if 2*15 + 1*distance_x < pos[0] < 2*15 + 2*distance_x and 10 + 0*distance_y < pos[1] < 10 + 1*distance_y:
                    mogelijk_set.append(kaarten[1])
                    index_set.append(1)
                if 3*15 + 2*distance_x < pos[0] < 3*15 + 3*distance_x and 10 + 0*distance_y < pos[1] < 10 + 1*distance_y:
                    mogelijk_set.append(kaarten[2])
                    index_set.append(2)
                if 4*15 + 3*distance_x < pos[0] < 4*15 + 4*distance_x and 10 + 0*distance_y < pos[1] < 10 + 1*distance_y:
                    mogelijk_set.append(kaarten[3])
                    index_set.append(3)
                if 1*15 + 0*distance_x < pos[0] < 1*15 + 1*distance_x and 2*10 + 1*distance_y < pos[1] < 2*10 + 2*distance_y:
                    mogelijk_set.append(kaarten[4])
                    index_set.append(4)
                if 2*15 + 1*distance_x < pos[0] < 2*15 + 2*distance_x and 2*10 + 1*distance_y < pos[1] < 2*10 + 2*distance_y:
                    mogelijk_set.append(kaarten[5])
                    index_set.append(5)
                if 3*15 + 2*distance_x < pos[0] < 3*15 + 3*distance_x and 2*10 + 1*distance_y < pos[1] < 2*10 + 2*distance_y:
                    mogelijk_set.append(kaarten[6])
                    index_set.append(6)
                if 4*15 + 3*distance_x < pos[0] < 4*15 + 4*distance_x and 2*10 + 1*distance_y < pos[1] < 2*10 + 2*distance_y:
                    mogelijk_set.append(kaarten[7])
                    index_set.append(7)
                if 1*15 + 0*distance_x < pos[0] < 1*15 + 1*distance_x and 3*10 + 2*distance_y < pos[1] < 3*10 + 3*distance_y:
                    mogelijk_set.append(kaarten[8])
                    index_set.append(8)
                if 2*15 + 1*distance_x < pos[0] < 2*15 + 2*distance_x and 3*10 + 2*distance_y < pos[1] < 3*10 + 3*distance_y:
                    mogelijk_set.append(kaarten[9])
                    index_set.append(9)
                if 3*15 + 2*distance_x < pos[0] < 3*15 + 3*distance_x and 3*10 + 2*distance_y < pos[1] < 3*10 + 3*distance_y:
                    mogelijk_set.append(kaarten[10])
                    index_set.append(10)
                if 4*15 + 3*distance_x < pos[0] < 4*15 + 4*distance_x and 3*10 + 2*distance_y < pos[1] < 3*10 + 3*distance_y:
                    mogelijk_set.append(kaarten[11])
                    index_set.append(11)
                if 500 < pos[0] < 670 and 220 < pos[1] < 260:
                    kaarten, sets=Kaart().__lijstsets__()
        if len(mogelijk_set) == 3:
            if len(checkset(mogelijk_set)) == 0:
                print("no set")
                mogelijk_set.clear()
            else:
                print("is set")
                scores+=1
                
                for k in index_set:
                    kaarten[k] = random.choice(pot)
                    pot.remove(kaarten[k])
                
                mogelijk_set.clear()
                index_set.clear()
                

        pygame.display.update()
    pygame.quit()

deck()