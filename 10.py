$prod_id = $_GET["prod_id"];

$sql = "SELECT * FROM Products WHERE product_id = " . $prod_id;
