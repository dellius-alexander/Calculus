#!/usr/bin/env node
// import http from 'http';
import http from 'http';

console.log('Starting healthcheck...');

const options = {
    host : process.env.HOSTNAME || '127.0.0.1',
    port : process.env.PORT || 3000,
    timeout : 2000
};

const request = http.request(options, (res) => {
    console.log(`STATUS: ${res.statusCode}`);
    if (res.statusCode == 200) {
        process.exit(0);
    }
    else {
        process.exit(1);
    }
});

request.on('error', function(err) {
    console.log('ERROR');
    process.exit(1);
});

request.end();