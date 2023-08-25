document.addEventListener("click", function (event) {
  var dropdowns = document.getElementsByClassName("dropdown-content");
  for (var i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (openDropdown.classList.contains("show")) {
      openDropdown.classList.remove("show");
    }
  }
});

// Toggle dropdown on click
var dropdownItems = document.getElementsByClassName("dropdown");
for (var i = 0; i < dropdownItems.length; i++) {
  dropdownItems[i].addEventListener("click", function () {
    var dropdownContent = this.querySelector(".dropdown-content");
    if (dropdownContent) {
      dropdownContent.classList.toggle("show");
    }
  });
}