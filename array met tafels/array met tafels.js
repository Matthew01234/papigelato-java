var tafels = [2,4,6,8]
var h2 = []
for (var count = 0; count < tafels.length;count++){
    for (var count2 = 1; count2 <= 10;count2++){
        h2.push(tafels[count] * count2);
    }
}
document.getElementById('h2').innerHTML = h2