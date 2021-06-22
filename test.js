const fetch = require("node-fetch");
var fs = require('fs');

let grocall = JSON.stringify({"gromethod": "lookup", "parameter": "items", "item_id":[12998]});
let apiURL = `http://10.0.0.249:80/groflaskapi/${grocall}`;

let api_key = fs.readFileSync('key.txt').toString().trim();
console.log(api_key);

fetch(
    apiURL, {
    method: 'POST', 
    headers: {"API_KEY":api_key}
    })
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        let replyJSON = JSON.parse(text)
        console.log(replyJSON); 
    })
    .catch((response)=>{
        console.log(response);
    });

