var api01 = 'https://backend-omega-seven.vercel.app/api/getjoke'
var api02 = 'https://v2.jokeapi.dev/joke/Any'
var api03 = 'https://geek-jokes.sameerkumar.website/api?format=json'

// These 4 lines are to make sure that each of the forms that are created in the functions will have their token that Django requires.  Each function has it inserted.
var csrfToken = document.getElementById("token");
console.log(csrfToken.innerHTML);
var token = document.querySelector("#token input").value;
console.log("the token test:", token)

async function jokeAPI01() {
    var response = await fetch(`${api01}`)
    var data = await response.json()
    // console.log("api01 data results:", data[0]['question'])
    var joke = data[0]
    console.log("var joke:", joke)
    var node = document.createElement('section')
    var h3v1 = document.createElement('h3')
    var h3v2 = document.createElement('h3')
    var form = document.createElement('form')
    var csrfInput = document.createElement('input')
    var questionInput = document.createElement('input')
    var punchlineInput = document.createElement('input')
    form.setAttribute('method', 'post')
    form.setAttribute('action', '/createJoke/')
    csrfInput.setAttribute('type', 'hidden')
    csrfInput.setAttribute('name', 'csrfmiddlewaretoken')
    csrfInput.setAttribute('value', token)
    questionInput.setAttribute('type', 'hidden')
    punchlineInput.setAttribute('type', 'hidden')
    questionInput.setAttribute('name', 'question')
    punchlineInput.setAttribute('name', 'punchline')
    questionInput.setAttribute('value', joke.question)
    punchlineInput.setAttribute('value', joke.punchline)
    var button = document.createElement('button')
    var submit = document.createTextNode('Save Joke to Database')
    button.appendChild(submit)
    form.appendChild(csrfInput)
    form.appendChild(questionInput)
    form.appendChild(punchlineInput)
    form.appendChild(button)
    form.setAttribute
    var question = document.createTextNode(joke.question)
    var punchline = document.createTextNode(joke.punchline)
    h3v1.appendChild(question)
    h3v2.appendChild(punchline)
    node.appendChild(h3v1)
    node.appendChild(h3v2)
    node.appendChild(form)
    document.getElementById('joke01').appendChild(node)
}

async function jokeAPI02() {
    var response = await fetch(`${api02}`)
    var data = await response.json()
    console.log("api01 data results:", data['setup'])
    var joke = data
    console.log("var joke:", joke)
    var node = document.createElement('section')
    var h3v1 = document.createElement('h3')
    var h3v2 = document.createElement('h3')
    var form = document.createElement('form')
    var csrfInput = document.createElement('input')
    var questionInput = document.createElement('input')
    var punchlineInput = document.createElement('input')
    form.setAttribute('method', 'post')
    form.setAttribute('action', '/createJoke/')
    csrfInput.setAttribute('type', 'hidden')
    csrfInput.setAttribute('name', 'csrfmiddlewaretoken')
    csrfInput.setAttribute('value', token)
    questionInput.setAttribute('type', 'hidden')
    punchlineInput.setAttribute('type', 'hidden')
    questionInput.setAttribute('name', 'question')
    punchlineInput.setAttribute('name', 'punchline')
    questionInput.setAttribute('value', joke.setup)
    punchlineInput.setAttribute('value', joke.delivery)
    var button = document.createElement('button')
    var submit = document.createTextNode('Save Joke to Database')
    button.appendChild(submit)
    form.appendChild(csrfInput)
    form.appendChild(questionInput)
    form.appendChild(punchlineInput)
    form.appendChild(button)
    form.setAttribute
    var question = document.createTextNode(joke.setup)
    var punchline = document.createTextNode(joke.delivery)
    h3v1.appendChild(question)
    h3v2.appendChild(punchline)
    node.appendChild(h3v1)
    node.appendChild(h3v2)
    node.appendChild(form)
    document.getElementById('joke02').appendChild(node)
}

async function jokeAPI03() {
    var response = await fetch(`${api03}`)
    var data = await response.json()
    console.log("api01 data results:", data['joke'])
    var joke = data
    console.log("var joke:", joke)
    var node = document.createElement('section')
    var h3v1 = document.createElement('h3')
    // var h3v2 = document.createElement('h3')
    var form = document.createElement('form')
    var csrfInput = document.createElement('input')
    var questionInput = document.createElement('input')
    var punchlineInput = document.createElement('input')
    form.setAttribute('method', 'post')
    form.setAttribute('action', '/createJoke/')
    csrfInput.setAttribute('type', 'hidden')
    csrfInput.setAttribute('name', 'csrfmiddlewaretoken')
    csrfInput.setAttribute('value', token)
    questionInput.setAttribute('type', 'hidden')
    punchlineInput.setAttribute('type', 'hidden')
    questionInput.setAttribute('name', 'question')
    punchlineInput.setAttribute('name', 'punchline')
    questionInput.setAttribute('value', joke.joke)
    punchlineInput.setAttribute('value', '')
    var button = document.createElement('button')
    var submit = document.createTextNode('Save Joke to Database')
    button.appendChild(submit)
    form.appendChild(csrfInput)
    form.appendChild(questionInput)
    form.appendChild(punchlineInput)
    form.appendChild(button)
    form.setAttribute
    var question = document.createTextNode(joke.joke)
    // var punchline = document.createTextNode(joke.punchline)
    h3v1.appendChild(question)
    // h3v2.appendChild(punchline)
    node.appendChild(h3v1)
    // node.appendChild(h3v2)
    node.appendChild(form)
    document.getElementById('joke03').appendChild(node)
}