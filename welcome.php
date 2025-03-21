<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST["username"];
        $number1 = $_POST["number1"];
        $number2 = $_POST["number2"];
        echo "Hello, $username!";
        echo "<br>";
        echo "The sum of $number1 and $number2 is " . ($number1 + $number2);
    }
?>