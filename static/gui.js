
// function showhide()
// {  
//     var div = document.getElementById("newpost");  
//     if (div.style.display !== "none") 
//      {  
//         div.style.display = "block";  
//      }  
//     else
//     {  
//         div.style.display = "none";  
//     }
      
//     }  


// function showDiv() {
//     document.getElementById('welcomeDiv').style.display = "block";
//  }

function pushMe(ticker) {
    var img = document.createElement("img")
    img.src =  ticker
    var card = document.getElementById("hide");
    while(card.firstChild) {
      card.removeChild(card.lastChild);
    }
    card.appendChild(img);
    
    var element = document.getElementById("here");
  element.appendChild(card);
  }