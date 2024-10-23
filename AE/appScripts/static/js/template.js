
function loadTemplate(templatePath, targetElementId) {
  //const templatePath = "{{ url_for('static', filename='template.html') }}";

  fetch(templatePath)
    .then(response => response.text())
    .then(data => {
      // Insert the template into the current document
      document.body.insertAdjacentHTML('beforeend', data);

      // var imageUrl = document.getElementById("AEtemp").getAttribute("data-image-url");
      // var imgElement = document.createElement("img");
      // imgElement.src = imageUrl;
      // imgElement.alt = "Image from Flask";
  
      // document.getElementById("logo").appendChild(imgElement);

      // Now you can use the template as usual
      const template = document.getElementById('my-template');
      const clone = document.importNode(template.content, true);
      document.getElementById('AEtemp').appendChild(clone);
    });
}

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

// // Display loading screen as soon as button is clicked and then show image once url ready
// document.getElementById('generateButton').addEventListener('click', async function() {
//   const prompt = document.getElementById('prompt').value;
//   print("button pressed")

//   if (!prompt) {
//       alert('Please enter a prompt');
//       return;
//   }

//   // Show loading screen
//   document.getElementById('loadingContainer').style.display = 'block';
//   // document.getElementById('resultContainer').style.display = 'none';

//   // try {
//   //     // const response = await fetch('/generate');
//   //     // const data = await response.json();
//   //     var imageUrl =  image_url;   

//   //     if (imageUrl) {
//   //         // Hide loading screen and show the result
//   //         document.getElementById('loadingContainer').style.display = 'none';
//   //         document.getElementById('resultContainer').style.display = 'block';
//   //         // document.getElementById('resultImage').src = data.imageUrl;
//   //     } else {
//   //         alert('Failed to generate image');
//   //     }
//   // } catch (error) {
//   //     alert('Error: ' + error.message);
//   // }
// });
document.addEventListener('DOMContentLoaded', function () {
  loadTemplate('/static/template.html', 'AEtemp');
});

