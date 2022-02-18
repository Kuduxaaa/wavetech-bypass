(function() {
    var letters = 'abgdevzTiklmnopJrstufqRySCcZwWxjh';
    var addend = 4304;
    var inputs = [];
    var inputTexts = document.querySelectorAll('input[data-geokb]');
    var inputAreas = document.querySelectorAll('textarea[data-geokb]');
    for (var i = 0; i < inputTexts.length; i++) {
      inputs.push(inputTexts[i]);
    }
    for (var i = 0; i < inputAreas.length; i++) {
      inputs.push(inputAreas[i]);
    }
  
    for (var i = 0; i < inputs.length; i++) {
      var elem = inputs[i];
      var parent = elem.parentElement;

      elem.addEventListener('keypress', function(e) {
        var isEnabled = this.getAttribute('data-geokb') === 'true';
        var keyCode = e.keyCode || e.which;

        if (isEnabled) {
          var charIndex = letters.indexOf(String.fromCharCode(keyCode));
          if (charIndex > -1) {
            var newIndex = this.selectionStart + 1;
            var leftText = this.value.substring(0, this.selectionStart);
            var rightText = this.value.substring(this.selectionEnd);
            this.value = leftText + String.fromCharCode(charIndex + addend) + rightText;
            this.setSelectionRange(newIndex, newIndex);
            e.preventDefault();
          }
        }
      });
    }
  })();