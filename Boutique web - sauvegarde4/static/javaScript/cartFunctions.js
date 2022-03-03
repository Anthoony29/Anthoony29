function removeProductCart(idProduct){
    fetch(`${window.origin}/removeProductCart/${idProduct}`,{method : "POST"})
    .then(function(data){
        window.location.href=window.location.href
    })
};

function sumPriceAllProducts(){
    const tagGetPriceElements = document.getElementsByClassName('js-priceProductSum');
    let total = 0

    for(i=0; i<tagGetPriceElements.length; i++){
        total += parseInt(tagGetPriceElements[i].innerHTML)
    }

    document.getElementById('priceNoTaxe').innerText = total+' €';
    let taxe = total*0.2
    document.getElementById('taxe').innerText = taxe+' €';

    let totalPrice = total+taxe
    document.getElementById('totalPrice').innerText = totalPrice+' €'

}

sumPriceAllProducts()