var counter = 0
var arrayEen = [1,2,3,4,5,6,7,8,9,10];
var arrayTwee = [2,4,6,8,10,12,14,16,18,20];
var h1 = [];
var h2 = [];
var h3 = [];
var h4 = [];


for(var i = 0;i<=arrayTwee.length-1;i++)
  h1.push(arrayEen[i] - arrayTwee[i]);

for(var i = 0;i<=arrayTwee.length-1;i++)
    h2.push(arrayEen[i] + arrayTwee[i]);

for(var i = 0;i<=arrayTwee.length-1;i++)
    h3.push(arrayEen[i] / arrayTwee[i]);

for(var i = 0;i<=arrayTwee.length-1;i++)
    h4.push(arrayEen[i] * arrayTwee[i]);

document.getElementById('h1').innerHTML = h1
document.getElementById('h2').innerHTML = h2
document.getElementById('h3').innerHTML = h3
document.getElementById('h4').innerHTML = h4