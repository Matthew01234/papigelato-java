print ('Welkom bij Papi Gelato')

hoorentjeofbakje = ''

prijshoorentje = 1.25
totaalAantalHoorentjes = 0

prijsbakje = 0.75
totaalAantalBakjes = 0

prijsbolletjes = 0.95
aantalBolletjes = 0
totaalAantalBolletjes = 0

prijsSlagroom = 0.5
prijsSprinkels = 0.3
prijsCaramelhorentje = 0.0
prijsCaramelbakje = 0.0

totaalAantalSlagroom = 0
totaalAantalSprinkels = 0
totaalAantalCaramel = 0 
totaalAantalTopping = 0
totaal = 0.0

liter = 0
prijsliter = 9.8


def zakelijkbestellen ():
    global liter
    x = 1
    liter = int(input('Hoeveel liter wilt u?: '))
    while x <= liter:
        
        smaakzakelijk = input ('Welke smaak wilt u voor liter nummer '+ str(x) + ' A) Aardbei, C) Chocolade,of V) Vanille?: ').upper()
        if smaakzakelijk in ['A','C','V']:
            x += 1

        else: print ('Sorry dat is geen optie die we aanbieden... '); continue
    bonnentje()



def bonnentje():
    global aantalBolletjes, hoorentjeofbakje, totaalAantalBolletjes, totaalAantalHoorentjes, totaalAantalBakjes,totaalAantalSlagroom, prijsSlagroom,prijsSprinkels,totaalAantalSprinkels , liter, zakelijk, totaal
    totaal = totaalAantalBolletjes * prijsbolletjes + totaalAantalHoorentjes * prijshoorentje + totaalAantalBakjes * prijsbakje + totaalAantalSlagroom * prijsSlagroom + totaalAantalSprinkels * prijsSprinkels * aantalBolletjes +prijsCaramelhorentje + prijsCaramelbakje + liter * prijsliter
    print ('--------------["Papi Gelato"]--------------')
    print ('Bedankt voor je bestelling hierbij uw bon!')
    if aantalBolletjes > 0:
        print (f'bolletjes: {totaalAantalBolletjes} x  {prijsbolletjes} = € ' + str(totaalAantalBolletjes * prijsbolletjes))
    if totaalAantalHoorentjes > 0:
        print (f'Hoorentje: {totaalAantalHoorentjes} x {prijshoorentje} = € '+ str(totaalAantalHoorentjes * prijshoorentje) +'')
    if totaalAantalBakjes > 0:
        print (f'Bakje: {totaalAantalBakjes} x {prijsbakje} = € '+ str(totaalAantalBakjes * prijsbakje) +'')
    if totaalAantalTopping > 0:
        print (f'topping: {totaalAantalTopping} =    €'+ str(totaalAantalSlagroom * prijsSlagroom + totaalAantalSprinkels * prijsSprinkels * aantalBolletjes +prijsCaramelhorentje + prijsCaramelbakje) + '')
    if zakelijk == ('2'):
        print ('Liters ijs: '+ str(liter) +' x '+ str(prijsliter) + '='+ str(prijsliter * liter)+'')  
    print (f'Totaal: € {totaal}')
    if zakelijk == ('2'):
        print (f'btw : {totaal  * 0.06} ')
    print ('--------------["Papi Gelato"]--------------')

def kiesTopping():
    global totaalAantalSlagroom, totaalAantalSprinkels, totaalAantalCaramel, totaalAantalTopping
    topping = input ('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?: ').upper()
    if topping in ['A','B','C','D']:
        if topping == ('A'):
            print ('')

        if topping ==('B'):
            totaalAantalSlagroom += 1
            totaalAantalTopping += 1

        if topping ==('C'):
            totaalAantalSprinkels += 1
            totaalAantalTopping += 1

        if topping ==('D'):
            totaalAantalCaramel += 1
            totaalAantalTopping += 1
        


def bestellen():
    global aantalBolletjes, hoorentjeofbakje, totaalAantalBolletjes, totaalAantalHoorentjes, totaalAantalBakjes, prijsCaramelhorentje, prijsCaramelbakje
    x = True
    while x == True:
        
        aantalBolletjes = int(str(input('Hoeveel bolletjes wil je? ')))
        if aantalBolletjes in [1,2,3]:
            y = 0
            while y < aantalBolletjes:
                y += 1
                smaak =  input ('Welke smaak wilt u voor bolletje nummer '+ str(y) + '? A) Aardbei, C) Chocolade, of V) Vanille? ')
                if smaak.upper() in     "ACMV": print () 
                else: 
                    print ('Sorry dat is geen optie die we aanbieden...')  
                    y -= 1   
                
            kiesTopping()
            hoorentjeofbakje = input('Wilt u deze '+str(aantalBolletjes) +' bolletje(s) in A) een hoorntje of B) een bakje?” ').upper()
            if hoorentjeofbakje == ('A'):
                hoorentjeofbakje = 'A'
                totaalAantalHoorentjes += 1
                prijsCaramelhorentje += 0.6
                print ('Hier is uw hoorentje met '+ str(aantalBolletjes) +' bolletje(s)')
                
            elif hoorentjeofbakje == ('B'):
                hoorentjeofbakje = ('B')
                totaalAantalBakjes += 1
                prijsCaramelbakje += 0.9
                print ('Hier is uw bakje met ' + str(aantalBolletjes) +' bolletje(s)')
                
              
                    
            else: print ('Sorry dat is geen optie die we aanbieden...') 

        elif aantalBolletjes in [4,5,6,7,8]:
            y = 0
            totaalAantalBakjes += 1
            prijsCaramelbakje += 0.9
            hoorentjeofbakje = "B"
            while y < aantalBolletjes:
                y += 1
                smaak =  input ('Welke smaak wilt u voor bolletje nummer '+ str(y) + '? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ')
                if smaak.upper() in "ACMV": print () 
                else: 
                    print ('Sorry dat is geen optie die we aanbieden...')  
                    y -= 1  
            kiesTopping()
        elif aantalBolletjes > int((8)):
            print('Sorry zulke grote bakken hebben we niet')
            bestellen()
        else: print ('Sorry dat is geen optie die we aanbieden...') 
        o = True
        while o == True:
            opnieuwbestellen = input ('Wil je op nieuw bestellen Ja (J) of Nee (N)').upper()
            totaalAantalBolletjes += aantalBolletjes
            if opnieuwbestellen == ('J'):              
                bestellen()
                o = False
            elif opnieuwbestellen == ('N'):
                print ('Bedankt en tot ziens!')
                x = False
                o = False
                bonnentje()
            else: print ('Sorry dat is geen optie die we aanbieden...') 
        return 








zakelijk = input ('Bent u 1) particulier of 2) zakelijk? ') 
if zakelijk == '1':
    bestellen()

if zakelijk == '2':
    zakelijkbestellen()






