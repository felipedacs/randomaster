function removeVirgulaSobrando(){
    var input = $("#input_codigo").val();

    if(input[0] == ','){
        input = input.substring(1,input.length);
        $("#input_codigo").val(input);
    } else if (input[input.length-1] == ','){
        input = input.substring(0,input.length-1);
        $("#input_codigo").val(input);
    }
}

$( ".add" ).on('click', function( e ) {
    e.preventDefault();

    var nome = $(this).closest( "div" ).children("div.nome_class").text();

    var valorExistente = $("span." + nome + "_total").text();
    valorExistente++;
    $("span." + nome + "_total").text(valorExistente);

    nomeExistente = $("#input_codigo").val();
    var nomeNovo = nomeExistente+ ',' + nome ;
    
    $("#input_codigo").val(nomeNovo);

    removeVirgulaSobrando();
});

$( ".rem" ).on('click', function( e ) {
    e.preventDefault();

    var nome = $(this).closest( "div" ).children("div.nome_class").text();
    var valorExistente = $("span." + nome + "_total").text();
    if(valorExistente != 0){
        valorExistente--;
        $("span." + nome + "_total").text(valorExistente);

        var nomeExistente = $("#input_codigo").val();

        var nomeRemovido = nomeExistente.replace(nome, "");

        $("#input_codigo").val(nomeRemovido);

        removeVirgulaSobrando();
        //$("#input_codigo").val(nomeRemovido);
    } else {
        //não faz nada        
    }
});

$( "#btn-bash-div" ).on('click', function( e ) {
    e.preventDefault();

    $(".bash-div").toggle();
});

$( "#btn-form-div" ).on('click', function( e ) {
    e.preventDefault();

    $(".form-div").toggle();
});