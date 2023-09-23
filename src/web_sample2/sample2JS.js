// ↓↓portsタブ・port3000の行のAdressを記入
const apiUrl = 'https://3000-will121173-apipracticep-7tnb9yycuqf.ws-us104.gitpod.io';

const tableElement = document.getElementById("tableElement");
function createRecord(event) {
    const requestBody = {
        price : document.getElementById("price").value,
        itemName : document.getElementById("itemName").value,
        accountingDate : new Date().toLocaleDateString("ja-JP", {year: "numeric",month: "2-digit",day: "2-digit"}).replaceAll('/', '-'),
        userId : document.getElementById("userid").value
    };
    console.log(requestBody);
    fetch(apiUrl+"/records/",{
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(requestBody),})
        .then((result) => result.json())
        .then((obj) => {
            console.log(obj);
        })
}


function showRecords(event) {
    var uid = document.getElementById("userid").value;
    (uid!="") ? urlstring = "?userid="+uid: urlstring="";
    fetch(apiUrl+"/records/"+urlstring)
    .then((result) => result.json())
    .then((obj) => {
        console.log(obj);
        var s = '<table class="recordlist"><tr><th>Price</th><th>ItemName</th><th>AccoutingDate</th><th>User</th></tr>'
        obj.forEach(es => {
            s = s + '<tr>' +
            '<td>' + es[0] + '</td>' +
            '<td>' + es[1] + '</td>' +
            '<td>' + es[2] + '</td>' +
            '<td>' + es[3] + '</td>' +
            '</tr>';});
        s=s+'</table>';
        console.log(s);
        tableElement.innerHTML = s;
    });
}

