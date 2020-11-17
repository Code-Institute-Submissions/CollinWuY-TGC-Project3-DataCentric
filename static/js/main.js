$(document).ready(function(){
    // Live Search Ajax Call to MongoDB
    $('#search').on('input', function(e){
        let searchValue = $('#search').val();
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
})