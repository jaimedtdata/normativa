const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

//value csrfToken
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

// hacemos la peticion
const sendSearchData = (pal_clave)=>{
    $.ajax({
        type : 'POST',
        url : 'result_search_ajax/',
        data : {
            'csrfmiddlewaretoken' : csrf,
            'pal_clave' : pal_clave
        },
        success : (res)=>{
            console.log(res.data);
            const data = res.data
            //si la respuesta es un array se ejecuta, preguntamos eso xq sabemos que si es un 
            //array entonces tiene objetos, de otro modo es un string y esta vacío
            // if (Array.isArray(data)){
            //     resultsBox.innerHTML = ""
            //     data.forEach(pal_clave =>{
            //         resultsBox.innerHTML += `
            //             <a href="${url}${pal_clave.pk}" class="item dropdown-item ">
            //                 <div class="row mt-2 mb-2">
            //                     <div class="col-2">
            //                         <img src="${pal_clave.image}" class="pal_clave-img" />
            //                     </div>
            //                     <div class="col-10">
            //                         <h5>${pal_clave.name}</h5>
            //                         <p class="text-muted">${pal_clave.studio}</p>
            //                     </div>
            //                 </div>
            //             </a>
            //         `
            //     })
            // } else{
            //     if (searchInput.value.length > 0){
            //         resultsBox.innerHTML=`<b>${data}</b>`
            //     } else {
            //         resultsBox.classList.add('not-visible')
            //     }
            // }
        },
        error : (err)=>{
            console.log(err);
        }
    })
}

searchInput.addEventListener('keyup', (e)=>{
    console.log(e.target.value);

    // mostramos la caja de resultados, classList.contains retorna true or false
    if (resultsBox.classList.contains('not-visible')){
        resultsBox.classList.remove('not-visible')
    }

    //send capture data from input id=search-input
    sendSearchData(e.target.value)
})