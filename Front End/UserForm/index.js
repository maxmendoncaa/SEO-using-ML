var count = 1; // initialize count variable

function addLink() {
  var container = document.getElementById('competitor-links');
  var div = document.createElement('div');
  div.id = 'competitor-link-' + count; // generate unique ID for the div
  var label = document.createElement('label');
  label.innerHTML = "Enter Competitor's Link " + count + ':';
  var input = document.createElement('input');
  input.type = 'url';
  input.name = 'competitor_link' + count;
  input.placeholder = '';
  var deleteBtn = document.createElement('button');
  deleteBtn.type = 'button';
  deleteBtn.innerHTML = 'Delete link';
  deleteBtn.onclick = function() { removeLink(div.id); }; // pass the div's ID to removeLink
  div.appendChild(document.createElement('br'));
  div.appendChild(label);
  div.appendChild(document.createElement('br'));
  div.appendChild(document.createElement('br'));
  div.appendChild(input);
  div.appendChild(document.createElement('br'));
  div.appendChild(deleteBtn);
  container.appendChild(div);

  count++; // increment the count variable for the next link
}

function removeLink(id) {
  var element = document.getElementById(id);
  element.parentNode.removeChild(element);
}

function clearForm() {
  var form = document.getElementById('user_form');
  form.reset();

  var container = document.getElementById('competitor-links');
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }

  // Make an AJAX call to delete the pagespeed.txt file
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "delete_file.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
    }
  };
  xhttp.send();
}

document.getElementById('clear_form').addEventListener('click', function(e) {
  e.preventDefault();
  clearForm();
});

function saveForm() {
  var formValues = {
    site_link: document.getElementById('site_link').value
  };

  var competitorLinks = document.querySelectorAll('[id^="competitor-link-"]');
  var competitorLinksData = [];
  for (var i = 0; i < competitorLinks.length; i++) {
    var linkId = competitorLinks[i].id;
    var linkValue = competitorLinks[i].querySelector('input').value;
    formValues[linkId] = linkValue;
    competitorLinksData.push({
      id: linkId,
      value: linkValue
    });
  }
  formValues.competitorLinksData = competitorLinksData;
  sessionStorage.setItem('user_form', JSON.stringify(formValues));
}

// Restore the form values from sessionStorage, if available
var savedForm = sessionStorage.getItem('user_form');
if (savedForm) {
  savedForm = JSON.parse(savedForm);

  // Restore the site link value
  document.getElementById('site_link').value = savedForm.site_link;

  // Restore the competitor links
  for (var i = 1; i < count; i++) {
    var linkId = 'competitor-link-' + i;
    var linkInput = document.querySelector('#' + linkId + 'input');
    if (linkInput) {
      var linkValue = savedForm[linkId];
      if (linkValue) {
        linkInput.value = linkValue;
      }
    }
  }
}

window.addEventListener('beforeunload', function(e) {
  saveForm();
});

function loadForm() {
  var savedFormValues = sessionStorage.getItem('user_form');
  if (savedFormValues) {
    savedFormValues = JSON.parse(savedFormValues);
    document.getElementById('site_link').value = savedFormValues.site_link;
    var competitorLinksData = savedFormValues.competitorLinksData;
    for (var i = 0; i < competitorLinksData.length; i++) {
      var linkId = competitorLinksData[i].id;
      var linkValue = competitorLinksData[i].value;
      var div = document.createElement('div');
      var label = document.createElement('label');
      label.innerHTML = "Enter Competitor's Link " + (i+1) + ':';
      var input = document.createElement('input');
      input.type = 'url';
      input.name = 'competitor_link' + (i+1);
      input.value = linkValue;
      var deleteBtn = document.createElement('button');
      deleteBtn.type = 'button';
      deleteBtn.innerHTML = 'Delete link';
      deleteBtn.onclick = (function(id) {
        return function() { removeLink(id); };
      })(linkId);
      div.appendChild(document.createElement('br'));
      div.appendChild(label);
      div.appendChild(document.createElement('br'));
      div.appendChild(document.createElement('br'));
      div.appendChild(input);
      div.appendChild(document.createElement('br'));
      div.appendChild(deleteBtn);
      div.id = linkId;
      document.getElementById('competitor-links').appendChild(div);
    }    
  }
}
window.addEventListener('load', function() {
  loadForm();
});

document.getElementById('edit_links').addEventListener('click', function(e) {
  e.preventDefault();
  loadForm();
});
