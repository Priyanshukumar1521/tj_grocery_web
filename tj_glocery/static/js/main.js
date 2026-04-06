/* =========================
   TJ GROCERY CART SYSTEM
========================= */

let cart = JSON.parse(localStorage.getItem("cart")) || [];


/* SAVE CART */
function saveCart() {
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}


/* ADD TO CART */
function addToCart(id) {

    let product = products.find(p => p.id === id);
    if (!product) return;

    let item = cart.find(i => i.id === id);

    if (item) {
        item.qty++;
    } else {
        cart.push({ ...product, qty: 1 });
    }

    saveCart();
    alert(product.name + " added to cart ✅");
}


/* REMOVE ITEM */
function removeItem(id) {
    cart = cart.filter(i => i.id !== id);
    saveCart();
    displayCart();
}


/* INCREASE QTY */
function increaseQty(id){
    let item = cart.find(i => i.id === id);
    if(item){
        item.qty++;
        saveCart();
        displayCart();
    }
}


/* DECREASE QTY */
function decreaseQty(id){
    let item = cart.find(i => i.id === id);

    if(item){
        item.qty--;

        if(item.qty <= 0){
            removeItem(id);
        }else{
            saveCart();
            displayCart();
        }
    }
}


/* CART COUNT */
function updateCartCount() {
    let el = document.getElementById("cart-count");

    if (el) {
        let count = cart.reduce((a, b) => a + b.qty, 0);
        el.innerText = count;
    }
}


/* =========================
   PRODUCT LIST
========================= */

function renderProducts(list) {

    let container = document.getElementById("product-list");

    container.innerHTML = list.map(p => `
        <div class="col-md-3 mt-3">
            <div class="card text-center shadow-sm">

                <img src="${p.image}" class="card-img-top">

                <div class="card-body">
                    <h5>${p.name}</h5>
                    <p class="fw-bold">₹${p.price}</p>

                    <a href="product.html?id=${p.id}"
                    class="btn btn-primary btn-sm">View</a>

                    <button onclick="addToCart(${p.id})"
                    class="btn btn-success btn-sm">
                    Add 🛒
                    </button>
                </div>
            </div>
        </div>
    `).join("");
}


/* =========================
   CART PAGE
========================= */

function displayCart(){

    let table = document.getElementById("cart-items");
    if(!table) return;

    table.innerHTML = "";

    if(cart.length === 0){
        table.innerHTML =
        `<tr><td colspan="4" class="text-center">
        Cart Empty 🛒
        </td></tr>`;
        document.getElementById("total").innerText = 0;
        return;
    }

    let total = 0;

    cart.forEach(item => {

        total += item.price * item.qty;

        table.innerHTML += `
        <tr>
            <td>
                <img src="${item.image}"
                width="50">
                ${item.name}
            </td>

            <td>
                <button onclick="decreaseQty(${item.id})"
                class="btn btn-sm btn-warning">-</button>

                ${item.qty}

                <button onclick="increaseQty(${item.id})"
                class="btn btn-sm btn-success">+</button>
            </td>

            <td>₹${item.price * item.qty}</td>

            <td>
                <button onclick="removeItem(${item.id})"
                class="btn btn-danger btn-sm">X</button>
            </td>
        </tr>
        `;
    });

    document.getElementById("total").innerText = total;
}


/* INIT */
updateCartCount();
displayCart();