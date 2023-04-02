function fetchComments(bookId) {
  const commentSection = document.querySelector("#comment-section");

  fetch(`/api/books/${bookId}/comments/`)
    .then((response) => response.json())
    .then((data) => {
      data.forEach((comment) => {
        const commentCard = `
        <div class="container my-5 py-5 text-dark">
            <div class="row d-flex justify-content-center">
            <div class="col-md-11 col-lg-9 col-xl-7">
              <div class="d-flex flex-start mb-4">
                <img
                  class="rounded-circle shadow-1-strong me-3"
                  src="${comment.user.avatar}"
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
  
                      <div
                        class="d-flex justify-content-between align-items-center"
                      >
                        <div class="d-flex align-items-center">
                          <a href="#!" class="link-muted me-2"
                            ><i class="fas fa-thumbs-up me-1"></i>${
                              comment.likes
                            }</a
                          >
                          <a href="#!" class="link-muted"
                            ><i class="fas fa-thumbs-down me-1"></i>${
                              comment.dislikes
                            }</a
                          >
                        </div>
                        <a href="#!" class="link-muted"
                          ><i class="fas fa-reply me-1"></i> Reply</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            </div>
      </div>
          `;
        commentSection.insertAdjacentHTML("beforeend", commentCard);
      });
    })
    .catch((error) => console.error(error));
}