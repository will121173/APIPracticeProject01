// html中のid=content1のブロックのテキストを、APIから取得した
// {"message":"Hello World"}のmessage=Hello Worldに書き換え

// ↓↓portsタブ・port3000の行のAdressを記入
const apiUrl = 'https://3000-will121173-apipracticep-m4y3pyvx931.ws-us104.gitpod.io';
const element = document.getElementById("content1");
fetch(apiUrl)
.then((res) => res.json())
.then((obj) => {element.innerText = obj.message});
