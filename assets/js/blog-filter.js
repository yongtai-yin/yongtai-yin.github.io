document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-tag');
    const posts = document.querySelectorAll('.post-item');

    filterButtons.forEach((button) => {
        button.addEventListener('click', () => {
            filterButtons.forEach((btn) => btn.classList.remove('active'));
            button.classList.add('active');

            const selectedTag = button.getAttribute('data-tag');

            posts.forEach((post) => {
                const postTags = post.getAttribute('data-tags').split(',');
                if (selectedTag === 'all' || postTags.includes(selectedTag)) {
                    post.classList.remove('hidden');
                } else {
                    post.classList.add('hidden');
                }
            });
        });
    });
});
