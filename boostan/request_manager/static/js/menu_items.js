// the side menu items will be loaded here. they are different for teachers students and personnel

$(document).ready(function () {

    // in this part I complete the side menu items with an API.
    $.ajax({
        url: "http://localhost:8000/requests/sideMenu/",
        type: "GET",
        success: function (data){
            document.getElementById("sideul").innerHTML = data.sideMenu;
            window.alert("سلام " + data.name);
        },
        error: function () {
            window.alert(" مشکلی پیش آمد، دوباره وارد شوید.");
            window.location.reload();
        }
    })
})