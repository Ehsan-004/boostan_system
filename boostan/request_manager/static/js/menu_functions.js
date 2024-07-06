// each item in side menu has some functionality, the functionality will be loaded here

function profile(){
    // event.preventDefault(); // Prevent the default
    $.ajax({
        url: "http://localhost:8000/requests/profile/",
        method: "GET",
        success: function (data) {
            document.getElementById("display_content").innerHTML = data.structure;
        },
        error: function () {
            alert("مشکلی پیش آمده است")
        }
    })

    // in this part it is possible to choose a menu item and add a border to chosen one
    const clickedLink = event.target;
    const sidebarLinks = document.querySelectorAll('#sideul li a');
    sidebarLinks.forEach((link) => {
        link.classList.remove('active');
    });
    // Add the 'active' class to the clicked link
    clickedLink.classList.add('active');
}

function admin_all_members(){
    $.ajax({
        url: "http://localhost:8000/requests/admin_all/",
        method: "GET",
        success: function (data){
            document.getElementById("display_content").innerHTML = data.structure;
        },
        error: function (){
            alert("مشکلی پیش آمده است")
        }
    })
}