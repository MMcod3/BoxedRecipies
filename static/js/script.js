$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

validateMaterializeSelect();
  function validateMaterializeSelect() {
      let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
      let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
      if ($("select.validate").prop("required")) {
          $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
      }
      $(".select-wrapper input.select-dropdown").on("focusin", function () {
          $(this).parent(".select-wrapper").on("change", function () {
              if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                  $(this).children("input").css(classValid);
              }
          });
      }).on("click", function () {
          if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
              $(this).parent(".select-wrapper").children("input").css(classValid);
          } else {
              $(".select-wrapper input.select-dropdown").on("focusout", function () {
                  if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                      if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                          $(this).parent(".select-wrapper").children("input").css(classInvalid);
                      }
                  }
              });
          }
      });
    };


// Initialise modal for delete buttons
if ($('.modal')) {
    $('.modal').modal();
}

// Add button functionality for ingredients ingredients
let ingredientCount = $('.ingredient').length + 1;
$('.add-ingredient-btn').click(function() {
    let newIngredient = document.createElement('div');
    newIngredient.className = 'ingredient';
    let htmlString = 
        `<div class="input-field col s4">
            <input id="quantity" name="ingredient-qty-${ingredientCount}" type="text" class="validate" autocomplete="off" required>
            <label for="quantity">Quantity</label>
        </div>
        <div class="input-field col s8">
            <select id="ingredient" name="ingredient-name-${ingredientCount}" required>
                <option value="" disabled selected>Select Ingredient</option>`;
    for (let i = 0; i < ingredients.length; i++) {
        htmlString += `<option value="${ingredients[i]}">${ingredients[i]}</option>`
    }
    htmlString += `</select>
        </div>`;
    newIngredient.innerHTML = htmlString;
    $('.ingredients').append(newIngredient);
    ingredientCount++;




// initializing select elements

$(document).ready(function(){
    $('.ingredient-list').formSelect();
});

$(document).ready(function(){
    $('.ingredient-list').formSelect();
});


    // Add button functionality to remove last ingredient
    $('.remove-ingredient-btn').click(function() {
        $('.ingredient').last().remove();
        if (ingredientCount >= 2) {
            ingredientCount--;    
        }
    })
    
    // Add button functionality to add new step in method
    let stepCount = $('.step').length + 1;
    $('.add-step-btn').click(function() {
        let htmlString = `<li class="step">
                            <input name="step-${stepCount}" type="text" class="validate" autocomplete="off" required>
                          </li>`;
        $('#steps-list').append(htmlString);
        stepCount++;
    });
    
    // Add button functionality to remove last step in method
    $('.remove-step-btn').click(function() {
        $('.step').last().remove();
        if (stepCount >= 2) {
            stepCount--;    
            }
        }
