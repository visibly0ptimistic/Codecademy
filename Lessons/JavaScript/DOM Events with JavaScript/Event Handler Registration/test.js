console.log = function() {};
const fs = require('fs');
const { expect } = require('chai');
const Structured = require('structured');

// This filepath does not need to go up a directory level
const code = fs.readFileSync('main.js', 'utf-8');

describe('', function() {
  it('', function() {
    const structureOne = () => {
      readMore.addEventListener();
    };
    
    const structureTwo = () => {
      readMore.addEventListener($event);
    }
    
    const structureThree = () => {
      readMore.addEventListener($event, $handler);
    }
    
    let varCallbacks = [
      function($event){
        if($event.value !== 'click'){
        	return {failure: "Did you pass in `'click'` as first argument of the `addEventListener()` method?"};
        }
      	return true;
      }
    ]
    
    let handlerCallbacks = {
      "$event, $handler": function(event, handler){
        if(handler.name !== 'showInfo'){
          return {failure: "Did you pass in `showInfo` as the event handler function?"}
        }
      }
    }

    const isMatchOne = Structured.match(code, structureOne);
    const isMatchTwo = Structured.match(code, structureTwo, {varCallbacks});
    const isMatchThree = Structured.match(code, structureThree, {varCallbacks: handlerCallbacks});

    expect(isMatchOne, 'Did you add the `addEventListener()` method to the `readMore` element?').to.not.be.false;
    expect(isMatchTwo, varCallbacks.failure || 'Did you add the event type to the `addEventListener()` method of the `readMore` element?').to.not.be.false;
    expect(isMatchThree, varCallbacks.failure || 'Did you correctly assign an event handler function as the second argument of `addEventListener()` function?').to.not.be.false;
  });
});
