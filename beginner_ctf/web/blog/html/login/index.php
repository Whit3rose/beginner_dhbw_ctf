<?php

if (isset($_GET["sessionUser"])) {
    $cookie = $_GET["sessionUser"];
    if ($cookie == "admin") {
    	echo "dhbw{schlechter_keks}";
    } else {
    	echo "user " + $cookie + " is not a valid user";
    }
}

if (isset($_GET["username"]) && isset($_GET["password"])) {
    echo "invalid username or password";
}
?>
