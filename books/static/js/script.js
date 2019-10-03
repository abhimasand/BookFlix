var selectables = document.querySelectorAll("#selectables .item");
var submitSelected = document.querySelector("#submitSelected");

var selected = [];

for (var i = 0; i < selectables.length; i++) {
	selectables[i].addEventListener("click", handleSelect);
}

function handleSelect() {
	console.log(this.id);
	if (this.classList.contains("selected")) {
		for (var i = 0; i < selected.length; i++) {
			if (selected[i] === this.id) {
				selected.splice(i, 1);
				break;
			}
		}
	} else {
		selected.push(this.id);
	}

	this.classList.toggle("selected");
	console.log(selected);
}

submitSelected.onclick = function() {
	$.ajax({
		type: "POST",
		url: "/read_books/handle_selected_books",
		data: {
			"selected[]": selected
		},
		success: function(data) {
			console.log("success: ", data);
			window.location.href = "/user_books/read_books";
			// Redirect here
		}
	})
};
