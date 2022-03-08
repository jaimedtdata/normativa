
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

var dniForm = document.getElementById('dni-form')
var capForm = document.getElementById('form-cap')
var externalForm = document.getElementById('form-external')
var dniInput = document.getElementById('dni-input')
var urlDni = '/dni/'
var base_url = window.location.origin;
    
    dniForm.addEventListener('submit', (e)=>{
        form = new FormData(dniForm)
        e.preventDefault()
        const dni = dniInput.value
        

        var options= {
            method: "POST",
            body : form,
            credentials: "same-origin",
            headers: {
            "X-CSRFToken": csrftoken,
            }
        }

        fetch(urlDni, options)
            .then(resp =>resp.json())
            .then(data => {
                const test=document.getElementById('test')
                console.log(data.data)
                const user_data = data.data
                
                
                if (user_data.dni){
                    //users that are in model Member
                    console.log(user_data.msg);
                    userExists=`<div>Ya tienes una cuenta registrada <a href="${base_url}">Inicia sesión aquí.</a></div>
                    <div>Si olvidaste tu contraseña <a href="${base_url}/password_reset/">recuperala aquí.</a></div>`
                    test.innerHTML = userExists
                    document.getElementById('dni-input').disabled=true
                    document.getElementById('input-value').disabled=true
                    

                }else{
                    //users that are in ERP but still not have account in this system
                    if (user_data.cap){
                        console.log(user_data.msg);
                        const cap = user_data.cap
                        blockCap = document.getElementById('block-cap')
                        blockCap.classList.remove('form-hide')
                        dniForm.classList.add('form-hide')//hide form dni
                        document.getElementById('title_cap').innerHTML= `Bienvenido(a) ${user_data.names}, completa tus datos de registro`
                       //window.location.replace(`${base_url}/sign-up-erp/`);

                       capForm.addEventListener('submit', (e)=>{
                            e.preventDefault()
                            RegisterUserCap(cap, user_data)
                       })

                        
                        

                    }else{
                        //users thar are not in Member model neither APimember, they externals users(other professions)
                        console.log(user_data.msg);
                        document.getElementById('id_formulario2-identity').value= dniInput.value
                        blockExternal=document.getElementById('block-external')
                        blockExternal.classList.remove('form-hide')
                        dniForm.classList.add('form-hide')//hide form dni
                        
                        externalForm.addEventListener('submit', (e)=>{
                            e.preventDefault()
                            RegisterExternalUser()
                        })
                        
                        


                    }
                }
            })
        
    })
    
const RegisterUserCap = (cap, user_data)=>{
    const urlCap = '/api/cap/'
    const form = new FormData()
    const email = document.getElementById('id_formulario1-email').value
    const password1 = document.getElementById('id_formulario1-password1').value
    const password2 = document.getElementById('id_formulario1-password2').value
    //form.append("cap",cap)
    form.append('email', email)
    form.append('password1', password1)
    form.append('password2', password2)
    form.append('cap', cap)
    var optionscap= {
        method: "POST",
        body : form,
        credentials: "same-origin",
        headers: {
        "X-CSRFToken": csrftoken,
        }
    }

    fetch(urlCap, optionscap)
        .then(resp => resp.json())
        .then(data =>{
            //show errors in the each field
            if (data.data.non_field_errors){
                document.getElementById('password_error_form1').innerHTML=  `<ul><li>${data.data.non_field_errors}</li></ul>`
            }

            if (data.error){
                console.log(data.error);
                document.getElementById('error_id_formulario1-email').innerHTML=  `<ul><li>${data.data.email}</li></ul>`
                if(data.data.email === undefined){
                    document.getElementById('error_id_formulario1-email').classList.add('form-hide')
                    document.getElementById('success_id_formulario1-email').innerHTML=  'correcto'
                    
                };
            }
            
            //succes register
            if (data.success){
                document.getElementById('alert-succes').innerHTML = `
                <div class="alert alert-success" role="alert">
                  <h3> <b> ${user_data.names}</b>, Te has Registrado Existosamente. </h3>
                    <div>
                       <h6> Para ingresar a la plataforma por favor  
                        <a href="/">inicia sesión</a>.</h6>
                    </div>
                </div>
            `
            capForm.reset()
            document.getElementById('block-cap').classList.add('form-hide')
            //window.location.replace(`${base_url}/success_sign_up/`);

            }

            
            console.log(data);
            
        })
        .catch(error => {
            //console.log( error)
        })
}

