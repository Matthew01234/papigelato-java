count = prompt('Hoeveel nummers wilt u in de pyramide stoppen?')


for (var i = 0; i <= count;i++){
    var nummers = [...Array(count - i).keys()].join('')
    var p = document.createElement('p')
    p.innerHTML = nummers
    document.getElementById('body').appendChild(p)
}
