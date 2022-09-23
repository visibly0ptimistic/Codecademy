const toEmoticon = meaning => {
    switch (meaning) {
        case 'shrug':
            return '¯\\_(ツ)_/¯'
        case 'smiley face':
            return ':)';
        case 'frown face':
            return ':(';
        case 'wink face':
            return ';)';
        case 'heart':
            return '<3';
        default:
            return '¯\\_(ツ)_/¯';
    }
}
/*
As a function declaration: 
function toEmoticon(meaning) {
    switch (meaning) {
        case 'shrug':
            return '¯\\_(ツ)_/¯'
        case 'smiley face':
            return ':)';
        case 'frown face':
            return ':(';
        case 'wink face':
            return ';)';
        case 'heart':
            return '<3';
        default:
            return '¯\\_(ツ)_/¯';
    }
}
*/
console.log(toEmoticon("whatever"))