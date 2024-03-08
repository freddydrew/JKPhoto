function setActiveSort(val){
    var sortbtns = document.getElementsByClassName("sort-btn");

    for (var i = 0; i < sortbtns.length; i++) {
        sortbtns[i].classList.remove('active')
      }

    let activeSortBtn = document.getElementById(val);
    activeSortBtn.classList.add('active')
}