function createCommentCard(comment) {
  return `
    <div class="d-flex flex-start mb-4 p-3">
      
      
      <div class="card w-100">
        <div class="card-body p-4">
          <div class="">
            <h5><i class="fa-solid fa-user"></i> ${comment.user.username}</h5>
            <div class="ml-auto">
              <p class="small">${new Date(
                comment.created_at
              ).toLocaleString()}</p>
            </div>
            <div>
              <p class="text-left"><span class="text-muted">${
                comment.rating
              }.0</span> <span class="fa rstar fa-star star-inactive ml-3"></span> <span class="fa rstar fa-star star-inactive"></span> <span class="fa fa-star rstar star-inactive"></span> <span class="fa fa-star rstar star-inactive"></span> <span class="fa fa-star rstar star-inactive"></span></p>
            </div>
            
            <p>${comment.content}</p>

            <div class="d-flex justify-content-between align-items-center">
              <div class="d-flex align-items-center">
                <a href="#!" class="link-muted me-2"><i class="fas fa-thumbs-up me-1"></i>${
                  comment.likes
                }</a>
                <a href="#!" class="link-muted"><i class="fas fa-thumbs-down me-1"></i>${
                  comment.dislikes
                }</a>
              </div>
              <a href="#!" class="link-muted"><i class="fas fa-reply me-1"></i> Reply</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}

function setStars(comment) {
  console.log("hello")
  console.log(document.querySelectorAll(".rstar"))
  document.querySelectorAll(".rstar").forEach((Element, index) => {
    if (index < comment.rating) {
      Element.classList.remove("star-inactive");
      Element.classList.add("star-active");
    }
  });
}

function fetchComments(bookId) {
  const commentSection = document.querySelector("#comment-section");
  const commentForm = document.querySelector("#add-comment-form");
  const ratingStars = document.querySelectorAll(
    ".star-container input[type='radio']"
  );

  commentForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const content = document.querySelector("#comment-content").value;
    const rating = document.querySelector(
      ".star-container input[type='radio']:checked"
    ).value;
    console.log(`Content: ${content}, Rating: ${rating}`);
    createComment(bookId, content, rating);
    console.log("Comment created!");
    commentForm.reset();
  });

  ratingStars.forEach((star) => {
    star.addEventListener("change", () => {
      console.log("Star rating changed!");
      const ratingValue = star.value;
      console.log(`User selected ${ratingValue} stars`);
    });
  });
  fetch(`/api/books/${bookId}/comments/`)
    .then((response) => response.json())
    .then((data) => {
      data.forEach((comment) => {
        const commentCard = createCommentCard(comment);
        commentSection.insertAdjacentHTML("beforeend", commentCard);
        
        setStars(comment);
      });
    })
    .catch((error) => console.error(error));
}

function createComment(bookId, content, rating) {
  fetch(`/api/books/${bookId}/comments/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ book: bookId, content, rating }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const commentSection = document.querySelector("#comment-section");
      // added recent
      const existingComment = getExistingComment(bookId);

      // If a comment already exists, update the existing comment
      if (existingComment) {
        updateComment(bookId, existingComment.id, content, rating);
        return;
      }
      // added recent

      const commentCard = createCommentCard(data);
      commentSection.insertAdjacentHTML("beforeend", commentCard);

      // added recent

      // Save the comment to localStorage
      saveComment(bookId, data.id, content, rating);

      // added recent
    })

    .catch((error) => console.error(error));
}

function getExistingComment(bookId) {
  const comments = JSON.parse(localStorage.getItem("comments")) || {};
  return comments[bookId] || null;
}

function updateComment(bookId, commentId, content, rating) {
  fetch(`/api/books/${bookId}/comments/${commentId}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ content, rating }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Update the existing comment in the DOM
      const commentCard = document.querySelector(`#comment-${data.id}`);
      commentCard.querySelector(".comment-content").textContent = data.content;
      commentCard.querySelector(
        ".comment-rating"
      ).textContent = `(${data.rating} stars)`;

      // Update the comment in localStorage
      saveComment(bookId, commentId, content, rating);
    })
    .catch((error) => console.error(error));
}

function saveComment(bookId, commentId, content, rating) {
  const comments = JSON.parse(localStorage.getItem("comments")) || {};
  comments[bookId] = { id: commentId, content, rating };
  localStorage.setItem("comments", JSON.stringify(comments));
}
