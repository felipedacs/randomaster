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

$( ".btn-composit" ).on('click', function( e ) {
    e.preventDefault();

    $(this).closest( "div" ).children("div.div-composit").toggle();
});