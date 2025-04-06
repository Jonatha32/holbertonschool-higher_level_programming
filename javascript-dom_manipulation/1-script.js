document.addEventListener('DOMContentLoaded', function() {
  
  const redHeaderElement = document.getElementById('red_header');
    redHeaderElement.addEventListener('click', function() {
      const headerElement = document.querySelector('header');
      headerElement.style.color = '#FF0000';
    });
});
