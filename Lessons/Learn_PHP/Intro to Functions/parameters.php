<?php
// Write your code below:
function increaseEnthusiasm
($str_param)
{
    return $str_param . "!";
}

function repeatThreeTimes
($str_param)
{
    return $str_param .
$str_param . $str_param;
}

echo increaseEnthusiasm("oh");
echo repeatThreeTimes("wow");

echo increaseEnthusiasm
(repeatThreeTimes("hai"));