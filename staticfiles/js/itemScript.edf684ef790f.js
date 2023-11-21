// function updateCartItemCount() {
//   fetch("/cartItemCount/")
//     .then(response => response.json())
//     .then(data => {
//       document.getElementById("numOfItems").textContent = data.numOfItems;
//     })
//     .catch(error => console.log(error));
// }

// // Aggiungi l'handler per l'evento di click del pulsante "Add to Cart"
// document.getElementById("add-to-cart-btn").addEventListener("click", function(event) {
//   event.preventDefault();
//   const itemId = event.target.value;
//   // Esegui qui la logica per aggiungere l'elemento al carrello
//   // ...

//   // Aggiorna il numero di elementi nel carrello
//   updateCartItemCount();
// });

// // Chiamare questa funzione all'avvio della pagina per aggiornare il numero di elementi nel carrello
// updateCartItemCount();

