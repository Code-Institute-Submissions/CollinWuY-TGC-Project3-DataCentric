$(document).ready(function(){
    // let bookList = [{{books}}];
    // [
    // {"name": "Dungeon and Dragons"},
    // {"name": "Call of Cthulhu"},
    // {"name": "Blades in the Dark"},
    // {"name": "Warhammer Fantasy"},
    // {"name": "Deadlands"},
    // {"name": "Cyberpunk"},
    // {"name": "Paranoia"},
    // {"name": "Shadow of the Demon Lord"},
    // {"name": "Legend of the Five Rings"},
    // {"name": "Star Wars Roleplaying"},
    // {"name": "Starfinder"},
    // {"name": "Fate Core"},
    // {"name": "Star Trek Adventures"},
    // {"name": "Bubblegumshoe"},
    // {"name": "Feng Shui"},
    // {"name": "Masks"},
    // {"name": "Fiasco"},
    // {"name": "Numenera"},
    // ]   

    // buildList(books)

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
                console.log("ajax reply", res);
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