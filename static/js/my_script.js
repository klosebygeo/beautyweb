/*================== toogle icon navbar =================*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
  menuIcon.classList.toggle('bx-x');
  navbar.classList.toggle('active');
};

const product = [
  {
    id: 0,
    image: '../static/img/accesorii1.png',
    title: 'Barba',
    price: 120,
  },
  {
    id: 1,
    image: '../static/img/sampon6.jpg',
    title: 'Sampon pentru ingrijirea parului',
    price: 110,
  },
  {
    id: 2,
    image: '../static/img/accesorii6.png',
    title: 'Accesorii',
    price: 60,
  },
  {
    id: 3,
    image: '..static/img/accesorii4.png',
    title: 'Accesorii',
    price: 65,
  }
];

const addtocart = (id) => {
  // Implementați funcționalitatea adăugării produsului în coșul de cumpărături aici
  console.log(`Produsul cu id-ul ${id} a fost adăugat în coșul de cumpărături.`);
}

const categories = [...new Set(product.map((item) =>
{return item}))];
let i = 0;
document.getElementById("root").innerHTML = categories.map((item) => {
  var { image, title, price } = item;
  return (
    `<div class='box'>
      <div class='img-box'>
        <img class='images' src=${image}></img>
      </div>
      <div class='bottom'>
        <p>${title}</p>
        <h2>$ ${price}.00</h2>`+
        "<button onclick='addtoCart("+(i++)+")'>Add to cart</button>"+
      `</div>
    </div>`
  );
}).join('');

var cart =[];

function  addcart(a){
    cart.push({...categories[a]});
    displaycart();
}


function  displaycart(a){
    let j = 0;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            return(
                `<div class='cart-item'>
                    <div class='row-img'>
                        <img class='rowing' src=${image}>
                    </div>
                    <p style='font-size:12px;'>${title}</p>
                    <h2 style='font-size:15px;'>$ ${price}.00</h2>`+
                    "<i class='fa-solid fa-trash' onclick='delElement("+(j++)+")'></i></div>"
            );
        }).join('');
    }
}
