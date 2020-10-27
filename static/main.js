$(document).ready(function(){

    // function buildList(data){
    //     let list = document.getElementById('menu');
    //     list.innerHTML = ""
    //     for(let i = 0; i < data.length; i++){
    //         let newRow = `<li>${data[i].name}</li>`;
    //         list.innerHTML += newRow
    //     }
    // }

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
                // console.log(bookData);
                // console.log(bookData[0].book_name); // Testing Json access
                let list = document.getElementById('menu');
                list.innerHTML = ""
                for (let i=0; i < bookData.length; i++){
                    let newRow = `<li>${bookData[i].book_name}</li>`;
                    list.innerHTML += newRow
                }
            }
        })
    })

    // function searchList(value, data){
    //     let filteredData = [];

    //     for(let i = 0; i < data.length; i++){
    //         value = value.toLowerCase();
    //         let name = data[i].name.toLowerCase();

    //         if (name.includes(value)){
    //             filteredData.push(data[i])
    //         }
    //     }
    //     return filteredData
    // }
})