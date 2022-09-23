const agreeOrDisagree = (first, second) => {
    if (first === second) {
        return 'You agree!'
    } else {
        return 'You disagree!'
    }
}

/*

As a function declaration:
function agreeOrDisagree(first, second) {
    if (first === second) {
        return 'You agree!'
    } else {
        return 'You disagree!'
    }
}

As a ternary: 
const agreeOrDisagree = (first, second) => (first === second) ? 'You agree!' : 'You disagree!'
*/

console.log(agreeOrDisagree("yep", "yep")) 