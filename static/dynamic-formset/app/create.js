function get_dynamic_attr(prefix){
    return {
        prefix: prefix,
        formTemplate: null,
        addText: ' Agregar',
        deleteText: 'X',
        addCssClass: 'btn btn-success btn-sm add-row',
        deleteCssClass: 'text-danger delete-row mt-2',
        formCssClass: 'dynamic-form',
        extraClasses: [],
        keepFieldValues: '',
        added: null,
        removed: null
    }
}