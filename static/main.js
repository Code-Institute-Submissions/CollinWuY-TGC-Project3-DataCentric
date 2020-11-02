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
                // console.log("ajax reply", res); // Testing Response
                let bookData = JSON.parse(res);
                console.log(bookData);
                // console.log(bookData[0].category); // Testing Json access
                var seenNames = {};

                let list = document.getElementById('menu');
                list.innerHTML = ""

                for (let i=0; i < bookData.length; i++){
                    let newRow = `<li>${bookData[i].category}</li>`;
                    list.innerHTML += newRow

                }
             
            }
        })
    })



})