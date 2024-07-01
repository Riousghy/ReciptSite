document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is loaded and running!");

    // Toggle recipe details
    const recipeLinks = document.querySelectorAll('ul li a[data-recipe-id]');
    recipeLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const recipeId = this.getAttribute('data-recipe-id');
            if (!recipeId) {
                console.error('Recipe ID is null or undefined');
                return;
            }
            fetch(`/recipe/${recipeId}/`)
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const recipeDetail = doc.querySelector('.recipe-detail');
                    const detailContainer = document.querySelector('.recipe-detail-container');
                    detailContainer.innerHTML = '';
                    if (recipeDetail) {
                        detailContainer.appendChild(recipeDetail);
                    } else {
                        console.error('Recipe detail element not found');
                    }
                })
                .catch(error => console.error('Error fetching recipe details:', error));
        });
    });

    // Show a confirmation dialog when creating a new recipe
    const createRecipeForm = document.querySelector('form');
    if (createRecipeForm) {
        createRecipeForm.addEventListener('submit', function(event) {
            const confirmed = confirm('Are you sure you want to create this recipe?');
            if (!confirmed) {
                event.preventDefault();
            }
        });
    }

    // Smooth scroll to the recipe list
    const scrollToRecipesBtn = document.querySelector('.scroll-to-recipes');
    if (scrollToRecipesBtn) {
        scrollToRecipesBtn.addEventListener('click', function() {
            document.querySelector('ul').scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Highlight the navbar link based on the current page
    const navLinks = document.querySelectorAll('.nav-link');
    const currentUrl = window.location.href;
    navLinks.forEach(link => {
        if (link.href === currentUrl) {
            link.classList.add('active');
        }
    });

    // 显示和隐藏模态框
    const modal = document.querySelector('.modal');
    if (modal) {
        const closeModal = modal.querySelector('.close');
        if (closeModal) {
            closeModal.addEventListener('click', function() {
                modal.style.display = 'none';
            });
        }
    }
});
