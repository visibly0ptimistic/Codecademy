const logs = [];
console.log = (val) => {logs.push(val)} 
const { expect } = require('chai')
const rewire = require('rewire');
const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

describe('', function () {
    it('', function () {
        let appModule;
        try {
            appModule = rewire("../app.js")
        } catch (e) {
            expect(true, 'Try checking your code again. You likely have a syntax error.').to.equal(false);
        }
        let usingSTO
        try {
            usingSTO = appModule.__get__("usingSTO");
        } catch (e) {
            expect(true, 'Did you create `usingSTO()`?').to.equal(false);
        }
        expect(usingSTO, "`usingSTO()` should be a function.").to.be.an.instanceOf(Function);
        
      usingSTO()
        expect(logs[logs.length-1], "Your `usingSTO()` function should log a string to the console.").to.be.a('string');
    });
});