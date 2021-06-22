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

### real code
```java
public static string Decrypt(byte[] bytes, bool checkCrc = true)
{
            for (int i = 0; i < bytes.Length; i++)
            {
                int num = i - 14;
                if (num >= 0)
                {
                    bytes[i] = (byte)((int)(bytes[i] - 21) - num % 6);
                }
            }
            string @string = Encoding.UTF8.GetString(bytes);
            string header = @string.Substring(0, 14);
            string text = @string.Substring(14);
            if (checkCrc)
            {
                TheRealStephenCypher.check(header, text);
            }
            return text;
        }
        private static string getHexCrc(byte[] bytes)
        {
            uint num = 0u;
            for (int i = 0; i < bytes.Length; i++)
            {
                int num2 = (int)((byte)((uint)bytes[i] ^ num));
                for (int j = 0; j < 8; j++)
                {
                    num2 = (num2 >> 1 ^ (num2 & 1) * -306674912);
                }
                num = (num >> 8 ^ (uint)num2);
            }
            return num.ToString("X").ToLower().PadLeft(8, '0');
        }
        private static void check(string header, string content)
        {
            if (!header.StartsWith("DGDATA"))
            {
                throw new ApplicationException("invalid input - header is not \"DGDATA\"");
            }
            string text = header.Substring(6);
            string hexCrc = TheRealStephenCypher.getHexCrc(Encoding.UTF8.GetBytes(content));
            if (!text.Equals(hexCrc))
            {
                throw new ApplicationException("bad CRC - expected " + hexCrc + ", claimed: " + text);
            }
        }
        public static byte[] Encrypt(byte[] plaintext)
        {
            byte[] array = new byte[14 + plaintext.Length];
            string s = "DGDATA" + TheRealStephenCypher.getHexCrc(plaintext);
            byte[] bytes = Encoding.UTF8.GetBytes(s);
            Array.Copy(bytes, array, bytes.Length);
            for (int i = 0; i < plaintext.Length; i++)
            {
                array[i + 14] = (byte)((int)(plaintext[i] + 21) + i % 6);
            }
            return array;
        }
```
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

