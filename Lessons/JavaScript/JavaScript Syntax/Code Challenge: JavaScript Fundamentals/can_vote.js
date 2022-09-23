const canVote = age => {
    if (age >= 18) {
        return true
    } else {
        return false
    }
}
/*
Alternate solutions:

As a function declaration:
function canVote(age) {
    if (age >= 18) {
        return true
    } else {
        return false
    }
}

Using a ternary:
const canVote = (age) => age >= 18 ? true : false
*/

console.log(canVote(19))