
const params = new Proxy(new URLSearchParams(window.location.search), {
get: (searchParams, prop) => searchParams.get(prop),
});
// Get the value of "some_key" in eg "https://example.com/?some_key=some_value"
var gtn = params.gtn; // "grupo de tipo de norma"
var titulo = params.norma; // "Titulo de grupo de tipo de norma"

// PRIMER VALOR PARA TOPICO NORMA
$('#topico').val(params.t)

if(titulo == null) { // si el titulo no esta definido muestro el filtro de tipos de norma
    titulo = $('#topico option:selected').text()
    $('#subnormas_caja').removeClass('d-none')
    $('#right').removeClass('col-lg')
    $('#right').addClass('col-lg-9')   
}

$('#titulo').html(titulo);

const normas = {{ normas|safe }}
const subtipos_uso_json = {{ sbu|safe }}
const tipos_uso_json = {{ tu|safe }}
const tipos_norma_json = {{ tn|safe }}
var uac = normas; // temporal para ejecutar mis filtros

var topico = $("#topico"),
tipos_norma = $("#tipos_norma"),
search = $("#filter_input"),
tipos_uso = $("#area_normas"),
subtipos_uso = $('#subtipo_usos'),
keywords = $("#keywords"),

date_range = undefined,

var normas_tabla = $('#normas-tabla').DataTable({
    searching: false,
    ordering:  true,
    lengthChange: false,
    responsive: true,
})

$('#datetimes').daterangepicker({
    locale: {
        format: 'YYYY-MM-DD'
    }
});

topicoNorma()

let array_tipos_norma = []

$("#tipos_norma option").each(function()
{
    array_tipos_norma.push($(this).val())
});

tipos_norma.val(array_tipos_norma)

array_tipos_norma = [] // vaciando array

$("#tipos_norma option").each(function()
{
    if(gtn == $(this).attr("grupo"))
    {
        array_tipos_norma.push($(this).val())
    }
});

tipos_norma.val(array_tipos_norma) // ME QUEDO CON LAS OPCIONES DEL TOPICO

execFilters() // PRIMERA EJECUCIÓN

tipos_norma.change(function(){
    execFilters() 
});

search.keyup(function(){    
    execFilters()  
})

tipos_uso.change(function(){

    var options_sbu = `<option class="text-wrap" value="0">TODOS</option>`
    
    subtipos_uso_json.forEach( sbu => {
        
        if( tipos_uso.val() == 0 ) {
            options_sbu += /*html*/`<option class="text-wrap" value="${sbu.id}">${sbu.name}</option>`     
        } else if( sbu.tipo_uso_id == tipos_uso.val() ) {
            options_sbu += /*html*/`<option class="text-wrap" value="${sbu.id}">${sbu.name}</option>`
        }       

    })

    subtipos_uso.html(options_sbu)
    execFilters()  
})

topico.change(function(){

    var options_tn = ``

    tipos_norma_json.forEach( tn => {
        if( tn.topico_id == topico.val() ) {
            if ( !tn.order.includes('.') ) {
                options_tn += /*html*/`<option grupo="${tn.grupo_id}" class="text-wrap font-weight-bold" value="${tn.id}">${tn.name}</option>`
            }
            else {
                options_tn += /*html*/`<option grupo="${tn.grupo_id}" class="text-wrap" value="${tn.id}">${tn.name}</option>`
            }
        }            
    })

    tipos_norma.html(options_tn)
})

subtipos_uso.change(function(){
    sbu_id = $("#subtipo_usos").val()
    subtipo_uso_option = $("#subtipo_usos option:selected").text()
    execFilters()
})

$('#datetimes').change(function(){
    date_range = $('#datetimes').data('daterangepicker')
    execFilters()
})

keywords.change(function(){
    execFilters()
})

function getNormativas(tipo_normas)
{
    if (tipo_normas.length != 0) {
        let respuesta = [];
    
        tipo_normas.forEach(sn => {
            let r = uac.filter(n => {
                        return n.tipo_norma_id == sn
                    })

            respuesta = respuesta.concat(r)
        })
        return respuesta
    } else {
        return uac
    }
}

