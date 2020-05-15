if (window == top) {
    window.addEventListener('keyup', doKeyPress, false);
}

function doKeyPress(event){
	
	if(event.shiftKey) {
        if(String.fromCharCode(event.keyCode) == '?') {
            alert('Shortcuts!')
        }   
    }
	
	
	
    if(event.ctrlKey && event.altKey && !event.shiftKey) {
        if(url = bookmarks[String.fromCharCode(event.keyCode)]) {
            window.open(url,"_self");
        }   
    }
}


