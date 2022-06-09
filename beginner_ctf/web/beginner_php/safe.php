<?php
$PASSWORD = 'dhbw{i_should_not_use_insecure_functions}';
if (isset($_POST['password'])) {
	$password = $_POST['password'];
	if (strcmp($password, $PASSWORD) == 0) {
		echo $PASSWORD;
	}
	else {
		echo 'Wrong Password';
	}
}
?>
