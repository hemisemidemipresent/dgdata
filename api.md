# Introduction

a guide on how to see how NK communicates with its servers is found [here](https://youtu.be/SJ4Tczw1LyA)
please do contribute to this list

# Encodings

## base64 (atob, zlib)

This is sometimes used by Ninja Kiwi, although usually for older features. Newer API settings are POST API endpoints (impossible to use externally) or DGDATA encoding, the origin of which is unclear.

**try this when there are no "�" when you open the link in the browser**
```js
const request = require('request');
const zlib = require('zlib');
const atob = require('atob');
request(
    'url',
    { json: true },
    (err, res, body) => {
        if (err) {
            return console.log(err);
        }
        let data = JSON.stringify(body, null, 4);
        let g = base64ToArrayBuffer(data);
        zlib.inflate(g, (err, buffer) => {
            if (err) {
                console.log('err happened');
            }
            let object = JSON.parse(buffer.toString('utf8')); // the object
        });
    }
);
function base64ToArrayBuffer(base64) {
    let binary_string = atob(base64);
    let len = binary_string.length;
    let bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
        bytes[i] = binary_string.charCodeAt(i);
    }
    return bytes.buffer;
}
```

## DGDATA

this is more frequently used.

**use this if when you open the link in your browser when the text starts with `DGDATA` and has numerous "�"s**

this module was made to make decoding such links much, much easier
```js
let dgdata = require('node-dgdata');
let request = require('request');
request(url, { encoding: null }, (err, res, body) => {
    if (err) {
        // handle error code
    }
    let decodedBody = dgdata.decode(body).toString('utf-8');
});
```

### history*

there is a non-github repo by the name of... `dgdata` (this package name is called `node-dgdata`). Currently all it does is rickrolls you, but one iteration ago it actually contained code that decrypted the dgdata. The code can be found [here](). This is simply a more extensive presentation of that code

there is also the same code, but in a repl.it project that can be found [here](https://replit.com/@oorzkws/CarefreeUnwrittenSubversion#index.js)

It is unknown whether these are really smart people with c# decompilers that decompiled NK's dgdata decoder called `TheStephenCypher`
# Races

## race leaderboard

this is the static leaderboard that updates the same way everyone else outside top 100 sees it. In some NK patch notes they mention this.
the live t100 lb is accessed via POST and is hence unreachable.
NK does not have an endpoint to viewing who is at nth place, only what place a user is, which is also via POST and hence unreachable.

`url: https://priority-static-api.nkstatic.com/storage/static/multi?appid=11&files=races/Caught_outside_the_loop`

## race information

for tower data, etc

`url: https://priority-static-api.nkstatic.com/storage/static/multi?appid=11&files=races/RACEID`

# Challenge code

`url: https://static-api.nkstatic.com/appdocs/11/es/challenges/CHALLENGECODE}`

encoding: base64

