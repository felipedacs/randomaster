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
