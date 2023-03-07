count = prompt('Hoeveel nummers wilt u in de pyramide stoppen?')

var nummers = []
for (var i = 0; i <= count;i++){
    nummers.push(i);
    var p = document.createElement('p')
    p.innerHTML = nummers
    document.getElementById('body').appendChild(p)
}
