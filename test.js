let dgdata = require('dgdata');

let url =
    'https://priority-static-api.nkstatic.com/storage/static/multi?appid=11&files=races/Caught_outside_the_loop';
request(url, { encoding: null }, (err, res, body) => {
    if (err) {
        // handle error code
    }
    let decodedBody = dgdata.decode(body).toString('utf-8');
    let json = JSON.parse(decodedBody);
    console.log(json);
});
