$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});

    // Initialise modal for delete buttons
    if ($('.modal')) {
        $('.modal').modal();
}
    
    // Initialise form select options
    let selects = document.querySelectorAll('select');
    let selectInstances = M.FormSelect.init(selects);

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

    // Add ingredients button functionality
    let ingredients = [];
    if (document.URL.includes('add_recipe') || document.URL.includes('edit_recipe')) {
        for (let i = 1; i < selects[1].length; i++) {
            ingredients.push(selects[1][i].innerHTML)
        }
    }
    
    let ingredientNumber = $('.ingredient').length + 1;
    $('.add-ingredient-btn').click(function() {
        let newIngredient = document.createElement('div');
        newIngredient.className = 'ingredient';
        let htmlString = 
            `<div class="input-field col s4">
                <input id="quantity" name="ingredient-qty-${ingredientNumber}" type="text" class="validate" autocomplete="off" required>
                <label for="quantity">Quantity</label>
            </div>
            <div class="input-field col s8">
                <select id="ingredient" name="ingredient-name-${ingredientNumber}" required>
                    <option value="" disabled selected>Select Ingredient</option>`;
        for (let i = 0; i < ingredients.length; i++) {
            htmlString += `<option value="${ingredients[i]}">${ingredients[i]}</option>`
        }
        htmlString += `</select>
            </div>`;
        newIngredient.innerHTML = htmlString;
        $('.ingredients').append(newIngredient);
        ingredientNumber++;
        
        // re-initialise selects on the page
        selects = document.querySelectorAll('select');
        selectInstances = M.FormSelect.init(selects);
    });

    // Remove ingredient button functionality 
    $('.remove-ingredient-btn').click(function() {
        $('.ingredient').last().remove();
        if (ingredientNumber >= 2) {
            ingredientNumber--;    
        }
    });

    // Add method button functionality
    let methodNumber = $('.method').length + 1;
    $('.add-method-btn').click(function() {
        let htmlString = `<li class="method">
                            <input name="method-${methodNumber}" type="text" class="validate" autocomplete="off" required>
                          </li>`;
        $('#method-list').append(htmlString);
        methodNumber++;
    });
    
    // Remove method button functionality
    $('.remove-method-btn').click(function() {
        $('.method').last().remove();
        if (methodNumber >= 2) {
            methodNumber--;    
        }
    })

});

   

    

    



