jQuery(document).ready(function() {
    $("input[type=submit]").prop('disabled', true);
    eventBindings();
});

function eventBindings() {
    $("#nav-multiple-tab").click(function() {
        changeSelection("multiple")
    });

    $("#nav-fill-in-tab").click(function() {
        changeSelection("fillin")
    });

    $("#nav-written-tab").click(function() {
        changeSelection("written")
    });

    $("#validate").click(function() {
        validateQuestion()
    });

    $('#plus-btn').click(function() {
        var row = parseInt($('#optionsQty').val()) + 1;
        $('#answerContainer').append(buildMultipleChoiseOption(row));
        $('#optionsQty').val(row);
    });

    $('#minus-btn').click(function() {
        if (parseInt($('#optionsQty').val()) > 2) {
            $('#optionsQty').val(parseInt($('#optionsQty').val()) - 1);
            $('#answerContainer tr:last').remove();
        }
    });
}

function buildMultipleChoiseOption(row) {
    html = '<tr><td class="option-td option-text" align="center" valign="middle"><div class="form-group shadow-textarea">';
    html += '<textarea class="form-control option" id="option' + row + 'Text" name="option' + row + 'Text" placeholder="Option ' + row + '"></textarea>';
    html += '</div></td><td class="option-td" align="center" valign="middle"><label class="switch ">';
    html += '<input type="checkbox" id="option' + row + '" name="option' + row + '" class="success">';
    html += '<span class="slider"></span></label></td></tr>';
    return html;
}

function changeSelection(val) {
    $("#selectedType").val(val);
}

function validateQuestion() {
	$("input[type=submit]").prop('disabled', false);
    return true;
}