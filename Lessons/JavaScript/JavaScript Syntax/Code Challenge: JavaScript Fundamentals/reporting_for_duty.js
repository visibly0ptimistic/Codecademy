const reportingForDuty = (rank, lastName) => `${rank} ${lastName} reporting for duty!`

/*
Using string concatenation:
const reportingForDuty = (rank, lastName) => rank + " " + lastName + " " + "reporting for duty!"

As a function declaration:
function reportingForDuty(rank, lastName) {
    return `${rank} ${lastName} reporting for duty!`
}
*/

console.log(reportingForDuty("Lieutenant", "Ejiasi"))