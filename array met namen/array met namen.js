var count = 0
namen = []
count = prompt('Hoeveel namen wilt u in de array stoppen?')
for (var i = 0; i <= count;i++){
    ingevuldenamen = prompt('Vul hier de namen 1 voor 1 in:')
    namen.push(ingevuldenamen)
}
document.getElementById('namen').innerHTML = 'Alle namen: '+ namen
document.getElementById('namenreversed').innerHTML = "De namen reversed zijn:" + namen.reverse()
