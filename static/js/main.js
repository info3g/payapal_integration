
var packagePrice;
var packageDiscountPrice;
var price;
packagePrice = 19;
packageDiscountPrice = 0;

if(packageDiscountPrice == 0) {
	price = packagePrice;
} else {
	price = packageDiscountPrice;
}


var packageName;
var totalPrice = price;
var dateSelected = false;


packageName = "Pest Tour";

var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
var hour = today.getHours();



var day = parseInt(dd) + 1;

var bbq_minDate = mm + '-' + day + '-' + yyyy;
var tour_minDate = mm + '-' + dd + '-' + yyyy;

var min_date;

if(packageName =="BBQ/Quiz Night" || hour >= 12) {
     		min_date = bbq_minDate;
} else {
     		min_date = tour_minDate;
}


$(".datepicker").datepicker({
	beforeShowDay: function(date) {
		if(packageName == "Pest Tour") {

       return [date.getDay() == 4 || date.getDay() == 5 || date.getDay() == 6];
   		} else if(packageName == "Buda Pack") {
   			return [date.getDay() == 4];
   		}
    },
    onSelect: function() {
        var dateObject = $(this).datepicker('getDate');
        var date = $.datepicker.formatDate("yy-mm-dd", dateObject);
        insertDate(date);
        updateDate();
        dateSelected = true;
    },
    minDate: new Date(min_date),
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

	$('.packagePrice').text(totalPrice + " €");

	updatePerson();
	checkCoupon();

});

$(".plusCount").click(function() {



	hCount++;

	$(".count").text(hCount);
	$("#hCount").val(hCount);

	totalPrice = hCount * price;

	$("#totalPrice").val(totalPrice);

	$('.packagePrice').text(totalPrice + " €");

	updatePerson();
	checkCoupon();

});

$('.submitBtn').click(function(event) {

	var docu = $('#docs').val();

	if(docu == "false") {

	event.preventDefault();

	$(".formError").show('fade');
	$(".formError").text("You must accept our documents!");

	}

});

//form cucc
var el_num = 1;
var formStep = 1;

function nextFormStep() {

	var name = $("#buyer_name").val();
	var email = $("#buyer_email").val();
	var country = $('#buyer_country').val();
	var zip = $('#buyer_zip').val();
	var address = $('#buyer_address').val();


	$(".formError").css({"display":"none"});


		if(el_num == 1) {

			if(dateSelected == true) {

				$('.headCount').toggle("fade");
				$('html,body').animate({
					scrollTop : $(".headCount").offset().top
				}, 800);
				el_num++;
				formStep++;

				$('.sumPerson').css({"display":"flex"});

			} else {

				$(".formError").show('fade');
				$(".formError").text("Choose a date!");
			}

		} else if (el_num==2) {



				$('.persInfo').toggle("fade");
				$('html,body').animate({
					scrollTop : $(".persInfo").offset().top
				}, 800);
				el_num++;
				formStep++;


		} else if(el_num == 3) {

			if(name !== "" && email !== "" && country !== "" && zip !== "" && address !== "") {


		 		$('.paymentSec').toggle("fade");
		 		$('html,body').animate({
					scrollTop : $(".paymentSec").offset().top
				}, 800);
				el_num++;
				formStep++;

				$('.formNext').css({"display":"none"});
				$('.submitBtn').css({"display":"inline-block"});

			} else {

				$(".formError").show('fade');
				$(".formError").text("Fill out all the fields!");

			}

		 }



		$("#form-step").text(" " + formStep);

}

function checkCoupon() {


	var code = $('#couponCode').val();

	if(code != "") {

		if(coupons.hasOwnProperty(code)) {
			var discount = coupons[code] * hCount;

			var discPrice = totalPrice-discount;

			$('#couponName').val(code);

			discountPrice(discPrice);

			$('.coupon').css({"display":"none"});
			$('.couponCard').show("fade");
			$('.coupon_name').text(code);

		} else {
			$('.discountError').show("fade");
		}
	}

}

function discountPrice(y) {

	var newTotalPrice = y;

	$('.realPrice').text(totalPrice + " €");
	$('.packagePrice').text(newTotalPrice + " €");
	$('#totalPrice').val(newTotalPrice);

}

function updateDate() {

	$('.sumDate').css({"display":"flex"});

	$('.summaryDate').text($('#tour_date').val());

}

function updatePerson() {


				var people = $('#hCount').val();

				if(people > 1) {

				$('.summaryPerson').text(people + " people");

				} else {
				$('.summaryPerson').text(people + " person");
				}


}

function setDoc(y) {

	$(y).addClass("purple");
	$("#docs").val("true");


}

function insertDate(y) {

	var input = document.querySelector("#tour_date");
	input.value = y;

}

function scrollDown(y) {

	$('html,body').animate({
		scrollTop: $("."+y).offset().top
	}, 800);

}
