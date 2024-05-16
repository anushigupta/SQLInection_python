$username = $_POST["username"];
$password = $_POST["password"];

$sql = "SELECT * FROM Users WHERE username = \"" . $username . "\" AND password = \"" . $password . "\"";
