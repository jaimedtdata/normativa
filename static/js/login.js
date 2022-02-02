storage = window.localStorage
const remember_user = storage.getItem('remember_user')
const username = storage.getItem('username')
const password = storage.getItem('password')
if (remember_user == null) {
	storage.setItem('remember_user', false)
	storage.setItem('username', '')
	storage.setItem('password', '')
}
var username_input = document.getElementById('id_username'),
	password_input = document.getElementById('id_password'),
	remember_checkbox = document.getElementById('remember-me')
	form = document.getElementById('login-form')

function set_user_local(user, password, is_checked){
	storage.setItem('remember_user', is_checked)
	storage.setItem('username', user)
	storage.setItem('password', password)
}
function set_values(){
	username_input.value = username
	password_input.value = password
}

if (remember_user == 'false') {
	remember_checkbox.checked = false
}
else{
	remember_checkbox.checked = true
	set_values()
}

function set_remember_case(){
	if (remember_checkbox.checked) {
		set_user_local(username_input.value, password_input.value, true)
	}
	else{
		set_user_local('','',false)
	}
}

remember_checkbox.onchange = () =>{
	set_remember_case()
}

form.onsubmit = () =>{
	set_remember_case()
}

set_remember_case()
set_values()
