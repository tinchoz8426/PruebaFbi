fetch("fbi.json")
  .then((data) => {
    return data.json();
  method: 'POST'
  })
  .then((users) => {
    // console.log(users);
    let output = "";
    console.log(users["items"].length);
    for (let i = 0; i < users["items"].length; i++) {
      console.log(users["items"]);
      output += `<div class="card" style="width: 18rem;">
      <img src="${users["items"][i]["images"][0]["original"]}" class="card-img-top" alt="Error desde servidor">
      <div class="card-body">
        <h5 class="card-title">${users["items"][i]["title"]}</h5>
        <p class="card-text">${users["items"][i]["description"]}</p>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"><b>Recompensa:</b> ${users["items"][i]["reward_text"]}</li>
      </ul>
      <div class="card-body">
        <a target="_blank" href="${users["items"][i]["url"]}" class="card-link">FICHA COMPLETA</a>
      </div>
    </div>`;
    }

    document.getElementById("users").innerHTML = output;
  });
