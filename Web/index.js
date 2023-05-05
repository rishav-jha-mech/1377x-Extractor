const table = document.getElementById("appendDataToTableBody")
const input = document.getElementById("searchInput")
const searchBtn = document.getElementById("searchBtn")
const loading = document.getElementById("loading")
const results = document.getElementById("results")

function init () {
    for (let index = 0; index < movies.length; index++) {
        const element = movies[index];
        const tr = document.createElement("tr");
        tr.innerHTML = `
        <th scope="row">${index + 1}</th>
        <td>
        <a href="http://1377x.to${element.link}" target="_blank" rel="noopener noreferrer">${element.title}</a></td>
        <td>${element.seeds}</td>
        <td>${element.leeches}</td>
        <td>${element.size}</td>
        <td>${element.date}</td>
        <td>${element.uploader}</td>
    `
        table.appendChild(tr)
        results.innerHTML = `${movies.length} Movies present`
    }
    loading.innerHTML = ``
    table.classList.remove("d-none")
}

init();

function search () {
    const value = input.value.toLowerCase()
    console.log(value);
    if (value === '') {
        init();
        return;
    }
    const filteredMovies = movies.filter((movie) => {
        return movie.title.toLowerCase().includes(value)
    })
    results.innerHTML = `${filteredMovies.length} Results found`
    table.innerHTML = ""
    for (let index = 0; index < filteredMovies.length; index++) {
        const element = filteredMovies[index];
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <th scope="row">${index + 1}</th>
            <td>
            <a href="http://1377x.to${element.link}" target="_blank" rel="noopener noreferrer">${element.title}</a></td>
            <td>${element.seeds}</td>
            <td>${element.leeches}</td>
            <td>${element.size}</td>
            <td>${element.date}</td>
            <td>${element.uploader}</td>
        `
        table.appendChild(tr)
    }
}