const rollTheDice = () => {
    let die1 = Math.floor(Math.random() * 6 + 1)
    let die2 = Math.floor(Math.random() * 6 + 1)
    return die1 + die2
} 

console.log(rollTheDice())

// Math.random() * 6 + 1, dice have 6 sides, Math.random() * 6 + 1, therefore evaluates to some floating point number in the range 0 to less than 7. Math.floor reduces that number to the nearest integer in the range 0 to 6, inclusively, with a (roughly) even distribution.

// If this was Math.random() * 6, the number 6 could never be generated. There are 7 values from 0 to 6, inclusive, so you need to go to 7.