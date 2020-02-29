var package;
var price;
var totalPrice;

price = 21;

$(".datepicker").datepicker({
    onSelect: function() { 
        var dateObject = $(this).datepicker('getDate');
        var date = $.datepicker.formatDate("dd-mm-yy", dateObject); 
        insertDate(date);
    }
});

var hCount = 1;

$(".minusCount").click(function() {

	if(hCount != 1) {

	hCount--;

	$(".count").text(hCount);
	$("#hCount").val(hCount);
	
	}

	totalPrice = hCount * price;

	$("#totalPrice").val(totalPrice);

});

$(".plusCount").click(function() {

	

	hCount++;

	$(".count").text(hCount);
	$("#hCount").val(hCount);

	totalPrice = hCount * price;

	$("#totalPrice").val(totalPrice);
	


});

//form cucc
var el_num = 1;
var formStep = 1;

function nextFormStep() {

	/*var name = $("#name").val();
	var email = $("#email").val();
	var msg = $("#message").val();*/

	$(".name-error").css({"display":"none"});
	$(".email-error").css({"display":"none"});
	$(".msg-error").css({"display":"none"});	


		if(el_num == 1) {

			/*if(name !== "") {*/

				$('.headCount').toggle("fade");
				$('html,body').animate({
					scrollTop : $(".headCount").offset().top
				}, 800);
				el_num++;
				formStep++;

			/*} else {

				$(".name-error").css({"display":"block"});
				$(".mail-ok").css({"display":"none"});*/

			} else if (el_num==2) {

			/*if(email !== "") {*/

				$('.persInfo').toggle("fade");
				$('html,body').animate({
					scrollTop : $(".persInfo").offset().top
				}, 800);
				el_num++;
				formStep++;
				/*$('.form-next').css({"display":"none"});
				$('.form-sub').css({"display":"inline-block"});

			} else {

				$(".email-error").css({"display":"block"});
				$(".mail-ok").css({"display":"none"});

			}*/

		 	} else if(el_num == 3) {

		 		$('.paymentSec').toggle("fade");
		 		$('html,body').animate({
					scrollTop : $(".paymentSec").offset().top
				}, 800);
				el_num++;
				formStep++;

				$('.formNext').css({"display":"none"});
				$('.submitBtn').css({"display":"inline-block"});

		 	}

		

		$("#form-step").text(" " + formStep);

}

function setDoc(y) {

	$(y).addClass("purple");
	$("#docs").val("true");


}

function insertDate(y) {

	var input = document.querySelector("#tour_date");
	input.value = y;

}

//select

function showOptions(x) {
		
			var list = document.querySelector(x);
			
			if(list.style.display == "block") {
				
				list.style.display = "none";
				$(x).animate({ "opacity" : "0", "margin-top" : "0px"});
				
			} else {
				
				list.style.display = "block";
				$(x).animate({ "opacity" : "1", "margin-top" : "10px"});
			}
		
		};
		
function selectValue(y,x) {

			

			if(filterData.city == "budapest") {

				document.querySelector('.district-select').style.display = "inline-block";
				$('.district-select').animate({"opacity": "1"});

			} if(filterData.city != "budapest") {

				document.querySelector('.district-select').style.display = "none";
				$('.district-select').animate({"opacity": "0"});

			}

			var parent = $(y).parent();
			
			$(parent).animate({ "opacity" : "0", "margin-top" : "0px"});

			var clicked = y.innerHTML;
			
			document.querySelector(x).innerHTML = clicked;


			
			$(parent).css({"display":"none"});

};