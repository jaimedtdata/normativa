
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
                
                
                if (data.data.dni){
                    userExists=`<div>Ya tienes una cuenta registrada <a href="${base_url}/login">Inicia sesión aquí</a></div>`
                    test.innerHTML = userExists
                }
            })
        
    })

