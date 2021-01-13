"use strict"
const readline = require('readline');
const assert = require('assert').strict;

Object.defineProperties(Array.prototype, {
    count: {
        value: function (query) {
            /* 
               Counts number of occurrences of query in array, an integer >= 0 
               Uses the javascript == notion of equality.
            */
            var count = 0;
            for (let i = 0; i < this.length; i++)
                if (this[i] == query)
                    count++;
            return count;
        }
    }
});

function answer(cord) {
    console.log(cord[0], cord[1]);
}

function findCord(Xs, Ys) {
    var x, y;

    for (var i = 0; i < 3; i++) {
        // console.log(Xs[i], " : ", Xs.count(Xs[i]));
        // console.log(Ys[i], " : ", Ys.count(Ys[i]));

        if (Xs.count(Xs[i]) == 1) {
            x = Xs[i]
            // console.log('x:', x)
        }
        if (Ys.count(Ys[i]) == 1) {
            y = Ys[i]
            // console.log('y:', y)
        }
    }
    return [x, y]
}

function test() {

}

function solve() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    var count = 1;
    var cord = [];
    var xy;
    var Xs = [];
    var Ys = [];

    rl.on('line', (line) => {
        xy = line.split(' ')
        Xs.push(xy[0]);
        Ys.push(xy[1]);
        if (count == 3) {

            cord = findCord(Xs, Ys);
            answer(cord);
            rl.close();
        }
        count += 1;
    })

}

if (require.main == module) {
    if (process.argv.length > 2 && process.argv[2] == 'test')
        test();
    else
        solve();
}