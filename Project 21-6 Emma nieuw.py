import pygame,os,random,sys


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

def kaartnaam(invoer):
    invoer=invoer.replace('(','')
    invoer=invoer.replace(')','')
    invoer=invoer.replace(',','')
    kleur=['green','purple','red']
    vulling=['empty','shaded','filled']
    vorm=['diamond','oval','squiggle']
    aantal=['1','2','3']
    a=kleur[int(invoer[0])]
    b=vulling[int(invoer[1])]
    c=vorm[int(invoer[2])]
    d=aantal[int(invoer[3])]
    return a+c+b+d

def afbeelding(invoer):
    invoer=kaartnaam(invoer)
    a=pygame.image.load(os.path.join('kaarten', invoer+'.gif'))
    return a

Color_Background = (129, 218, 232)

display_width = 1000
display_height = 655

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Set! Family Games')




def display_kaarten(kaarten):
    
    # de afmetingen van de gebruikte kaarten :
    global distance_x
    distance_x= 100
    global distance_y
    distance_y= 200
    
    # de posities van alle kaarten op het display :
    global displaycards
    displaycards = [] 
    for i in range(0,3):
        for j in range(0,4):
            displaycards.append(((j+1)*15+j*distance_x,(i+1)*10+i*distance_y))
    
    # Display van kaarten & extra's :
    gameDisplay.fill(Color_Background)
    for k in range(0,12):
        gameDisplay.blit(afbeelding(kaarten[k]),displaycards[k])
    
    gameDisplay.blit(pygame.transform.scale((pygame.image.load(
        os.path.join('kaarten', 'SET.png'))), (300, 166.667)), (500, 15))
    font = pygame.font.SysFont(None, 30)
    
    pygame.draw.rect(gameDisplay, (181, 134, 181), (500, 220, 170, 40))
    pygame.draw.rect(gameDisplay, (0, 0, 0), (500, 220, 170, 40), 3)  
    button1 = font.render('No sets', True, (0, 0, 0))
    gameDisplay.blit(button1, (510,230))
    
    for i in index_set:
        pygame.draw.rect(gameDisplay, (0, 0, 0), (displaycards[i][0],displaycards[i][1], distance_x, distance_y), 3)
        

