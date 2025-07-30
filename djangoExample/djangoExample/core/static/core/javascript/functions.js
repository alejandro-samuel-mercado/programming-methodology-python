(function (d, s, id) {
  var js;
  if (d.getElementById(id)) {
    return;
  }
  js = d.createElement(s);
  js.id = id;
  js.src = "https://embedsocial.com/embedscript/ri.js";
  d.getElementsByTagName("head")[0].appendChild(js);
})(document, "script", "EmbedSocialReviewsScript");

var swiper = new Swiper(".swiper-container", {
  slidesPerView: 1,
  speed: 1500,
  loop: true,
  effect: "fade",
  autoplay: {
    delay: 5000,
  },
});

window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const scrollContainer = document.querySelector(".scroll-container");
  const scrollHeight = scrollContainer.scrollHeight;
  let currentScroll = 0;
  const scrollStep = 1; // Cantidad de píxeles para desplazarse
  const scrollDelay = 50; // Tiempo en milisegundos entre desplazamientos

  function autoScroll() {
    currentScroll += scrollStep;
    if (currentScroll >= scrollHeight - scrollContainer.clientHeight) {
      currentScroll = 0; // Reiniciar cuando llegue al final
    }
    scrollContainer.scrollTop = currentScroll;
  }

  setInterval(autoScroll, scrollDelay);
});

document.addEventListener("DOMContentLoaded", () => {
  const titles = document.querySelectorAll(".title");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("show"); // Añade la clase 'show' cuando es visible
          entry.target.classList.add("animate__fadeInLeft"); // Añade la animación de Animate.css
          observer.unobserve(entry.target); // Deja de observar si quieres que se active solo una vez
        }
      });
    },
    {
      threshold: 0.1, // Se activa cuando el 10% del elemento está visible
    }
  );

  titles.forEach((title) => {
    observer.observe(title); // Observa cada título
  });
});

document.querySelectorAll(".add-to-cart").forEach((button) => {
  button.addEventListener("click", () => {
    button.textContent = "Añadido";
    button.style.backgroundColor = "#28a745";
    setTimeout(() => {
      button.textContent = "Agregar al Carrito";
      button.style.backgroundColor = "#007bff";
    }, 2000);
  });
});

$(document).ready(function () {
  $("#productsCarousel").carousel({
    interval: 5000, // Cambia automáticamente cada 5 segundos
    wrap: true, // Vuelve al inicio después de la última diapositiva
  });
});
