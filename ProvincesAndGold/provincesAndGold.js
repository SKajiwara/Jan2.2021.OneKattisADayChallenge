"use strict";
const readline = require('readline');

function kattis() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })

    var totalWorth = 0;
    var tWorths = [3, 2, 1];
    var tCosts = [6, 3, 0];
    var vCosts = [8, 5, 2];

    rl.on('line', (line) => {
        const gsc = line.split(' ');
        for (var i = 0; i < 3; i++) {
            totalWorth += gsc[i] * tWorths[i];
        }

        if (totalWorth >= vCosts[0])
            console.log("Province or Gold");
        else if (totalWorth >= tCosts[0])
            console.log("Duchy or Gold");
        else if (totalWorth >= vCosts[1])
            console.log("Duchy or Silver");
        else if (totalWorth >= tCosts[1])
            console.log("Estate or Silver");
        else if (totalWorth >= vCosts[2])
            console.log("Estate or Copper");
        else
            console.log("Copper");

        rl.close();
    });
}

if (require.main == module) {
    if (process.argv.lenght > 2 && process.argv[2] == "test") {
        test();
    } else {
        kattis();
    }
} 
