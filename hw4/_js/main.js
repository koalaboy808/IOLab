$(document).ready(
    $("#new-item").on('click', function() {
        var user_input = $("#todo-item-input").val();
        // alert(user_input);
        console.log(user_input);

        $("#list_todo").prepend( "<li class='todo_style'> <button> Move me! </button>" + user_input + "</li>");
        $("#todo-item-input").val('');
        // $("li").onclick = function() {this.parentNode.removeChild(this);}
    })
);

$("#list_todo").on('click', "button", function() {
        // $(this).parent().remove();
        // console.log($(this).parent())
        var completedItem = $(this).parent()

        completedItem.removeClass("todo_style");
        completedItem.addClass("completed_style");

        $(this).html("Add To To-Do");


        $("#list_completed").prepend(completedItem);
});

$("#list_completed").on('click', "button", function() {
        // $(this).parent().remove();
        // console.log($(this).parent())
        var undo = $(this).parent()

        undo.removeClass("completed_style");
        undo.addClass("todo_style");

        $(this).html("Move Me!");


        $("#list_todo").prepend(undo);
});