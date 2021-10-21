// MY (SUCCESSFUL) TRY

// let counter = document.getElementById("value");
// const decrease = document.querySelector(".decrease");
// const reset = document.querySelector(".reset");
// const increase = document.querySelector(".increase");

// decrease.addEventListener("click", () => {
//     counter.textContent -= 1;
//     if (counter.textContent < 0) {
//         counter.style.color = "hsl(360, 67%, 44%)"
//     }
// });

// reset.addEventListener("click", () => {
//     counter.textContent = 0;
//     counter.style.color = "black";
// });

// increase.addEventListener("click", () => {
//     counter.textContent = (parseInt(counter.textContent) + 1);
//     if (counter.textContent > 0) {
//         counter.style.color = "hsl(125, 67%, 44%)"
//     }
// });

// ----------------------------------------------------------------------------------------

// PROFESSOR CODE

// set initial count
let count = 0;

// select value and buttons
const value = document.querySelector("#value");
const btns = document.querySelectorAll(".btn");

// Iterate through all the buttons
btns.forEach(btn => {
    // Add event listener to every button and detect which button im clicking. Then increase, decrease or reset and change color
    btn.addEventListener("click", (e) => {
        const styles = e.currentTarget.classList;
        if (styles.contains("decrease")) {
            count--;
        }
        else if (styles.contains("increase")){
            count++;
        }
        else {
            count = 0;
        }
        // Color conditions by me :)
        count < 0 ? value.style.color = "red"
            : count === 0 ? value.style.color = "black" 
            : value.style.color = "green";
        value.textContent = count;
    });
});