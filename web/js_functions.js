async function take_values (){
    document.getElementById("output").value = [];
    let last_name = document.getElementById("last_name").value;
    let first_name = document.getElementById("first_name").value;
    let dad_name = document.getElementById("dad_name").value;
    let dob = document.getElementById("dob").value;
    let doi = document.getElementById("doi").value;

    let checkboxes = document.getElementsByName('pos');
    let gender;
    for (let index = 0; index < checkboxes.length; index++) {
        if (checkboxes[index].checked) {
            gender = checkboxes[index].value;
         }
      }

    let body_length = document.getElementById("body_length").value;
    let body_weight = document.getElementById("body_weight").value;
    let ind_ketle = body_weight/((body_length/100)**2)

    let lungs_capacity = document.getElementById("lungs_capacity").value;
    let d_r_wrist = document.getElementById("d_r_wrist").value;
    let d_l_wrist = document.getElementById("d_l_wrist").value;
    let systolic_pressure = document.getElementById("systolic_pressure").value;
    let diastolic_pressure =  document.getElementById("diastolic_pressure").value;
    let heart_rate = document.getElementById("heart_rate").value;

    let teeth = document.getElementById("teeth").value;

    let biological_params = get_biological_params(gender);

    const result = await eel.calculate_centiles(last_name, first_name, dad_name, gender, dob, doi, body_length,
    body_weight, ind_ketle, lungs_capacity, d_r_wrist, d_l_wrist, systolic_pressure, diastolic_pressure, heart_rate,
    teeth, biological_params)();

    document.getElementById("output").innerHTML = result;
    }
document.getElementById("submit").onclick = take_values;



function get_biological_params(gender){
    let biological_params;
    if (gender == 'F'){
        var ma_radio = document.getElementsByName('GMa');
        var p_radio = document.getElementsByName('GP');
        var ax_radio = document.getElementsByName('GAx');
        var me_radio = document.getElementsByName('GMe');
        var ma;
        var p;
        var ax;
        var me;
        for (var i = 0; i < ma_radio.length; i++) {
            if (ma_radio[i].type === 'radio' && ma_radio[i].checked) {
                ma = ma_radio[i].value;
                }
            if (p_radio[i].type === 'radio' && p_radio[i].checked) {
                p = p_radio[i].value;
                }
            if (ax_radio[i].type === 'radio' && ax_radio[i].checked) {
                ax = ax_radio[i].value;
                }
            if (me_radio[i].type === 'radio' && me_radio[i].checked) {
                me = me_radio[i].value;
                }
                }
            biological_params = [ma, p, ax, me];
            }

    if (gender == 'M'){
        var bax_radio = document.getElementsByName('BAx');
        var ax;
        for (var i = 0; i < bax_radio.length; i++) {
            if (bax_radio[i].type === 'radio' && bax_radio[i].checked) {
                ax = bax_radio[i].value;
                }
            }

        var l_radio = document.getElementsByName('BL');
        var v_radio = document.getElementsByName('BV');
        var l;
        var v;
        for (var i = 0; i < l_radio.length; i++) {
            if (l_radio[i].type === 'radio' && l_radio[i].checked) {
                l = l_radio[i].value;
                }
            if (v_radio[i].type === 'radio' && v_radio[i].checked) {
                v = v_radio[i].value;
               }
            }

        var p_radio = document.getElementsByName('BP');
        var f_radio = document.getElementsByName('BF');
        var p;
        var f;
        for (var i = 0; i < p_radio.length; i++) {
            if (p_radio[i].type === 'radio' && p_radio[i].checked) {
                p = p_radio[i].value;
                }
            if (f_radio[i].type === 'radio' && f_radio[i].checked) {
                f = f_radio[i].value;
            }
            }
            biological_params = [ax, v, l, p, f];
            }
    return biological_params;




}
