var changeQ = document.getElementsByClassName("increase");

for (i = 0; i < changeQ.length; i++) {
  changeQ[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);

    if (action == "plus") {
      Increase(productId, action);
    } else if (action == "minus") {
      Decrease(productId, action);
    }
  });
}
function Increase(productId, action) {
  console.log("Increase");
  var quantity = Number(
    document.querySelector(`input[data-product=${productId}]`).value
  );
  quantity = quantity + 1;
  document.querySelector(`input[data-product=${productId}]`).value = quantity;
  console.log(quantity);
}

function Decrease(productId, action) {
  var quantity = Number(
    document.querySelector(`input[data-product=${productId}]`).value
  );
  console.log("Decrease");
  quantity = quantity - 1;
  document.querySelector(`input[data-product=${productId}]`).value = quantity;
}
