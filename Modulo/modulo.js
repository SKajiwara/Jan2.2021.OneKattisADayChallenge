"use strict";
const readline = require('readline');

function kattis() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })

    var i = 1, num = 0, numMod42 = 0, distMods = [];
    rl.on('line', (line) => {
        num = Number(line);
        numMod42 = num % 42;

        if (distMods.indexOf(numMod42) === -1)
            distMods.push(numMod42);

        if (i == 10) {
            console.log(distMods.length);
            rl.close();
        }
        i += 1;
    })
}

function test() {
    console.log("test");
}

if (require.main == module) {
    if (process.argv.length > 2 && process.argv[2] == "test")
        test();
    else
        kattis();
}