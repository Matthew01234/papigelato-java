var customerinfo = {
    'particulier/zakelijk' : 0,
    'typeijs' : 0,
    'aantaltypeijs' : 0,
    'smaken' : {'aardbei':0,'chocolade':0,'vanille':0,},
    'topping' : {'geen':0,'slagroom':0,'sprinkels':0,'caramel':0,}
}



function startfunctie(){
    customerinfo['particulier/zakelijk'] = prompt('Welkom bij Papi Gelato, \n Bent u 1) particulier of 2) zakelijk?')

    if (customerinfo['particulier/zakelijk'] == 1) {
        customerinfo['aantaltypeijs'] = prompt('Hoeveel bolletjes wil je?')
        smaken()
    }
    
    if (customerinfo['particulier/zakelijk'] == 2) {
        customerinfo['aantaltypeijs'] = prompt('Hoeveel liter wil je?')
        smaken()   
    }
}

function smaken (){
    for (var i = 0; customerinfo['aantaltypeijs'] >= i;i++){
        gekozensmaak = prompt('welke smaak wilt u?  aardbei / chocolade / vanille' )
        if (gekozensmaak == 'aardbei') {
            customerinfo['smaken']['aardbei'] += 1
        }
        if (gekozensmaak == 'chocolade') {
            customerinfo['smaken']['chocolade'] += 1
        }
        if (gekozensmaak == 'vanille') {
            customerinfo['smaken']['vanille'] += 1
        }
    }
    topping()
}
function topping (){
    for (var i = 0; customerinfo['aantaltypeijs'] >= i;i++){
        gekozentopping = prompt('welke topping wilt u? geen / slagroom / sprinkels / caramel')
        if (gekozentopping == 'geen') {
            customerinfo['topping']['geen'] += 1
        }
        if (gekozentopping == 'slagroom') {
            customerinfo['topping']['Slagroom'] += 1
        }
        if (gekozentopping == 'sprinkels') {
            customerinfo['topping']['sprinkels'] += 1
        }
        if (gekozentopping == 'caramel') {
            customerinfo['topping']['caramel'] += 1
        }
    }
    bon()
}
function bon(){
    if (customerinfo['particulier/zakelijk'] == 1) {
        alert( 'Bedankt voor het bestellen bij Papi Gelato!\n -----------------------------------------------\nHier is uw bon:\n Aantal bolletjes = '+ (customerinfo['aantaltypeijs']) +' x 0.95 =  \n -----------------------------------------------\n'
        )
 
    }
    if (customerinfo['particulier/zakelijk'] == 2) {
        alert( 'Bedankt voor het bestellen bij Papi Gelato!\n -----------------------------------------------\nHier is uw bon:\n Aantal liters = '+ (customerinfo['aantaltypeijs']) +' x 9.8 =  \n -----------------------------------------------\n'
        )
    }
}

startfunctie()

