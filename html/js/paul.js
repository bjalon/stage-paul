var max = 124;
var nbre1 = Math.floor(Math.random() * max);
var nbre2 = Math.floor(Math.random() * max);

document.getElementById("nombre1").innerHTML = nbre1;
document.getElementById("nombre2").innerHTML = nbre2;

var expectedSomme = nbre1 + nbre2;

var validationSomme = document.getElementById("validationSomme");
var somme = document.getElementById("somme1");

validationSomme.onclick = checkSomme
somme.onkeypress = (event) => {
	if (event.code == 'Enter' || event.code == 'NumpadEnter') {
		checkSomme();
	}
}

function checkSomme() {
	if (expectedSomme != parseInt(somme.value)) {
		alert("T'es trop nul !")
	} else {
		alert("Bravo !")
	}
}

var expectedDifference = nbre1 - nbre2;

var validationDifference = document.getElementById("validationDifference");

validationDifference.onclick = () => {
	
	var difference = document.getElementById("difference1");
	
	if (expectedDifference != parseInt(difference.value)) {
		alert("T'es trop nul !")
	} else {
		alert("Bravo !")
	}
}



var expectedProduit = nbre1 * nbre2;

var validationProduit = document.getElementById("validationProduit");

validationProduit.onclick = () => {
	var produit = document.getElementById("produit1");
	if (expectedProduit != parseInt(produit.value)) {
		alert("T'es trop nul !")
	} else {
		alert("Bravo !")
	}
}





