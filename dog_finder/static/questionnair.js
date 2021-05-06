$(document).ready(function(){
    // Hide all questions
    $('.questions').hide();

    // show first question
    $('#q1').show();

    //go to next q when pressed
    $('#q1 #submit').click(function(){
        $('.questions').hide();
        $('#q2').fadeIn(300);
        return false
    });

    $('#q2 #submit').click(function(){
        $('.questions').hide();
        $('#q3').fadeIn(300);
        return false
    });

    $('#q3 #submit').click(function(){
        $('.questions').hide();
        $('#q4').fadeIn(300);
        return false
    });


});

// Process the Value of the Answer
function process(q){
    if (q=="q1"){
        var submitted = $('input[name=q1]:checked').val();
        
    }
}