// https://docs.github.com/en/copilot/getting-started-with-github-copilot/getting-started-with-github-copilot-in-visual-studio-code

/* 
GitHub Copilot provides suggestions for numerous languages and a wide variety of frameworks,
but it works especially well for Python, JavaScript, TypeScript, Ruby, Go, C# and C++.
The following samples are in JavaScript, but other languages will work similarly.

Optionally, you can see alternative suggestions, if any are available.

OS        See next suggestion        See previous suggestion
macOS          Option (⌥) or Alt+]          Option (⌥) or Alt+[ 
Windows        Ctrl+]                       Ctrl+[

To open a new tab with multiple additional options, press Ctrl+Enter.
To accept a suggestion, above the suggestion, click Accept Solution. To reject all suggestions, close the tab. */

// function to calculate days between dates
function calculateDaysBetweenDates(begin, end) {
  const date1 = new Date(begin);
  const date2 = new Date(end);
  const timeDiff = Math.abs(date2.getTime() - date1.getTime());
  return Math.ceil(timeDiff / (1000 * 3600 * 24));
}

/*
I described what I wanted to do using natural language within a comment,
and GitHub Copilot suggests the code to accomplish that goal. 

GitHub Copilot can even generate suggestions for APIs and frameworks.
*/

// function for todays date
function todaysDate() {
  const today = new Date();
  const dd = String(today.getDate()).padStart(2, '0');
  const mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  const yyyy = today.getFullYear();
  return yyyy + '-' + mm + '-' + dd;
}

// function to convert days to years
function daysToYears(days) {
  return days / 365;
}

const days_lived = (calculateDaysBetweenDates('1998-11-27', todaysDate()));

console.log(calculateDaysBetweenDates('1998-11-27', todaysDate()))
console.log(daysToYears(days_lived));