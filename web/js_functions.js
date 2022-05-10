async function take_values (){
    let last_name = document.getElementById("last_name").value;
    let first_name = document.getElementById("first_name").value;
    let dad_name = document.getElementById("dad_name").value;
    let dob = document.getElementById("dob").value;
    let doi = document.getElementById("doi").value;
    let checkboxes = document.getElementsByClassName('checkbox');
    let checkboxesChecked = [];
    for (let index = 0; index < checkboxes.length; index++) {
        if (checkboxes[index].checked) {
            checkboxesChecked.push(checkboxes[index].value);
         }
      }
    let gender = checkboxesChecked[0];
    const result = await eel.save_common_info(last_name, first_name, dad_name, gender, dob, doi)();
    document.getElementById("output").value = result;
    }
document.getElementById("submit").onclick = take_values;

