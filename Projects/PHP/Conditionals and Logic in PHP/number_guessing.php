<?php
$play_count = 0;
$correct_guesses = 0;
$guess_high = 0;
$guess_low = 0;

echo "I'm going to think of a number between 1 and 10 (inclusive). Try to guess it!\n";

function guessNumber() {
    global $play_count;
    global $correct_guesses;
    global $guess_high;
    global $guess_low;
    $play_count++;
    $number = rand(1, 10);
    echo "I'm thinking of a number between 1 and 10 (inclusive). Try to guess it!\n";
    $guess = readline(">> ");
    if ($guess == $number) {
        echo "You guessed it! My number was $number.\n";
        $correct_guesses++;
    }   elseif ($guess > $number) {
        echo "Too high. My number was $number.\n";
        $guess_high++;
    }   elseif ($guess < $number) {
        echo "Too low. My number was $number.\n";
        $guess_low++;
    }
}

guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();

$percent_correct = $correct_guesses / $play_count * 100;

echo "You guessed the number correctly $correct_guesses out of $play_count times. That's $percent_correct% correct.\n";

echo "You guessed too high $guess_high times.\n";
echo "You guessed too low $guess_low times.\n";

