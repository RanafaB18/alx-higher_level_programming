#!/usr/bin/node

exports.esrever = function (list) {
    const len = list.length
    const reversedArray = []
    for (let i = len - 1; i >= 0; i--){
        reversedArray[(len-1) - i] = list[i]
    }
    return reversedArray
}
