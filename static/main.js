$(document).ready(function(){

    // Live Search Ajax Call to MongoDB
    $('#search').on('input', function(e){
        let searchValue = $('#search').val();
        console.log("Value:", searchValue);
        $.ajax({
            method: "POST",
            url: "/livesearch",
            data: {text: searchValue},
            success: function(res){
                let bookData = JSON.parse(res);
                var seenNames = {};
                let list = document.getElementById('menu');
                list.innerHTML = ""
                for (let i=0; i < bookData.length; i++){
                    let newRow = `<a href="/info/${bookData[i]._id.$oid}")}}"><li>${bookData[i].name}</li></a>`;
                    list.innerHTML += newRow
                } 
            }
        })
    })
    
    $("#navbarCustom .nav-item").click(function(){
        $('#navbarCustom .nav-item').removeClass('active');
        $(this).addClass('active');
    })


    $('.ratings').click(function(){
        ratingScore();
    })

    function ratingScore(){
        let rating = document.getElementsByName("rate");
        if(rating[4].checked){
            console.log(rating[4].value);
        } else if(rating[3].checked){
            console.log(rating[3].value);
        }else if(rating[2].checked){
            console.log(rating[2].value);
        }else if(rating[1].checked){
            console.log(rating[1].value);
        }else{
            console.log(rating[0].value);
        }
    }

})