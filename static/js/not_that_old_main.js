// var coupons = JSON.parse('{"taxi_01":3.0, "hostel_01":2.0}');

var packageInfo = JSON.parse('{"model": "pages.packages", "pk": 1, "fields": {"name": "Buda Tour", "slug": "buda-tour", "price": 42.0, "discount_price": 39.0, "payment_option": "both"}}');

var pack = packageName;
console.log(pack);

// var packageInfo = JSON.parse({{serialized_package}});


var package = packageInfo.fields.name;
var price = packageInfo.fields.price;
var totalPrice = price;
var dateSelected = false;

$(".datepicker").datepicker({
    onSelect: function() {
        var dateObject = $(this).datepicker('getDate');
        var date = $.datepicker.formatDate("yy-mm-dd", dateObject);
        insertDate(date);
        updateDate();
        dateSelected = true;
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

	$('.packagePrice').text(totalPrice + " €");

	updatePerson();

});

$(".plusCount").click(function() {



	hCount++;

	$(".count").text(hCount);
	$("#hCount").val(hCount);

	totalPrice = hCount * price;

	$("#totalPrice").val(totalPrice);

	$('.packagePrice').text(totalPrice + " €");

	updatePerson();

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

	if(coupons.hasOwnProperty(code)) {
		var discount = coupons[code];

		var discPrice = totalPrice-discount;

		$('#couponName').val(code);

		discountPrice(discPrice);

		$('.coupon').css({"display":"none"});
		$('.couponCard').show("fade");

	} else {
		$('.discountError').show("fade");
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