function getSearchNormativas(search)
{
    if( search != undefined ) {
        return uac.filter(n => {
            return n.norma.toLowerCase().includes(search.toLowerCase()) 
                    || n.denominacion.toLowerCase().includes(search.toLowerCase()) 
                    || n.base_legal.toLowerCase().includes(search.toLowerCase())
                    || n.descripcion.toLowerCase().includes(search.toLowerCase())
        })
    } else {
        return uac
    }
}

function getTipoUsoNormativas(tu_id)
{
    if (tu_id != 0) {
        return uac.filter(n => {
            return n.tipos_uso_id.includes(parseInt(tu_id))
        })
    } else {
        return uac
    }
}

function getSubTipoUsoNormativas(sbu_id)
{
    if (sbu_id != 0) {
        return uac.filter(n => {
            return n.subtipos_uso_id.includes(parseInt(sbu_id))
        })
    } else {
        return uac
    }
}

function getNormasPorFechas(date_range)
{
    if (date_range != undefined) {

        return uac.filter(n => {
            return moment(n.fecha_publicacion) >= moment(date_range.startDate.format('YYYY-MM-DD')) && moment(n.fecha_publicacion) <= moment(date_range.endDate.format('YYYY-MM-DD'))
        })
    } else {
        return uac
    }
}

function getNormasPorKeywords(keywords)
{

    if (keywords.length != 0) {
        let respuesta = [];

        keywords.filter(k => {
            let r = uac.filter(n => {
                        return n.palabras_clave.includes(parseInt(k))
                    })

            respuesta = respuesta.concat(r)
        })

        return respuesta
    } else {
        return uac
    }
}

function topicoNorma()
{
    var options_tn = ``

    tipos_norma_json.forEach( tn => {
        if( tn.topico_id == topico.val() ) {
            if ( !tn.order.includes('.')  ) {
                options_tn += /*html*/`<option grupo="${tn.grupo_id}" class="text-wrap font-weight-bold" value="${tn.id}">${tn.name}</option>`
            }
            else {
                options_tn += /*html*/`<option grupo="${tn.grupo_id}" class="text-wrap" value="${tn.id}">${tn.name}</option>`
            }
        }            
    })

    tipos_norma.html(options_tn)
}

function execFilters()
{
    uac = getNormativas(tipos_norma.val())
    uac = getSearchNormativas(search.val())
    uac = getTipoUsoNormativas(tipos_uso.val())
    uac = getSubTipoUsoNormativas(subtipos_uso.val())
    uac = getNormasPorKeywords(keywords.val())
    uac = getNormasPorFechas(date_range)

    normas_tabla.destroy()

    render(uac)

    normas_tabla = $('#normas-tabla').DataTable({
        searching: false,
        ordering:  true,
        lengthChange: false,
    })
    

    uac = normas
}

function render(resultado)
{
    html = ``

    resultado.forEach((r) => {
        html += /*html*/
                `<tr >
                    <td>${r.tipo_norma}</td>
                    <td>${r.tipos_uso}</td>
                    <td>${r.subtipos_uso}</td>
                    <td >
                        ${r.norma}`;
                    
        if (r.es_vigente) {
            html += /*html*/`
                <span class="fst-italic fw-lighter fs-7 text-center text-danger">*No vigente</span>
            `
        }

        html +=/*html*/
            `</td>
                <td>
                    ${r.denominacion}`
                    if (r.estado == 'NV') {
                        html += /*html*/`
                        <small class="fst-italic fw-lighter fs-7 text-danger">*No Vigente</small>
                        `
                    } else if (r.estado == 'DP') {
                        html += /*html*/` <small class="fst-italic fw-lighter fs-7 text-danger">*Derogado Parcialmente</small>`
                    }
                    
            html += /*html*/`
                </td>
                
                <td >${r.descripcion}</td>
                <td >${r.base_legal}</td>
                <td >${r.articulo}</td>
                <td class="text-center">
                    `
                    
                    if (r.document) {
                        html += /*html*/`
                            <a target="_blank" href="/normativas/${r.id}/ver-pdf">
                                <i class="fa fa-file-pdf fa-2x text-danger mr-1" aria-hidden="true"></i>
                            </a>

                    
                        `
                    } else {
                        html += /*html*/` <span class="text-center"><i class="fa fa-minus fa-2x text-dark" aria-hidden="true"></i></span>`
                    }
                    
                    html += /*html*/`
                </td>
                <td >
                    ${r.fecha_publicacion}
                </td>
            </tr>`
    })

    $('#normas_edificatorias').html(html);
}
