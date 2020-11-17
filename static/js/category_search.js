$(document).ready(function(){
    // Category Search Ajax Call to MongoDB
    $('#bookCategory').on('change', function(e){
        let bookCategory = $("#bookCategory").val();
        $.ajax({
            method: "POST",
            url: "/catsearch",
            data: {text: bookCategory},
            success: function(res){
                let bookCategory = JSON.parse(res);
                $("#bookAuthor").val(bookCategory[0].publisher);      
            }
        })
    })
})
