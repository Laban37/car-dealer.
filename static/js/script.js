// Simple console log and welcome alert
console.log("JavaScript is working!");
alert("Welcome to the Car Dealership site!");

// Example: Highlight car cards on hover
document.addEventListener("DOMContentLoaded", function() {
    const carCards = document.querySelectorAll(".car-card");

    carCards.forEach(card => {
        card.addEventListener("mouseover", function() {
            card.style.transform = "scale(1.05)";
            card.style.transition = "transform 0.3s";
            card.style.boxShadow = "0px 5px 15px rgba(0,0,0,0.3)";
        });

        card.addEventListener("mouseout", function() {
            card.style.transform = "scale(1)";
            card.style.boxShadow = "0px 2px 5px rgba(0,0,0,0.1)";
        });
    });
});

// Example: Simple alert when a "View Car" button is clicked
const carButtons = document.querySelectorAll(".view-car-btn");
carButtons.forEach(button => {
    button.addEventListener("click", function() {
        alert("Redirecting to car details page...");
    });
});
