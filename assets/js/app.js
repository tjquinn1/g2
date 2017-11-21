function overlay() {
	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function Demo(config){
	this.config = config;
	this.config.development = config.development || false;
  
	this.paymentForm = $('#' + config.formID);
	this.inputs = $('input[type=text], input[type=email], input[type=tel]');
	this.button = this.paymentForm.find('.button');
  
	this.states = {
	  'show' : 'active',
	  'wait' : 'loading'
	};
	this.focusClass = "has-focus";
	this.valueClass = "has-value";
  
	this.initialize();
  }
  
  
  Demo.prototype.initialize = function(){
	var self = this;
  
	this.events();
	this.inputs.each(function(index, element){
	  self.labelHander($(element));
	});
	this.notify('error');
  };
  
  
  Demo.prototype.events = function(){
	var self = this;
  
	this.inputs.on('focus', function(){
		$(this).closest('label').addClass(self.focusClass);
		self.labelHander($(this));
	  }).on('keydown', function(){
		self.labelHander($(this));
	  }).on('blur', function(){
		$(this).closest('label').removeClass(self.focusClass);
		self.labelHander($(this));
	});
  };
  
  
  Demo.prototype.labelHander = function(element){
	var self = this;
	var input = element;
	var label = input.closest('label');
  
	window.setTimeout(function(){
	  var hasValue = (input.val().length > 0) ? true : false ;
  
	  if (hasValue) {
		label.addClass(self.valueClass);
	  } else {
		label.removeClass(self.valueClass);
	  }
	}, 10);
  };
  
  
  Demo.prototype.notify = function(status){
	var self = this;
	var notice = $('.notice-' + status );
	var delay = (this.config.development === true) ? 4000 : 2000;
  
	notice.show()
  
	window.setTimeout(function(){
	  notice.addClass('show');
	  self.button.removeClass(self.states.wait);
  
	  window.setTimeout(function(){
		notice.removeClass('show');
		window.setTimeout(function(){
		  notice.hide();
		}, 310);
	  }, delay);
	}, 10);
  };
  $(function(){
	function Response(){
	  this.view = $('body');
	  this.backButtons = $('.back');
	  this.transitionend = 'webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend';
  
	  this.initialize();
	}
  
	Response.prototype.initialize = function(){
	  this.events();
	};
  
	Response.prototype.events = function(){
	  var self = this;
  
	  // this.backButtons.on('click', function(event){
	  //   self.backHandler(event);
	  // });
	};
  
	Response.prototype.backHandler = function(event){
	  var href = (window.location.origin + $(event.target).attr('href')) || window.location.origin;
  
	  this.view.addClass('out');
  
	  window.setTimeout(function(){
		// window.location = href;
		console.log(href);
	  },1000);
	  // event.preventDefault();
	};
  
	var response = new Response();
  });
	
	$('#bought').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});
