"use strict";

document.querySelectorAll("input.currency").forEach(function(el) {
	el.addEventListener("change", function() {
		var val = parseFloat(el.value);
		if (isNaN(val)) {
			return;
		}

		el.value = val.toFixed(2);
	});
});
