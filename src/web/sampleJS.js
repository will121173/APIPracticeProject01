// html中のid=content1のブロックのテキストを、APIから取得した
// {"message":"Hello World"}のmessage=Hello Worldに書き換え

// ↓↓portsタブ・port3000の行のAdressを記入
const apiUrl = 'https://～～～～～～～～～～～～～～～～.gitpod.io';
const element = document.getElementById("content1");
fetch(apiUrl)
.then((res) => res.json())
.then((obj) => {element.innerText = obj.message});
