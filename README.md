# dgdata

A library for easily making requests to files in binary encoded with dgdata

# How to use

Primitively, you can just `fetch` the url
```js
let textEncoding = require('text-encoding');
let dgdata = require('dgdata');

let url = "https://";
request(url, { encoding: null }, (err, res, body) => {
    if (err) {
        // handle error code 
    }
    let decodedBody = dgdata.decode(body).toString('utf-8');
    let json = JSON.parse(decodedBody);
}
```

[Github](https://github.com/hemisemidemipresent/dgdata) 
[npm](https://www.npmjs.com/package/node-dgdata)