document.addEventListener('DOMContentLoaded', function () {
	$.get('https://fortonfish.com/hellosalut/?lang=fr', function (data, status) {
		if (status === 'success') {
			$('div#hello').text(data.hello);
		}
	});
});
