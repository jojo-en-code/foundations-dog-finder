$(document).ready(function(){
    // Hide all questions
    $('.questions').hide();

    let score = 0

    // show first question
    $('#q1').show();

    //go to next q when pressed
    $('#q1 #submit').click(function(){
        const isChecked  = checkCheckBoxes()
        if(!isChecked) return false
        
        addScore1()
        console.log(score)

        $('.questions').hide();
        $('#q2').fadeIn(300);
        return false
    });

    $('#q2 #submit').click(function(){
        const isChecked  = checkCheckBoxes()
        if(!isChecked) return false
        
        addScore2()
        console.log(score)

        $('.questions').hide();
        $('#q3').fadeIn(300);
        return false
    });

    $('#q3 #submit').click(function(){
        const isChecked  = checkCheckBoxes()
        if(!isChecked) return false
        
        addScore3()
        console.log(score)

        $('.questions').hide();
        $('#q4').fadeIn(300);
        return false
    });
    $('#q4 #submit').click(function(){
        const isChecked  = checkCheckBoxes()
        if(!isChecked) return false
        
        addScore4()
        console.log(score)
        $('.questions').hide();
        

        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function()
        {
          if(this.readyState == 4 && this.status == 200) {
            let data = JSON.parse(this.responseText)
            document.getElementById('score').innerHTML = data.score;
            document.getElementById('score_breeds').innerHTML = data.result;
          } else {
            document.getElementById('score').innerHTML = "Something went wrong.";
          }
        }
        xhr.open("POST", "/questionnair", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            score:score
        })); 


        return false
    });
    function checkCheckBoxes() {
        if(!$('#radio_yes').is(':checked') && !$('#radio_no').is(':checked')) {
            return false
        }
        return true
    }

    function addScore1(){
        if($('#q1 #radio_yes').is(':checked')){
            score += parseInt($('#q1 #radio_yes').val()) 
        }
        else{
            score += parseInt($('#q1 #radio_no').val())
        }
    }
    function addScore2(){
        if($('#q2 #radio_yes').is(':checked')){
            score += parseInt($('#q2 #radio_yes').val()) 
        }
        else{
            score += parseInt($('#q2 #radio_no').val())
        }
    }
    function addScore3(){
        if($('#q3 #radio_yes').is(':checked')){
            score += parseInt($('#q3 #radio_yes').val()) 
        }
        else{
            score += parseInt($('#q3 #radio_no').val())
        }
    }
    function addScore4(){

        if($('#q4 #radio_yes').is(':checked')){
            score += parseInt($('#q4 #radio_yes').val()) 
        }
        else{
            score += parseInt($('#q4 #radio_no').val())
        }
        
    }
    
   

});
