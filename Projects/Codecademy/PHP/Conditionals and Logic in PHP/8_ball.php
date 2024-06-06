<?php

function magic8Ball() {
    echo "What is your question?\n";


    $question = readline(">> ");

    echo "You asked: $question\n";

    $choice = rand(1, 10);
    echo "choice is $choice\n";

    if ($choice === 1) {
        echo "It is certain.\n";
    }   elseif ($choice === 2) {
        echo "It is decidedly so.\n";
    }   elseif ($choice === 3) {
        echo "Without a doubt.\n";
    }   elseif ($choice === 4) {
        echo "Yes - definitely.\n";
    }   elseif ($choice === 5) {
        echo "You may rely on it.\n";
    }   elseif ($choice === 6) {
        echo "As I see it, yes.\n";
    }   elseif ($choice === 7) {
        echo "Most likely.\n";
    }   elseif ($choice === 8) {
        echo "Outlook good.\n";
    }   elseif ($choice === 9) {
        echo "Yes.\n";
    }   elseif ($choice === 10) {
        echo "Signs point to yes.\n";

}
}

magic8Ball();