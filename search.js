<!DOCTYPE html>
<html lang="en">
<head>
	<!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>
      <link type="text/css" rel="stylesheet" href="cdn.materialdesignicons.com/2.8.94/css/materialdesignicons.min.css">
      <link rel="stylesheet" href="https://cdn.rawgit.com/Dogfalo/materialize/v1-dev/extras/noUiSlider/nouislider.css">
      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <!--Custom Style-->
      <style>
		@-webkit-keyframes fade-in{
			from{
				opacity:1;
    			top:-400px;
    			text-shadow: none;
			}
			to{
				opacity: 0;
   				 color:transparent;
    			 top:-1000px;
    			 text-shadow: #111 0 0 150px;
			}
		}
		.text-animated{
			display:inline;
			position:relative;
			top:0px;
			-webkit-animation:fade-in 5.5s;

		}
		@-webkit-keyframes fade-out{
			from{
   				 opacity:0;
    			top:-400px;
			}
			to{
   				 opacity:1;
    			 top:0px;
			}
		}
		.label-animated{
			display:inline;
			position:relative;
			-webkit-animation:fade-out 5.5s;
		}
		@-webkit-keyframes fade-out-alt{
			from{
   				 opacity:0;
    			 top:700px;
			}
			to{
   				 opacity:1;
    			 top:0px;
			}
		}
		.label-animated-alt{
			position:relative;
			-webkit-animation:fade-out-alt 3.5s;
		}
			.section-search .input-field label {
     		color: #FFF !important;

   		}
   		/* label focus color */
		.section-search .input-field input[type=text]:focus + label {
     		color: #FFAB40 !important;
     		box-shadow: 0 1px 0 0 #000 !important;
   		}
   		/* label underline focus color */
		.section-search .input-field input[type=text]:focus {
    		border-bottom: 1px solid #FFAB40 !important;
   		}
 		/* icon prefix focus color */
		.section-search .input-field .prefix.active {
			color: #FFAB40 !important;
		   }
		.noUi-connect {
  			background: #FFAB40;
		   }
		.noUi-horizontal .noUi-handle,
		.noUi-vertical .noUi-handle {
  			background: #FFAB40;
		   }
		.noUi-target.noUi-horizontal .noUi-tooltip {
		    background-color: #FFAB40;
		   }
		[type="checkbox"] + span:not(.lever):before,
		[type="checkbox"]:not(.filled-in) + span:not(.lever):after {
  			content: '';
  			position: absolute;
  			top: 0;
  			left: 0;
  			width: 18px;
  			height: 18px;
  			z-index: 0;
  			border: 2px solid #ffab40; 
  			border-radius: 1px;
  			margin-top: 3px;
  			-webkit-transition: .2s;
  			transition: .2s;
			}
		[type="checkbox"]:checked + span:not(.lever):before {
  			top: -4px;
  			left: -5px;
  			width: 12px;
  			height: 22px;
  			border-top: 2px solid transparent;
  			border-left: 2px solid transparent;
  			border-right: 2px solid #fff;
  			border-bottom: 2px solid #fff;
  			-webkit-transform: rotate(40deg);
          	transform: rotate(40deg);
  			-webkit-backface-visibility: hidden;
         	 backface-visibility: hidden;
  			-webkit-transform-origin: 100% 100%;
         	 transform-origin: 100% 100%;
			}
   </style>
	<meta charset="UTF-8">
	<title>User Page</title>
