<?php            
if (isset($_POST['username']) && isset($_POST['password'])) {		
    if ($_POST['username'] == '11649981' && $_POST['password'] == '584948') {
        echo '<script>alert("dhbw{you_probably_should_not_publish_your_phonecalls}")</script>';
    }
    else {
        echo '<script>alert("Wrong credentials")</script>';
    }
}
?>  
