<?php
  
$annualExpenses = [
    "vacations" => 1000,
    "carRepairs" => 1000,    
];

$monthlyExpenses = [
    "rent" => 1500,
    "utilities" => 200,
    "healthInsurance" => 200
];

$grossSalary = 48150;
$socialSecurity = $grossSalary * .062;

$incomeSegments = [[9700, .88], [29775, .78], [8675, .76]];

// Write your code below:


// Taxes
$netIncome = ($incomeSegments[0][0] * $incomeSegments[0][1]) + ($incomeSegments[1][0] * $incomeSegments[1][1]) + ($incomeSegments[2][0] * $incomeSegments[2][1]);

$netIncome = $netIncome - $socialSecurity;

$annualIncome = $netIncome;

echo "Annual income before deducting annual expenses:\n$annualIncome\n";


// Annual Expenses
$annualIncome = $annualIncome - $annualExpenses["vacations"] - $annualExpenses["carRepairs"];

echo "\nAnnual income after deducting annual expenses:\n$annualIncome\n";


// Monthly Expenses
$monthlyIncome = $annualIncome / 12;

echo "\nMonthly income before deducting monthly expenses:\n$monthlyIncome\n";

$monthlyIncome = $monthlyIncome - $monthlyExpenses["rent"] - $monthlyExpenses["utilities"] - $monthlyExpenses["healthInsurance"];

echo "\nMonthly income after deducting monthly expenses:\n$monthlyIncome\n";

// Weekly Expenses
$weeklyIncome = $monthlyIncome / 4.33;

echo "\nWeekly income before deducting weekly expenses:\n$weeklyIncome\n";

$weeklyExpenses = [
    "gas" => 25,
    "food" => 90,
    "entertainment" => 47
];

$weeklyIncome = $weeklyIncome - $weeklyExpenses["gas"] - $weeklyExpenses["food"] - $weeklyExpenses["entertainment"];

echo "\nWeekly income after deducting weekly expenses:\n$weeklyIncome\n";


// Savings
$savings = $weeklyIncome * 52;

echo "\nSavings:\n$savings\n";