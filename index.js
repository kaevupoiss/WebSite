function menuFun() {
    var x = document.getElementById("menu").style.width;
    if (x === "0px") {
        document.getElementById("menu").style.width = "250px";
        document.getElementById("mainwrapper").style.marginLeft = "250px";
        //document.getElementsByClassName("header").style.left = "250px";
    } else {
        document.getElementById("menu").style.width = "0px";
        document.getElementById("mainwrapper").style.marginLeft = "0px";
        //document.getElementsByClassName("header").style.left = "0px";
    }
}