def game():

    
    # Alle kaarten in de pot, weergegeven als een string
    pot=Kaart.__combinaties__()
    for i in range(0,len(pot)):
        pot[i] = str(pot[i])

    global kaarten    
    kaarten = random.sample(pot,12)
    #print(kaarten)
    
    begin=True
    
    #implementen van tijd : 
    clock = pygame.time.Clock()
    
    
    FPS= 60
    
    
    mogelijk_set=[]
    global index_set
    index_set = []
    
    score1=0
    score2=0
    newcards = True
    
    
    
    # main loop :

    while begin:
        clock.tick(FPS)
        gameDisplay.fill(Color_Background)
        
        font1 = pygame.font.SysFont(None, 40)
        font2 = pygame.font.SysFont(None, 30)
        pygame.draw.rect(gameDisplay, (181, 134, 181), (300, 50, 400, 555))
        pygame.draw.rect(gameDisplay, (0,0,0), (300, 50, 400, 555), 3)
        
        gameDisplay.blit(pygame.transform.scale((pygame.image.load(
            os.path.join('kaarten', 'SET.png'))), (300, 166.667)), (350, 70))
        
        pygame.draw.rect(gameDisplay, (96, 191, 100), (390, 250, 220, 90))
        pygame.draw.rect(gameDisplay, (0,0,0), (390, 250, 220, 90), 3)
        competent = font1.render('Competent', True, (0, 0, 0))
        gameDisplay.blit(competent, (420,260))
        tijd1 = font2.render('30 seconden', True, (0, 0, 0))
        gameDisplay.blit(tijd1, (435,300))
 
        pygame.draw.rect(gameDisplay, (240, 180, 95), (390, 360, 220, 90))
        pygame.draw.rect(gameDisplay, (0,0,0), (390, 360, 220, 90), 3)
        expert = font1.render('Expert', True, (0, 0, 0))
        gameDisplay.blit(expert, (455,370))
        tijd2 = font2.render('20 seconden', True, (0, 0, 0))
        gameDisplay.blit(tijd2, (435,410))
        
        pygame.draw.rect(gameDisplay, (223, 105, 86), (390, 470, 220, 90))
        pygame.draw.rect(gameDisplay, (0,0,0), (390, 470, 220, 90), 3)
        master = font1.render('Master', True, (0, 0, 0))
        gameDisplay.blit(master, (455,480))
        tijd3 = font2.render('10 seconden', True, (0, 0, 0))
        gameDisplay.blit(tijd3, (435,520))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # verteld het programma te stoppen wanneer het scherm gesloten wordt
                #begin=False
                #run=False
                #pygame.display.update()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP: # verteld het programma wat te doen wanneer op het scherm geklikt wordt
                pos=pygame.mouse.get_pos()
                if 390 < pos[0] < 610 and 250 < pos[1] < 340:
                    tijd=30
                    begin=False
                if 390 < pos[0] < 610 and 360 < pos[1] < 450:
                    tijd=20
                    begin=False
                if 390 < pos[0] < 610 and 470 < pos[1] < 560:
                    tijd=10
                    begin=False
                
        pygame.display.update()    
    
    #geeft de tijd die je gebruikt tijdens het spelen van set 
    global counter, text
    counter, text = tijd, str(tijd).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    run=True
    
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
        
        
        #display van score, kaarten in de pot en de tijd 
        font = pygame.font.SysFont(None, 30)
        scores1=font.render('Player score: '+str(score1), True, (0,0,0))
        gameDisplay.blit(scores1, (700, 230))
        
        scores2=font.render('Computer score: '+str(score2),True,(0,0,0))
        gameDisplay.blit(scores2,(700, 250))
        
        display_pot=font.render('Kaarten in de pot: '+str(len(pot)),True,(0,0,0))
        gameDisplay.blit(display_pot, (500,400))
        
        display_time=font.render('Time: '+text, True, (0, 0, 0))
        gameDisplay.blit(display_time, (500,190))
        
        
        # event loop met alle mogelijke gebeurtenissen :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # verteld het programma te stoppen wanneer het scherm gesloten wordt
                run=False
            if event.type == pygame.MOUSEBUTTONUP: # verteld het programma wat te doen wanneer op het scherm geklikt wordt
                pos=pygame.mouse.get_pos()
                for i in range(0,12):
                    if displaycards[i][0] < pos[0] < (displaycards[i][0]+distance_x) and displaycards[i][1] < pos[1] < (displaycards[i][1]+distance_y):
                        #checkt of de kaart al aangeklikt is 
                       if i in index_set:
                           index_set.remove(i)
                           mogelijk_set.remove(kaarten[i])
                       else:
                           index_set.append(i)
                           mogelijk_set.append(kaarten[i])
                if 500 < pos[0] < 670 and 220 < pos[1] < 260:
                    if checkset(kaarten) == 0: 
                        score1 += 1
                        for n in (0,1,2):
                            kaarten[n]=random.choice(pot)
                            pot.remove(kaarten[n])
                        
                    else:
                        score2 += 1
            
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3) 
                else:
                    text= '0'.rjust(3)
                    if len(checkset(kaarten)) == 0 :
                        for k in (0,1,2):
                            kaarten[k]=random.choice(pot)
                            pot.remove(kaarten[k])
                    
                    else:
                        score2+=1
                        counter = tijd+1
                        for l in checkset(kaarten)[0]:
                            index_set_comp = int(kaarten.index(l))
                            kaarten[index_set_comp] = random.choice(pot)
                            pot.remove(kaarten[index_set_comp])
        
        
        if len(mogelijk_set) == 3:
            if len(checkset(mogelijk_set)) == 0:
                print("no set")
                mogelijk_set.clear()
                index_set.clear()
                score2+=1
                
            else:
                print("is set")
                score1+=1    #update de score
                counter = tijd+1 #reset de tijd 
  
                #verwijdert de 3 nieuwe kaarten die op display staan vande pot :
                for k in index_set:
                    kaarten[k] = random.choice(pot)
                    pot.remove(kaarten[k])
                
                mogelijk_set.clear()
                index_set.clear()            
                

        pygame.display.update()
    pygame.quit()

game()
