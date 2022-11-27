function checkboxes() {
    var box = document.getElementById("box");
     
    // creating checkbox element
    var checkbox = document.createElement('input');
     
    // Assigning the attributes
    // to created checkbox
    checkbox.type = "checkbox";
    checkbox.name = "name";
    checkbox.value = "value";
    checkbox.id = "id";
     
    // appending the checkbox to div
    box.appendChild(checkbox);
}