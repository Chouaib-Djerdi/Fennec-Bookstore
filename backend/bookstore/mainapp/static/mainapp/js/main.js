// const bookListDiv = document.getElementById("book-list");

// function fetchBooks() {
//   fetch("http://127.0.0.1:8000/api/books/")
//     .then((response) => response.json())
//     .then((data) => {
//       let books = "";
//       data.forEach((book) => {
//         books += `<div>
//           <h2>${book.title}</h2>
//           <p>Author: ${book.author}</p>
//           <p>Price: ${book.price}</p>
//         </div>`;
//       });
//       bookListDiv.innerHTML = books;
//     });
// }

// fetchBooks();

fetch("http://127.0.0.1:8000/api/books/")
  .then((response) => response.json())
  .then((data) => {
    const bookList = document.getElementById("book-list");
    if (bookList) {
      data.forEach((book) => {
        const listItem = document.createElement("li");
        listItem.textContent = book.title;
        bookList.appendChild(listItem);
      });
    }
  })
  .catch((error) => console.error(error));
