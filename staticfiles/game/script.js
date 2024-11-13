document.addEventListener("DOMContentLoaded", () => {
    const cells = document.querySelectorAll(".cell");
    const boardElement = document.getElementById("board");
    const restartButton = document.getElementById("restart");

    let board = ["", "", "", "", "", "", "", "", ""];
    let gameActive = true;

    // Result modal elements
    const resultModal = document.createElement("div");
    resultModal.id = "resultModal";
    resultModal.innerHTML = `
        <div id="resultText"></div>
        <button id="closeModal">Close</button>
    `;
    document.body.appendChild(resultModal);
    const resultText = document.getElementById("resultText");
    const closeModalButton = document.getElementById("closeModal");

    cells.forEach(cell => {
        cell.addEventListener("click", () => {
            const index = cell.getAttribute("data-index");
            if (board[index] === "" && gameActive) {
                board[index] = "X";
                cell.classList.add("clicked");
                cell.innerText = "X";
                updateGame();
            }
        });
    });

    restartButton.addEventListener("click", () => {
        board = ["", "", "", "", "", "", "", "", ""];
        gameActive = true;
        cells.forEach(cell => {
            cell.classList.remove("clicked", "win");
            cell.innerText = "";
        });
        resultModal.classList.remove("show");
    });

    closeModalButton.addEventListener("click", () => {
        resultModal.classList.remove("show");
    });

    function updateGame() {
        fetch(`/play_move/?board=${board.join(",")}`)
            .then(response => response.json())
            .then(data => {
                board = data.board;
                if (data.status === "finished") {
                    gameActive = false;
                    displayResult(data.winner);
                } else {
                    updateBoard();
                }
            });
    }

    function updateBoard() {
        board.forEach((mark, i) => {
            if (mark && !cells[i].classList.contains("clicked")) {
                cells[i].innerText = mark;
                cells[i].classList.add("clicked");
            }
        });
    }

    function displayResult(winner) {
        if (winner === "Tie") {
            resultText.innerText = "It's a Tie!";
        } else if (winner === "X") {
            resultText.innerText = "You Win!";
        } else {
            resultText.innerText = "You Lose!";
        }
        resultModal.classList.add("show");
    }
});
