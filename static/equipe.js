$("#btn-copy").on('click', function( e ) {
	e.preventDefault();

	var codigo = $("#codigo_clip");

	codigo.select();

	document.execCommand("Copy");
});

$("#btn-refresh").on('click', function( e ) {
	e.preventDefault();

	window.location.reload();
});

$( "#btn-auditoria-div" ).on('click', function( e ) {
	e.preventDefault();

	$(".auditoria-div").toggle();
});

$( ".btn-equipe" ).on('click', function( e ) {
	e.preventDefault();

	$(this).closest( "div" ).children("table").toggle();
});

$( ".input-composit" ).focusout(function( e ) {
	e.preventDefault();
	var texto = $(this).val().toUpperCase();
	$(this).closest( "div" ).closest( "section" ).children("div.div-composit").children("p").text(texto);
});


$( ".btn-foto" ).on('click', function( e ) {
	e.preventDefault();

	var divfoto = '.div-foto-' + $(this).val();
	var divimgfoto = '.div-img-foto-' + $(this).val();
	
	html2canvas(document.querySelector(divfoto)).then(canvas => {
		$(divimgfoto).html(canvas);
	});
/*
	var divText = $(divimgfoto).outerHTML;
    var myWindow = window.open('', '', 'width=200,height=100');
    var doc = myWindow.document;
    doc.open();
    doc.write($(divimgfoto).get());
    doc.close();
    */
});