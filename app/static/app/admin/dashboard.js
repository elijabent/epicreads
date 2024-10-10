var books = [];

function addBook(title, cover_front, summary, id) {
    let book = {title: title, cover_front: cover_front, summary:summary, id: id};
    books.push(book);
}

function refreshBooks(){
    for (let i = 0; i < books.length; i++) {
        let book = books[i];
        let newBook = `
            <div class="col s4 book">
                <div class="card">
                    <div class="card-image">
                        <img src="/media/${book.cover_front}">
                        <span class="card-title">${book.title}</span>
                    </div>
                    <div class="card-content">
                        <p>${book.summary}</p>
                    </div>
                    <div class="card-action right-align">
                        <a href="/admin_dashboard/edit_book/${book.id}"><i class="material-icons black-text">edit</i></a>
                        <a href="/admin_dashboard/stats/${book.id}"><i class="material-icons black-text">info</i></a>
                        <a href="/admin_dashboard/delete_book/${book.id}"><i class="material-icons red-text text-darken-2">delete</i></a>
                    </div>
                </div>
            </div>
        `;

        //selects last row in grid
        let lastRow = document.querySelectorAll('.row')[document.querySelectorAll('.row').length - 1];
        //checks how many children are in row
        if (lastRow.children.length < 3) {
            lastRow.innerHTML += newBook;
        }
        else{
            let newRow = document.createElement('div');
            newRow.setAttribute('class', 'row');
            document.querySelector('.container').appendChild(newRow);
            newRow.innerHTML += newBook;
        }
    }
}

document.addEventListener('DOMContentLoaded', function(){
    refreshBooks();
});