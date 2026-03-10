const API = "http://localhost:8000"

async function reviewCode() {

const code = document.getElementById("codeInput").value

const res = await fetch(`${API}/review`, {
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({code})
})

const data = await res.json()

document.getElementById("output").innerText = data.review
}

async function generateDocs(){

const code = document.getElementById("codeInput").value

const res = await fetch(`${API}/document`,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({code})
})

const data = await res.json()

document.getElementById("output").innerText = data.documentation

}
