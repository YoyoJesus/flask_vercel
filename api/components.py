def render_navbar():
    return '''
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">
                <img src="/static/myAvatar.jpg" alt="Austin Sternberg" style="width: 50px; border-radius: 50%;">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>
                    <li class="nav-item"><a class="nav-link" href="https://blog.yoyojesus.xyz" target="_blank" rel="noopener">Blog</a></li>
                    <li class="nav-item"><a class="nav-link" href="/resume">Resume</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"></script>
    '''

def render_footer():
    return '''
    <footer class="footer-custom text-center py-3 bg-dark text-white mt-5">
        <div>
            <p class="mb-0">2025 Austin Sternberg - Somehow running Flask on Vercel</p>
        </div>
    </footer>
    '''
