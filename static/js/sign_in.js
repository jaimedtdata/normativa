// Tuition
var profession = document.getElementById('id_profession')

let tuition_input = document.getElementById('id_tuition')
if (tuition_input) {
	tuition_input.oninput = (ev) => {
		if (profession.value == 'A') {
			if(ev.target.value.length > 5){
				ev.target.value = ev.target.value.slice(0,5)
				alertify.warning('No se permiten más números')
			}
		}else if (profession.value == 'I'){
			if(ev.target.value.length > 6){
				ev.target.value = ev.target.value.slice(0,6)
				alertify.warning('No se permiten más números')
			}		
		}
	}
}

if (profession) {
	profession.onchange = () => {
		let value = profession.value
		let tuition_title = document.getElementById('tuition_title')
		tuition_title.innerText = value === 'I' ? 'CIP No.:' : 'CAP No.:'
	}
}

// Firma
let signature_input = document.getElementById('id_signature')
let preview = document.getElementById("peview")
if (preview) {preview.style.display = 'none'}
if (signature_input) {
	signature_input.oninput = (ev) => {
		let file = ev.target.files
		if (file.length > 0) {
		    var fileReader = new FileReader();
		    fileReader.onload = function (event) {
				if (preview) {preview.style.display = 'block'}
		    	preview.setAttribute("src", event.target.result);
		    };
		    fileReader.readAsDataURL(file[0]);
		}
	}
}

// Celular
set_cellphone_case()

// Teléfono
let phone_input = document.getElementById('id_phone')
phone_input.oninput = (ev) => {
	if(phone_input.value.length > 8){
		phone_input.value = phone_input.value.slice(0,8)
		alertify.warning('No se permiten más números')
	}
}

var form = document.querySelector('form')
form.onsubmit = (ev) =>{
	ev.preventDefault()
	let flag = confirm('A continuación procederemos con el registro. ¿Está seguro de continuar con la información proporcionada?') 
	if (flag) {
		form.submit()
	}
	return false
}

// Tipo de Persona
var person_type = document.getElementById('id_person_type')
function set_person_type_rules(){
	if (person_type.value == 'N') {
		names_title.innerText = 'Nombres:'
		identity_title.innerText = 'DNI:'
		address_title.innerText = 'Dirección:'
		first_surname.style.display = 'block'
		second_surname.style.display = 'block'
		names.classList.add('col-md-4')
		names.classList.remove('col-md-8')
		names_input.classList.add('just-letters')
		address.classList.remove('col-md-8')
		identity.classList.add('dni-case')
		identity.classList.remove('ruc-case')
		set_dni_inputs()
	}else if (person_type.value == 'J') {
		names_title.innerText = 'Razón Social:'
		identity_title.innerText = 'RUC:'
		address_title.innerText = 'Direcció Fiscal:'
		first_surname.style.display = 'none'
		second_surname.style.display = 'none'
		names.classList.add('col-md-8')
		names.classList.remove('col-md-4')
		names_input.classList.remove('just-letters')
		address.classList.add('col-md-8')
		identity.classList.remove('dni-case')
		identity.classList.add('ruc-case')
		set_ruc_inputs()
	}
	set_upper_inputs()
}
if (person_type) {
	var names_title = document.getElementById('names-title')
	var identity_title = document.getElementById('identity_title')
	var identity = document.getElementById('id_identity')
	var names = document.getElementById('names_div')
	var names_input = document.getElementById('id_names')
	var first_surname = document.getElementById('first_surname_div')
	var second_surname = document.getElementById('second_surname_div')
	var address = document.getElementById('address_div')
	var address_title = document.getElementById('address_title')
	person_type.onchange = () =>{
		set_person_type_rules()
	}
	set_person_type_rules()
}
