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

    let body_length = document.getElementById("body_length").value;
    let body_weight = document.getElementById("body_weight").value;
    let ind_ketle = body_weight/((body_length/100)**2)

    let c_chest = document.getElementById("с_chest").value;
    let c_waist = document.getElementById("с_waist").value;
    let c_r_shoulders = document.getElementById("с_r_shoulders").value;
    let c_l_shoulders = document.getElementById("с_l_shoulders").value;
    let c_hips = document.getElementById("с_hips").value;
    let c_neck = document.getElementById("с_neck").value;
    let c_wrist = document.getElementById("с_wrist").value;

    let t_stomach = document.getElementById("t_stomach").value;
    let t_shoulder = document.getElementById("t_shoulder").value;
    let t_back = document.getElementById("t_back").value;

    let lungs_capacity = document.getElementById("lungs_capacity").value;
    let d_r_wrist = document.getElementById("d_r_wrist").value;
    let d_l_wrist = document.getElementById("d_l_wrist").value;
    let systolic_pressure = document.getElementById("systolic_pressure").value;
    let diastolic_pressure =  document.getElementById("diastolic_pressure").value;
    let heart_rate = document.getElementById("heart_rate").value;

    const result = await eel.calculate_centiles(last_name, first_name, dad_name, gender, dob, doi, body_length,
    body_weight, ind_ketle, c_chest, c_waist, c_r_shoulders, c_l_shoulders, c_hips, c_neck, c_wrist, lungs_capacity,
    d_r_wrist, d_l_wrist, systolic_pressure, diastolic_pressure, heart_rate, t_stomach, t_shoulder, t_back)();

    document.getElementById("output").innerHTML = result;
    }
document.getElementById("submit").onclick = take_values;

