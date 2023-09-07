var count = 0
var productIdArr = [];
function additionclicked(productId){
    var cartCount = document.getElementById("cartCount");
    count++;
    productIdArr.push(productId);
    console.log(productIdArr);
    cartCount.textContent = count;
}

function goToCart(){
    $.ajax({
        type: "POST",
        url: "/cart-proc",
        contentType: "application/json",
        data: JSON.stringify({ 'productIdArr': productIdArr }),
        success: function(response) {
            console.log(response);
            if(response.message == "SUCCESS"){
                window.location.href = "/cart"
            }
        }
    });
}