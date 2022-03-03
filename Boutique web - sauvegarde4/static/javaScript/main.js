var ProductImg = document.getElementById("ProductImg");
var SmallImg = document.getElementsByClassName("small-img");

SmallImg[0].onclick = function()
{
    ProductImg.src = SmallImg[0].src;
}
SmallImg[1].onclick = function()
{
    ProductImg.src = SmallImg[1].src;
}
SmallImg[2].onclick = function()
{
    ProductImg.src = SmallImg[2].src;
}
SmallImg[3].onclick = function()
{
    ProductImg.src = SmallImg[3].src;
}


var btnAddCart = document.getElementsByClassName("js-eventCart");


document.getElementById('js-eventCart').addEventListener('click', (event) => {
    //Récupère la valeur (en gros l'id) de 'data-idProduct' du boutton ajouter au panier
    var attribute = event.target.getAttribute("data-idProduct");

    //Fait la requête au serveur pour ajouter au panier avec l'id récuperé(attribute)
    fetch(`${window.origin}/addCart/${attribute}`,{method : "POST"});
});

var MenuItems = document.getElementById("MenuItems");

MenuItems.style.maxHeight = "0px";

function menutoggle(){
    if(MenuItems.style.maxHeight == "0px")
        {
            MenuItems.style.maxHeight = "200px";
        }
    else
        {
            MenuItems.style.maxHeight = "0px"
        }
}

