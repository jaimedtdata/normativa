async function fetch_managed(data) {
	const response = await fetch(managed_search_url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': getCookie('csrftoken'),
		},
		redirect: 'error',
		body: JSON.stringify(data),
	})
	const status = await response.status
	if (status == 200) {
		const data = await response.json()
		return data
	}else {
		console.log(response)
		return "[]"
	}
}

function set_searchs(){
	var sm_buttons = document.getElementsByClassName('search-managed')
	for (var i = sm_buttons.length - 1; i >= 0; i--) {
		sm_buttons[i].onclick = (ev) => {
			let parent = ev.target.parentNode
			if (parent.tagName === "svg") {parent = parent.parentNode}
			if (parent.tagName === "BUTTON") {parent = parent.parentNode}
			parent = parent.parentNode
			let person_type = parent.childNodes[1].childNodes[3]
			let identity = parent.childNodes[3].childNodes[3]
			let names = parent.childNodes[7].childNodes[3]
			let first_surname = parent.childNodes[9].childNodes[3]
			let second_surname = parent.childNodes[11].childNodes[3]
			let mobile = parent.childNodes[13].childNodes[3]
			let email = parent.childNodes[15].childNodes[3]
			let data = {
				'names': names.value,
				'first_surname': first_surname.value,
				'second_surname': second_surname.value,
				'person_type': person_type.value,
				'identity': identity.value,
				'mobile': mobile.value,
				'email': email.value,
			}
			fetch_managed(data).then((response)=>{
				let profile = JSON.parse(response)
				if (profile.length !== 0) {
					names.value = profile.names
					first_surname.value = profile.first_surname
					identity.value = profile.identity
					second_surname.value = profile.second_surname
					mobile.value = profile.mobile
					email.value = profile.email
					person_type.value = profile.person_type
					names.readOnly = true
					identity.readOnly = true
					first_surname.readOnly = true
					second_surname.readOnly = true
					person_type.disabled = true
					mobile.readOnly = true
					email.readOnly = true
					alertify.success('Propietario/Administrado encontrado');
				}else{
					names.readOnly = false
					first_surname.readOnly = false
					second_surname.readOnly = false
					person_type.disabled = false
					mobile.readOnly = false
					email.readOnly = false
					alertify.warning('Propietario/Administrado no encontrado.');
					alertify.warning('Se guardará la información proporcionada.');
				}
			})
		}
	}
	set_cellphone_case()
}
set_searchs()
set_cellphone_case()

function person_type_case(input){
	let parent = input.parentNode.parentNode
	let person_type = parent.childNodes[1]
	let identity = parent.childNodes[3]
	let names = parent.childNodes[7]
	let first_surname = parent.childNodes[9]
	let second_surname = parent.childNodes[11]
	if (!is_post) {
		identity.childNodes[3].value = ''
	}
	if (input.value == 'J') {
		identity.childNodes[3].classList.add('ruc-case')
		identity.childNodes[3].classList.remove('dni-case')
		set_ruc_inputs()
		identity.childNodes[1].innerText = 'RUC'
		names.childNodes[1].innerText = 'Razón Social'
		names.classList.add('col-md-7')
		names.classList.remove('col-md-3')
		first_surname.style.display = 'none'
		second_surname.style.display = 'none'
	}
	else if (input.value == 'N') {
		identity.childNodes[3].classList.add('dni-case')
		identity.childNodes[3].classList.remove('ruc-case')
		set_dni_inputs()

		identity.childNodes[1].innerText = 'DNI'
		names.childNodes[1].innerText = 'Nombres'
		names.classList.add('col-md-3')
		names.classList.remove('col-md-7')
		first_surname.style.display = 'block'
		second_surname.style.display = 'block'
	}
}

function person_type(person_type_input){
	var person_type = document.getElementById(person_type_input)
	person_type.onchange = (ev) => {
		person_type_case(ev.target)
	}
	person_type_case(person_type)
}
