Title: Garden of Games: Seeded
Summary: See the past, present, and future of streaming.
Slug: gog/seeded
Status: Hidden
HideTitle: True


## <center><a href='/gog'>Entrance</a> | <a href='/gog/growing'>Growing</a> | <a href='/gog/harvested'>Harvested</a> | <a href='/gog/composted'>Composted</a> | <a href='/gog/seeded'><b>Seeded</b></a></center>

---

<div id="search-bar"></div><br>
<div id="game-list">Loading...</div>

<script src='/js/seeded.js'></script>
<script>
function dynamicSort(property) {
    var sortOrder = 1;
    if(property[0] === "-") {
        sortOrder = -1;
        property = property.substr(1);
    }
    return function (a,b) {
        var result = (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
        return result * sortOrder;
    }
}

function dynamicSortMultiple() {
    var props = arguments;
    return function (obj1, obj2) {
        var i = 0, result = 0, numberOfProperties = props.length;
        while(result === 0 && i < numberOfProperties) {
            result = dynamicSort(props[i])(obj1, obj2);
            i++;
        }
        return result;
    }
}

function createGameList() {
var searchTerm = document.getElementById('search-box').value.toLowerCase();
var filtered = jsonArray.filter(jsonObject => 
jsonObject.name.toLowerCase().includes(searchTerm));

if (document.getElementById('platform-dropdown').value) {
    filtered = filtered.filter(function(jsonObject)  { return jsonObject.platform == document.getElementById('platform-dropdown').value; });
};

var sort_by = document.getElementById('sort-dropdown').value;
if (sort_by == 1) {
    filtered.sort(dynamicSortMultiple("name", "-votes"));
} else if (sort_by == 2) {
    filtered.sort(dynamicSortMultiple("-name", "-votes"));
} else if (sort_by == 4) {
    filtered.sort(dynamicSortMultiple("votes", "name"));
} else {
    filtered.sort(dynamicSortMultiple("-votes", "name"));
};
    

var html_to_write = '';
var vote_letter = "s";
for (var i = 0; i < filtered.length; i += 2) {
    if (filtered[i].votes == 1) { vote_letter = ""; } else { vote_letter = "s"; };
    html_to_write = html_to_write.concat(`<div class="row">
  <div class="col-sm-6">
    <div class="card text-white" style="background-color: rgba(33,37,41,0.95);">
        <div class="card-body">
            <div class="row align-items-center">
                <div class="col-auto align-self-center">
                    <img class="rounded align-self-center" src="/images/games/${filtered[i].id}.png" style="width: 96px; height: 96px;">
                </div>
                <div class="col justify-content-center" align="center">
                    <b>${filtered[i].name}</b><br>
                </div>
            </div><br>
            <div class="row align-items-center">
                <div class="col justify-content-center" align="center">
                    #${filtered[i].id} | ${filtered[i].platform} | ${filtered[i].votes} Vote${vote_letter}
                </div>
            </div>
        </div>
    </div>
    </div>`);
    if (i + 1 < filtered.length) {
        if (filtered[i+1].votes == 1) { vote_letter = ""; } else { vote_letter = "s"; };
        html_to_write = html_to_write.concat(`<div class="col-sm-6">
    <div class="card text-white" style="background-color: rgba(33,37,41,0.95);">
        <div class="card-body">
            <div class="row align-items-center">
                <div class="col-auto align-self-center">
                    <img class="rounded align-self-center" src="/images/games/${filtered[i+1].id}.png" style="width: 96px; height: 96px;">
                </div>
                <div class="col justify-content-center" align="center">
                    <b>${filtered[i+1].name}</b><br>
                </div>
            </div><br>
            <div class="row align-items-center">
                <div class="col justify-content-center" align="center">
                    #${filtered[i+1].id} | ${filtered[i+1].platform} | ${filtered[i+1].votes} Vote${vote_letter}
                </div>
            </div>
        </div>
    </div>
    </div>`);
    };
    html_to_write = html_to_write.concat(`</div><br>`);
};
var node = document.getElementById('game-list');
node.innerHTML = html_to_write;
};

const platforms = Array.from(new Set(jsonArray.map((item) => item.platform)));
platforms.sort();

var html_to_write = `<form>
  <div class="form-row">
    <div class="col">
      <input id="search-box" type="text" class="form-control" placeholder="Search" oninput="createGameList()">
    </div>
    <div class="col-md-auto">
      <select id="platform-dropdown" class="custom-select" onchange="createGameList()">
      <option value="">Platform</option>`;

for (var p of platforms) {
html_to_write = html_to_write.concat(`<option value="${p}">${p}</option>`);
};

html_to_write = html_to_write.concat(`</select>
    </div>
    <div class="col-md-auto">
      <select id="sort-dropdown" class="custom-select" onchange="createGameList()">
      <option value="">Sort</option>
      <option value="1">Name (A-Z)</option>
      <option value="2">Name (Z-A)</option>
      <option value="3">Votes (highest first)</option>
      <option value="4">Votes (lowest first)</option>
    </select>
    </div>
  </div>
</form>`);

var node = document.getElementById('search-bar');
node.innerHTML = html_to_write;

createGameList();
</script>
