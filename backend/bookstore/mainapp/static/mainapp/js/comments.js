function createCommentCard(comment) {
  return `
    <div class="d-flex flex-start mb-4 p-3">
      <img
        class="rounded-circle shadow-1-strong me-3"
        src="http://127.0.0.1:8000/static/mainapp/images/Default-PFP.jpg"
        alt="avatar"
        width="65"
        height="65"
      />
      <div class="card w-100">
        <div class="card-body p-4">
          <div class="">
            <h5>${comment.user.username}</h5>
            <p class="small">${new Date(
              comment.created_at
            ).toLocaleString()}</p>
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
      const commentCard = createCommentCard(data);
      commentSection.insertAdjacentHTML("beforeend", commentCard);
    })
    .catch((error) => console.error(error));
}
