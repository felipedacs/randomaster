$( ".add" ).on('click', function( e ) {

    e.preventDefault();

    var nome = $(this).closest( "div" ).children("div.nome_class").text();
    var valorExistente = $("span." + nome + "_total").text();

    valorExistente++;

    $("span." + nome + "_total").text(valorExistente);
    $("span." + nome + "_total_user").text(valorExistente);
    /*
    var target = $(e.target).text();

    $( ".projeto" ).removeAttr("style"); // reseta posições
    
    $('div.projeto:not(:contains("' + target + '"))').closest( "div.projeto" ).hide();
    $('div.projeto:contains("' + target + '")').closest( "div.projeto" ).show();

    var divs = $('div.projeto:contains("' + target + '")');
    var qtd = divs.length;
    $( ".resultadoPesquisa").show();
    $( "#targetProjetos").removeClass();
    $( "#targetProjetos").text(target + " (" + qtd + ")").addClass("tag badge tag-" + target);
    */
});

$( ".rem" ).on('click', function( e ) {

    e.preventDefault();

    var nome = $(this).closest( "div" ).children("div.nome_class").text();
    var valorExistente = $("span." + nome + "_total").text();
    if(valorExistente == 0){
        //não faz nada
    } else {
        valorExistente--;
    }
    
    $("span." + nome + "_total").text(valorExistente);
    $("span." + nome + "_total_user").text(valorExistente);
    /*
    var target = $(e.target).text();

    $( ".projeto" ).removeAttr("style"); // reseta posições
    
    $('div.projeto:not(:contains("' + target + '"))').closest( "div.projeto" ).hide();
    $('div.projeto:contains("' + target + '")').closest( "div.projeto" ).show();

    var divs = $('div.projeto:contains("' + target + '")');
    var qtd = divs.length;
    $( ".resultadoPesquisa").show();
    $( "#targetProjetos").removeClass();
    $( "#targetProjetos").text(target + " (" + qtd + ")").addClass("tag badge tag-" + target);
    */
});
