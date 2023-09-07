function logoutButtonClicked(){
    console.log("Logged out") //画面が変わる時にチェックするだけ ログアウトの時
    window.location.href = "/logout"
}

function shoppingclicked(){
    console.log("shopping in") //ショップのページの時
    window.location.href = "/shopping"
}

function getpointclicked(){
    console.log("getpoint in")
    window.location.href = "/play_janken"
}