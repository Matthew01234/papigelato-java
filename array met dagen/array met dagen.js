const dagen = ['Maandag ','Dinsdag ','Woensdag ','Donderdag ','Vrijdag ','Zaterdag ','Zondag '];

document.getElementById('dagen').innerHTML = 'Alle dagen van de week zijn: '+ dagen
document.getElementById('werkdagen').innerHTML = "De werkdagen zijn:" + dagen.slice(0,5)
document.getElementById('weekenddagen').innerHTML = "De weekenddagen zijn: "+ dagen.slice(5,7)
document.getElementById('ReversedDagen').innerHTML = "Alle dagen van de week in omgekeerde volgorde zijn: " + dagen.reverse()
document.getElementById('ReversedWerkDagen').innerHTML = "De werkdagen in omgekeerde volgorde zijn: "+ dagen.slice(2,7)
document.getElementById('ReversedWeekendDagen').innerHTML = "De weekenddagen in omgekeerde volgorde zijn: "+ dagen.slice(0  ,2)