const RegisterExternalUser = ()=>{
    
    const urlExternalUser = '/api/member-external/'
    const form = new FormData()
    const names = document.getElementById('id_formulario2-names').value
    const first_surname = document.getElementById('id_formulario2-first_surname').value
    const second_surname = document.getElementById('id_formulario2-second_surname').value
    const identity = document.getElementById('id_formulario2-identity').value
    const mobile = document.getElementById('id_formulario2-mobile').value
    const phone = document.getElementById('id_formulario2-phone').value
    const email = document.getElementById('id_formulario2-email').value
    const address = document.getElementById('id_formulario2-address').value
    const password1 = document.getElementById('id_formulario2-password1').value
    const password2 = document.getElementById('id_formulario2-password2').value

    form.append('names', names)
    form.append('first_surname', first_surname)
    form.append('second_surname', second_surname)
    form.append('identity', identity)
    form.append('mobile', mobile)
    form.append('phone', phone)
    form.append('email', email)
    form.append('address', address)
    form.append('password1', password1)
    form.append('password2', password2)

    var optionsExternal= {
        method: "POST",
        body : form,
        credentials: "same-origin",
        headers: {
        "X-CSRFToken": csrftoken,
        }
    }

    fetch(urlExternalUser, optionsExternal)
        .then(resp=> resp.json())
        .then(data =>{
            console.log(data)
            console.log(data.data.non_field_errors);

            //show errors in the each field
            if (data.data.non_field_errors){
                document.getElementById('password_error_form2').innerHTML=  `<ul><li>${data.data.non_field_errors}</li></ul>`
            }
            
            if (data.error){
                console.log(data.error);
                document.getElementById('error_id_formulario2-email').innerHTML=  `<ul><li>${data.data.email}</li></ul>`
                document.getElementById('error_id_formulario2-mobile').innerHTML=  `<ul><li>${data.data.mobile}</li></ul>`
                if(data.data.email === undefined){
                    document.getElementById('error_id_formulario2-email').classList.add('form-hide')
                    document.getElementById('success_id_formulario2-email').innerHTML=  'correcto'
                    
                };
                if(data.data.mobile === undefined){
                    document.getElementById('error_id_formulario2-mobile').classList.add('form-hide')
                    document.getElementById('success_id_formulario2-mobile').innerHTML=  'correcto'
                    
                };
            }

            //succes register
            if (data.success){
                document.getElementById('alert-succes').innerHTML = `
                <div class="alert alert-success" role="alert">
                   <h3> <b> ${data.data.names}</b>, Te has Registrado Existosamente.</h3>
                   <div>
                       <h6> Para ingresar a la plataforma por favor  
                        <a href="/">inicia sesión</a>.</h6>
                    </div>
                </div>
            `
            externalForm.reset()
            document.getElementById('block-external').classList.add('form-hide')
            //window.location.replace(`${base_url}/success_sign_up/`);

            }
        })
        .catch(error => {
            //console.log( error)
            

        })


}


// const checkDni = (event)=>{
//     value = dniInput.value
//     if (event.keyCode === 13) {
//         if (value.length < 8){
//             document.getElementById('error_id_input_dni').innerHTML = "Ingresa un DNI válido."
//         }
//     }
    
// }

// dniInput.addEventListener('keyup', checkDni)
