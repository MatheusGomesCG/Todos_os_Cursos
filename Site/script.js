// Função para rolar para o topo da página
function scrollToTop() {
    // Rola suavemente até o topo da página
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Mostra o botão de rolagem para o topo quando o usuário rolar a página para baixo
window.onscroll = function () {
    var button = document.getElementById("scrollToTopButton");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}
