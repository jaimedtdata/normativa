function f_consulta_Normal(e,
                           txtTextoBusqueda){
                           
                           //return true;
   efm = e.form.name;
   if(document.getElementById(efm + ":" + txtTextoBusqueda).value.length <= 3){
    //alert("Debe de ingresar un texto con mayor longitud."); //Modificado 2017-02-15
    return false;
   }            
   return true;
}


function f_valida_Busqueda_Avanzada(e, 
                                    txtAnioResolucion, 
                                    lblAnioResolucion,
                                    cboAreaPrimera,
                                    txtNroResolucion) {
    efm = e.form.name;
    var mensaje="";
    var pivoteError = 0;
    var valor = document.getElementById(efm + ":" + txtAnioResolucion);
    var objTmp;
    fnColorearLabel(efm, lblAnioResolucion, false);

    //VALIDANDO AÑO
    if (valor.value.length != 0) { //Si ha ingresado año
        if(check_numero(valor)){  //Es numérico el valor ingresado?
        pivoteError++;
        fnColorearLabel(efm, lblAnioResolucion, true);
        //mensaje= mensaje + "* El valor introducido en Año de Resolución es incorrecto. \n";
        document.getElementById(efm + ":" + txtAnioResolucion).value="";
        }
    }
    
    objTmp = document.getElementById(efm + ":" + cboAreaPrimera);
    
    if(typeof(objTmp) != 'undefined' && objTmp != null){
        if (document.getElementById(efm + ":" + cboAreaPrimera).text == ""){
        pivoteError++;
        objTmp = document.getElementById(efm + ":" + txtNroResolucion);
        
        if(typeof(objTmp) != 'undefined' && objTmp != null){
            fnColorearLabel(efm, txtNroResolucion, true);
        }
        
        //mensaje= mensaje + "* El valor introducido en Sigla es incorrecto. \n";
    }
    }
    
    
    
    if (pivoteError > 0) {
        //alert(mensaje);
        return false;
    }

    return true;
}

function fnColorearLabel(form, idLabel, blDataCorrecto) {
    nombreForm = "";
    if (idLabel.length > 0)
        nombreForm = form + ":" + idLabel;
    else 
        nombreForm = form;
    var label = document.getElementById(nombreForm);
    if (blDataCorrecto)
        label.style.color = "Red";
    else 
        label.style.color = "Black";

}

function check_numero(element) {
    var cant = element.value;
    var cant_es_flotante = isFloat(cant);
    if (isNaN(cant)) {
        return true;
    }
    else if (cant < 1) {
        return true;
    }
    else if (cant_es_flotante == true) {
        return true;
    }
    return false;
}

function isFloat(myNum) {
    var myMod = myNum % 1;
    if (myMod == 0) {
        return false;
    }
    else {
        return true;
    }
}

function mostrarContenido(rowIndex) {
    var x = document.getElementById('desCorta'+rowIndex);
    var y = document.getElementById('desLarga'+rowIndex);
    var a = document.getElementById('verMas'+rowIndex);
    var b = document.getElementById('verMenos'+rowIndex);
    if (x.style.display === 'none') {
        x.style.display = 'inline';
        y.style.display = 'none';
    } else {
        x.style.display = 'none';
        y.style.display = 'inline';
    }
}

function f_seleccionarBusqueda(){
    //alert('entro a f_seleccionarBusqueda');
   var x = document.getElementById('busqueda-rapida-content');
   var y = document.getElementById('busqueda-avanzada-content');
    //alert(x);
   /*
   if(x.style.display === 'block'){
        alert('Busq_rap');
        document.getElementById('FormListado1:b_RealizaBusqueda').click();
    }else{
        alert('Busq_avan');
        document.getElementById('FormListado:btnAceptar').click();
    }
   if(x.style.display === 'block' || x.style.display === 'inline'){
        alert('Busq_rap');
        document.getElementById('FormListado1:b_RealizaBusqueda').click();
    }else if(y.style.display === 'block' || y.style.display === 'inline'){
        alert('Busq_avan');
        document.getElementById('FormListado:btnAceptar').click();
    }else{
        alert('Sin definir')
    }*/
    if(x.style.display != 'none'){
        //alert('Busq_rap');
        document.getElementById('FormListado1:b_RealizaBusqueda').click();
    }else if(y.style.display != 'none'){
        //alert('Busq_avan');
        document.getElementById('FormListado:btnAceptar').click();
    }//else{
     //alert('Sin definir')
     //}
}