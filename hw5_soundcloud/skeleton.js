
// Event hander for calling the SoundCloud API using the user's search query
$('#call_api').on('click', function callAPI() {
// $('#call_api').on('click', function callAPI(query) {
	$("#query_output").empty()

	var query = $("input[name=query_input]").val();
		$.get("https://api.soundcloud.com/tracks?client_id=b3179c0738764e846066975c2571aebb",
			{'q': query,
			// {'q': "blink182",
			'limit': '200'},
			function(data) {
				// PUT IN YOUR CODE HERE TO PROCESS THE SOUNDCLOUD API'S RESPONSE OBJECT
				// HINT: CREATE A SEPARATE FUNCTION AND CALL IT HERE
				console.log(data)
				n=1
				for (i=0; i<20; i++) {
					console.log(n + ". " + data[i].title + "; " + data[i].title);

					var attach_img = data[i].artwork_url
					if(attach_img === null) {
						attach_img = "img/soundcloud_logo.png"
					}

					console.log(typeof attach_img)
					console.log(attach_img)
					$("#query_output")
						// .append("<button> Play </button>" + n + ". " + data[i].title + "; " + data[i].permalink_url + "</br></br>");
						.append("<div class='half-container'> <p>" + data[i].title + "</p> <button> move </button> <img alt=" + data[i].permalink_url + " src=" + attach_img + "> </div>");
					n+=1;
				}
			},'json'
		);
	});

$('#query_output').on('click', 'button', function() {
	move_output = $(this)
	// move_output.parent().removeClass( "half-container" ).addClass( "full-container" ).append("<button class='up'> Up </button>").append("<button class='down'> Down </button>");
	
	// $("#chosen_song").prepend(move_output.parent());
	$(move_output.parent()).clone().prependTo("#chosen_song").addClass( "full-container" ).append("<button class='up'> Up </button>").append("<button class='down'> Down </button>");
	// move_output.html("Remove");

})

$('#query_output').on('click', 'img', function() {
	$('#stratus').remove();

	var url = $(this)[0].alt;
	console.log("THIS IS THE URL: " + url);
	// Create a new Stratus player using the clicked song's permalink URL
	$.stratus({
      key: "b3179c0738764e846066975c2571aebb",
      auto_play: true,
      align: "bottom",
      // links: "https://soundcloud.com/5-seconds-of-summer/2-5-seconds-of-summer-i-miss"
      links: url
    });

})

// when click button
$("#chosen_song").on('click', 'img', function changeTrack() {
	$('#stratus').remove();

	var url = $(this)[0].alt;
	console.log("THIS IS THE URL: " + url);
	// Create a new Stratus player using the clicked song's permalink URL
	$.stratus({
      key: "b3179c0738764e846066975c2571aebb",
      auto_play: true,
      align: "bottom",
      // links: "https://soundcloud.com/5-seconds-of-summer/2-5-seconds-of-summer-i-miss"
      links: url
    });
});

// $(".up").on('click', function(){
//   var id = $(this).attr('class');
//   console.log(id)
// });

$("#chosen_song").on('click', 'button', function changeTrack() {
	// alert($(this).attr('class'));
	if ($(this).attr('class')=="up") {
		($(this).parent()).insertBefore($(this).parent().prev())
	} else if ($(this).attr('class')=="down") {
		($(this).parent()).insertAfter($(this).parent().next())
	} else {
		$(this).parent().empty();
	}
});

