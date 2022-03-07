
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    var dniForm = document.getElementById('dni-form')
    var dniInput = document.getElementById('dni-input')
    var url = '/dni/'
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

        fetch(url, options)
            .then(resp =>resp.json())
            .then(data => {
                test=document.getElementById('test')
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
                        formRegister = document.getElementById('form-signup')
                        formRegister.classList.remove('form-display')
                        document.getElementById('id_identity').value= dniInput.value
                        dniForm.classList.add('form-display')//hide form dni
                        document.getElementById('register_title').innerHTML= `Bienvenido ${user_data.names}, completa tus datos de registro`
                        hideInputsCAP()
                       //window.location.replace(`${base_url}/sign-up-erp/`);

                        
                        

                    }else{
                        //users thar are not in Member model neither APimember, they externals users(other professions)
                        console.log(user_data.msg);
                        document.getElementById('id_identity').value= dniInput.value
                        formRegister=document.getElementById('form-signup')
                        formRegister.classList.remove('form-display')
                        //dniForm.classList.add('form-display')//hide form dni
                        
                        
                        // document.getElementById('id_tuition').placeholder="Solo para colegiados";
                        // document.getElementById('id_tuition').disabled=true
                        // document.getElementById('id_secret_code').placeholder="Solo para colegiados";
                        // document.getElementById('id_secret_code').disabled=true
                        


                    }
                }
            })
        
    })
    
    const hideInputsCAP = ()=>{
        document.getElementById('id_names').setAttribute('type', 'hidden')
        document.getElementById("label_names").style.display = 'none';
        document.getElementById('id_first_surname').setAttribute('type', 'hidden')
        document.getElementById("label_first_surname").style.display = 'none';
        document.getElementById('id_second_surname').setAttribute('type', 'hidden')
        document.getElementById("label_second_surname").style.display = 'none';
        document.getElementById('id_second_surname').setAttribute('type', 'hidden')
        document.getElementById("label_second_surname").style.display = 'none';

        document.getElementById('id_identity').setAttribute('type', 'hidden')
        document.getElementById("label_identity").style.display = 'none';
        document.getElementById('id_profession').setAttribute('type', 'hidden')
        document.getElementById("label_profession").style.display = 'none';
        document.getElementById('id_tuition').setAttribute('type', 'hidden')
        document.getElementById("tuition_title").style.display = 'none';
        document.getElementById('id_secret_code').setAttribute('type', 'hidden')
        document.getElementById("label_secret_code").style.display = 'none';
        document.getElementById('id_person_type').setAttribute('type', 'hidden')
        document.getElementById("label_person_type").style.display = 'none';
        document.getElementById('id_mobile').setAttribute('type', 'hidden')
        document.getElementById("label_mobile").style.display = 'none';
        document.getElementById('id_phone').setAttribute('type', 'hidden')
        document.getElementById("label_phone").style.display = 'none';
        document.getElementById('id_address').setAttribute('type', 'hidden')
        document.getElementById("label_address").style.display = 'none';
    }