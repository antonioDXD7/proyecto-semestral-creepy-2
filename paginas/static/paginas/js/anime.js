const base_url = "https://api.jikan.moe/v3";


function searchAnime(event) {

    event.preventDefault();

    const form = new FormData(this);
    const query = form.get("search");

    fetch(`${base_url}/search/anime?q=${query}&page=1`)
        .then(res => res.json())
        .then(updateDom)
        .catch(err => console.warn(err.message));
}

function updateDom(data) {

    const searchResults = document.getElementById('AGREGARANIME');

    const animeByCategories = data.results
        .reduce((acc, anime) => {

            const { type } = anime;
            if (acc[type] === undefined) acc[type] = [];
            acc[type].push(anime);
            return acc;

        }, {});

    searchResults.innerHTML = Object.keys(animeByCategories).map(key => {

        const animesHTML = animeByCategories[key]
            .sort((a, b) => a.episodes - b.episodes)
            .map(anime => {
                return `
                <div class="row espaciadoadmi centrado creepybordeinicio">
                <h5 class="card-title text-center "> TIPO: ${key.toUpperCase()}</h5>

                <div class="col-sm-6 col-md-3 centrado espaciado">
                <h5 class="centrado">NOMBRE DEL ANIME: <BR> ${anime.title}</h5>
              </div>

                <div class="col-sm-6 col-md-3 centrado espaciado">
                  <h5 class="card-title text-center "><img id="img_arre" src="${anime.image_url}"></h5>
                </div>        
        
                <div class="col-sm-6 col-md-3 centrado espaciado">
                  <p class="centrado"> DESCRIPCION DEL ANIME :<BR>${anime.synopsis}</p>
                </div>
                
                <div class="col-sm-6 col-md-3 centrado espaciado">
                <h6 class="centrado">LINCK PARA VER MAS SOBRE EL ANIME: <BR> <a href="${anime.url}">MAS INFORMACION DEL ANIME</a></h6>
                </div>
              
              </div>

            
                `
            }).join("");


        return `
        <div class="container col-md-12 ">
        <div clas="row">
        ${animesHTML}
        </div>
        </div>`
    }).join("");
}

function pageLoaded() {
    const form = document.getElementById('APIANIME');
    form.addEventListener("submit", searchAnime);
}


window.addEventListener("load", pageLoaded);
