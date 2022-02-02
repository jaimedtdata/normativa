
async function fetch_user(data) {
	const response = await fetch(user_search_url,{
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': getCookie('csrftoken'),
		},
		body: JSON.stringify(data),
		redirect: 'error',
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

function set_profeessions_onchange(){
	var profession_inputs = document.getElementsByClassName('profession_change')
	for (let i = profession_inputs.length - 1; i >= 0; i--) {
		profession_inputs[i].onchange = () => {
			set_profeession_title(profession_inputs[i])
		}
	}
}
function set_profeession_title(el){
	let value = el.value
	let parent = el.parentNode.parentNode
	let tuition_title = parent.getElementsByClassName('tuition-title')[0]
	let tuition_input = parent.getElementsByClassName('tuition-case')[0]
	if (value === 'I') {
		tuition_title.innerText = 'CIP N°'
		tuition_input.classList.remove('cap-case')
		tuition_input.classList.add('cip-case')
		tuition_input.value = ''
		set_cip_inputs()
	}else{
		tuition_input.classList.add('cap-case')
		tuition_input.classList.remove('cip-case')
		tuition_title.innerText = 'CAP N°'
		set_cap_inputs()
	}

}

function search_profile_app(){
	var sp_buttons = document.getElementsByClassName('search-profile')
	for (var i = sp_buttons.length - 1; i >= 0; i--) {
		sp_buttons[i].onclick = (ev) => {
			let parent = ev.target.parentNode
			if (parent.tagName === "svg") {parent = parent.parentNode}
			if (parent.tagName === "BUTTON") {parent = parent.parentNode}
			parent = parent.parentNode
			let tuition = parent.childNodes[1].childNodes[3]
			let names = parent.childNodes[5].childNodes[3]
			let first_surname = parent.childNodes[7].childNodes[3]
			let second_surname = parent.childNodes[9].childNodes[3]
			let profession = parent.childNodes[11].childNodes[3]
			let mobile = parent.childNodes[13].childNodes[3]
			let email = parent.childNodes[15].childNodes[3]
			let is_signature_validated = parent.childNodes[17].childNodes[4]
			let data = {
				'tuition': tuition.value,
				'profession': profession.value,
			}
			if (tuition.value != '') {
				fetch_user(data).then((response)=>{
					let user = JSON.parse(response)
					if (user.length !== 0) {
						names.value = user.names
						names.readOnly = true
						first_surname.value = user.first_surname
						first_surname.readOnly = true
						second_surname.value = user.second_surname
						second_surname.readOnly = true
						profession.value = user.profession
						profession.disabled = true
						if (user.is_signature_validated) {
							is_signature_validated.innerText = 'Validada'
							is_signature_validated.classList.add('text-success')
							is_signature_validated.classList.remove('text-danger')
						}else{
							is_signature_validated.innerText = 'Sin Validar'
							is_signature_validated.classList.add('text-danger')
							is_signature_validated.classList.remove('text-success')
						}
						mobile.value = user.mobile
						mobile.readOnly = true
						email.value = user.email
						email.readOnly = true
    					alertify.success('Profesional encontrado');
    					tuition.readOnly = true
					}else{
						names.value = ''
						names.readOnly = false
						first_surname.value = ''
						first_surname.readOnly = false
						second_surname.value = ''
						second_surname.readOnly = false
						profession.disabled = false
						is_signature_validated.innerText = 'No Registrado'
						is_signature_validated.classList.add('text-danger')
						is_signature_validated.classList.remove('text-success')
						mobile.value = ''
						mobile.readOnly = false
						email.value = ''
						email.readOnly = false
    					alertify.error('Profesional no encontrado');
    					tuition.readOnly = false
					}
				})
			}else{
				alertify.warning('Ingrese el número de colegiatura');
			}
		}
	}
	set_profeessions_onchange()
	set_cip_inputs()
	set_cap_inputs()
	set_cellphone_case()
	set_upper_inputs()
}

search_profile_app()