function callApi(){

    fetch("http://localhost:5000/user?user_id=6acba1a68ccbbad556d84feb")
    .then(res => res.json())
    .then(data => {
        const firstName = data["first_name"];
        const lastName = data["last_name"];
        const city = data["city"];
        const age = data["age"];
        const userDiv = document.querySelector(".user-info");
        //get city and age for your user
        // place it inside h1 tag and show it on your webpage
        userDiv.innerHTML = `
        <h1> First Name: ${firstName} </h1>
        <h1> Last Name: ${lastName} </h1>
        <h1> City: ${city} </h1>
        <h1> Age: ${age} </h1>
        ` // innterHTML adds literal html code as a text inside that div//the `` is like an f string and the dollar sign variable name is how u use variables in text
    })
}
callApi()
 //search up cors security. its like a system that doesnt let two seperate servers talk for security i think.
//its cus my backend is localhost:5000 but my frontend is localhost:5500
//type this to access it and view 127.0.0.1:5500/connect_to_flask.html