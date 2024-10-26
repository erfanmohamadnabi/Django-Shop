var swiper = new Swiper(".main-slider", {
  pagination: {
    el: ".swiper-pagination",
    dynamicBullets: true,
  },
  autoplay: {
    delay: 5000,
  },
});

var swiper = new Swiper(".cat-slider", {
  slidesPerView: 2,
  spaceBetween: 20,
  autoplay: {
    delay: 5000,
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1024: {
      slidesPerView: 6,
      spaceBetween: 15,
    },
  },
});

var swiper = new Swiper(".off-product", {
  slidesPerView: 1,
  spaceBetween: 20,
  autoplay: {
    delay: 5000,
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
  },
});

var swiper = new Swiper(".slider-product1", {
  slidesPerView: 1,
  spaceBetween: 20,
  autoplay: {
    delay: 5000,
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 15,
    },
  },
});

var swiper = new Swiper(".slider-product2", {
  slidesPerView: 1,
  spaceBetween: 10,
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
  },
});

var swiper = new Swiper(".partners", {
  slidesPerView: 2,
  spaceBetween: 10,
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 40,
    },
    1024: {
      slidesPerView: 5,
      spaceBetween: 50,
    },
  },
});

var swiper = new Swiper(".gall-pro", {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".pro-main", {
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  thumbs: {
    swiper: swiper,
  },
});

function decrement(e) {
  const btn = e.target.parentNode.parentElement.querySelector(
    'button[data-action="decrement"]'
  );
  const target = btn.nextElementSibling;
  let value = Number(target.value);
  value--;
  target.value = value;
}

var swiper = new Swiper(".related", {
  slidesPerView: 1,
  spaceBetween: 10,
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 15,
    },
  },
});

var swiper = new Swiper(".about-slider", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  loop: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 1,
    slideShadows: true,
  },
  pagination: {
    el: ".swiper-pagination",
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
  },
});

function showTab(tabId) {
  // Hide all tab content
  const tabContents = document.querySelectorAll(".tab-content");
  tabContents.forEach((content) => {
    content.classList.add("hidden");
  });

  // Show the selected tab content
  const selectedTab = document.getElementById(tabId);
  if (selectedTab) {
    selectedTab.classList.remove("hidden");
  }

  // Remove the 'active' class from all tab buttons
  const tabButtons = document.querySelectorAll(".tab-button");
  tabButtons.forEach((button) => {
    button.classList.remove("active");
  });

  // Add the 'active' class to the clicked tab button
  const clickedButton = document.querySelector(
    `[onclick="showTab('${tabId}')"]`
  );
  if (clickedButton) {
    clickedButton.classList.add("active");
  }
}

// Initialize the first tab
showTab("tab1");

    // خواندن مقادیر زمان از localStorage
    let seconds = localStorage.getItem('seconds') ? parseInt(localStorage.getItem('seconds')) : 60;
    let minutes = localStorage.getItem('minutes') ? parseInt(localStorage.getItem('minutes')) : 10;
    let hours = localStorage.getItem('hours') ? parseInt(localStorage.getItem('hours')) : 24;
    let days = localStorage.getItem('days') ? parseInt(localStorage.getItem('days')) : 4;
    setInterval(() => {
        if (seconds > 0) {
            seconds--;
        } else {
            if (minutes > 0) {
                minutes--;
                seconds = 59;
            } else {
                if (hours > 0) {
                    hours--;
                    minutes = 59;
                    seconds = 59;
                } else {
                    if (days > 0) {
                        days--;
                        hours = 23;
                        minutes = 59;
                        seconds = 59;
                    }
                }
            }
        }
        // ذخیره مقادیر در localStorage
        localStorage.setItem('seconds', seconds);
        localStorage.setItem('minutes', minutes);
        localStorage.setItem('hours', hours);
        localStorage.setItem('days', days);
        // به روز رسانی نمایش تایمر
        document.getElementById("secondElement").style.setProperty("--value", seconds);
        document.getElementById("minuteElement").style.setProperty("--value", minutes);
        document.getElementById("hourElement").style.setProperty("--value", hours);
        document.getElementById("dayElement").style.setProperty("--value", days);
    }, 1000);