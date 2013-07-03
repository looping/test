function Controller(){
	document.onkeydown = function keyControl(){
		var myevent = window.event; 
		switch(myevent.keyCode){
        		case 13:{
				enterKeyPressed();
	                }break;
        	        case 37:{
				leftKeyPressed();
			}break;
			case 38:{
				upKeyPressed();
			}break;
			case 39:{
				rightKeyPressed();
			}break;
			case 40:{
				downKeyPressed();
			}break;
			default:{
			}break;
	}

	}
	function enterKeyPressed(){
		alert("enter!");
	}

	function leftKeyPressed(){
		alert("left!");
	}
	function upKeyPressed(){
		alert("up!");
	}
	function rightKeyPressed(){
		alert("right!");
	}
	function downKeyPressed(){
		alert("down!");
	}
}