</head>
<body id="user" class="scrollspy light-grey lighten-1">
	<div id="nav_bar" class="navbar-fixed" style="transition: 0.5s;">
		<nav class="light-blue label-animated">
				<div class="nav-wrapper">
					<a href="#" data-target="mobile-nav" class="sidenav-trigger left-align show-on-large">
						<i class="material-icons">menu</i></a>
						<a href="#" class="brand-logo orange-text center"><i class="material-icons white-text">place</i>XYou</a>
						<ul class="right">
							<li> <a class="tooltipped" data-position="bottom" data-tooltip="Click me to search tours" onclick="animate_label()"><i class="material-icons white-text">search</i>
							</a></li>
							<li><a href="" class="tooltipped" data-position="bottom" data-tooltip="I am your shopping cart"><i class="material-icons white-text">shopping_cart</i></a></li>
						</ul>
			</div>
		</nav>
	</div>
	<ul class="sidenav" id="mobile-nav">
		<li><div class="user-view">
      		<div class="background">
        		<img src="background2.png">
      		</div>
      	<a href="#user"><img class="circle" src="background1.jpg"></a>
      	<a href="#name"><span class="white-text name">Ad Min</span></a>
      	<a href="#email"><span class="white-text email">admin@gmail.com</span></a>
    	</div></li>
		<li>
			<a class="light" href="#home">My Profile</a>
		</li>
		<li>
			<a class="light" href="#contacts">Logout</a>
		</li>
	</ul>
	<section class="section light-blue lighten-1 section-icons center label-animated">
		<div class="container">
			<div class="row">
				<h4 class="grey-text text-darken-3">Fast Tips</h4>
				<div class="col s12 m4">
					<div class="card-panel light grey-text text-darken-3 orange lighten-1">
						<i class="material-icons large light-blue-text">menu</i>
						<h4>Menu Button</h4>
						<p>Click on this button to show your profile.</p>
					</div>
				</div>
				<div class="col s12 m4">
					<div class="card-panel light grey-text text-darken-3 orange lighten-1">
						<i class="material-icons large light-blue-text">search</i>
						<h4>Search Button</h4>
						<p>Click on this button to show search panel.</p>
					</div>
				</div>
				<div class="col s12 m4">
					<div class="card-panel light grey-text text-darken-3 orange lighten-1">
						<i class="material-icons large light-blue-text">shopping_cart</i>
						<h4>My Cart</h4>
						<p>Clicking on this you'll be redirected to your cart page.</p>
					</div>
				</div>
			</div>
		</div>
	</section>
	<section  class="section section-search center scrollspy" >
		<div id="search_label" style="opacity:0; ">
			<div class="row card-panel light-blue lighten-1">
				<div class="col s12">
					<h4 class="white-text">Search tours here!</h4>
					<form>
					<div class="input-field col s12 m10">
						<i class="material-icons white-text prefix">search</i>
						<input type="text" class="validate autocomplete white-text" id="autocomplete-input">
						<label for="autocomplete-input" class="white-text">Type here country name</label>
					</div>
					<div class="input-field col s12 m2">
						<button class="grey-text text-darken-3 waves-effect waves-light orange lighten-1 btn-large" type="submit" name="action">Go!
						</button>
					</div>
					</form>
				</div>
			</div>
		</div>
		<div class="container" id="search_label_1" style="opacity:0;">
			<div class="row ">
  			<div class="col s12 m10">
  				<div class="card-panel light light-blue" style="height: 110px;">
   					<h5 class="white-text" style="text-align: left;">Prices Range</h5>
   					<div class="col s10 offset-s2">
   						<div id="test-slider" ></div>
   					</div>
    			</div>
  			</div>
  			<div class="col s12 m2">
  				<div class="card-panel light light-blue" style="height: 110px;">
  				<form action="#">
    				<h6 style="margin-top:30px;">
      					<label>
        					<input type="checkbox"  class="white"/>
        					<span  class="white-text">Apply Filter</span>
      					</label>
   					</h6>
   				</form>
   			</div>
  			</div>
  			</div>
		</div>
	</section>
	<div class="container">
	<div class="row white-text">
		<div class="col s12 center-align">
			<h2 class="black-text text-animated" style="opacity: 0; top: -1980px">Welcome!</h4>
		</div>
	</div>
		<div class="row white-text">
		<div class="col s12 center-align">
			<h4 class="black-text text-animated" style="opacity: 0; top: -1980px">Have a nice day!</h4>
		</div>
	</div>
	</div>
	  <script type="text/javascript" src="js/materialize.min.js"></script>
	  <script src="https://cdn.rawgit.com/Dogfalo/materialize/v1-dev/extras/noUiSlider/nouislider.min.js"></script>
	  <script src="https://unpkg.com/wnumb@1.1.0"></script>
	 <script>
	  const sideNav = document.querySelector('.sidenav');
	  M.Sidenav.init(sideNav, {});
	  document.addEventListener('DOMContentLoaded', function() {
    	var elems = document.querySelectorAll('.tooltipped');
    	var instances = M.Tooltip.init(elems, {});
  		});
	  function animate_label(){
	  	document.getElementById('search_label').className="container label-animated-alt";
	  	document.getElementById('search_label').style.opacity="1";
	  	document.getElementById('search_label').style.top="0";
	  	document.getElementById('search_label_1').className=" container label-animated-alt";
	  	document.getElementById('search_label_1').style.opacity="1";
	  	document.getElementById('search_label_1').style.top="0";
	  }
	  const autocmpl = document.querySelector('.autocomplete');
      M.Autocomplete.init(autocmpl,{
      	data: {
      			"Taiwan": null,
      			"Montenegro": null,
      			"Hawaii": null,
      		}
      });
       var slider = document.getElementById('test-slider');
  		noUiSlider.create(slider, {
   		start: [250, 8000],
   		connect: true,
   		step: 10,
   		orientation: 'horizontal', // 'horizontal' or 'vertical'
   		range: {
     		'min': 200,
     		'max': 10000
   		},
   		format: wNumb({
     		decimals: 0
   		})
  		});	  
	</script>
</body>
</html>