var table = new Tabulator("#example-table", {
    ajaxURL: window.url_ajax,  // URL do endpoint do AJAX
    ajaxConfig: "GET",
    pagination: true,
    paginationMode: "remote",
    headerFilter: true,  // Ativa o filtro no cabeçalho
    paginationSize: 10,
    paginationSizeSelector: [5, 10, 25, 50],
    layout: "fitColumns",
    columns: [
        {
            title: "Nome",
            field: "nome",
            width: 150,
            headerFilter: "input",  // Filtro no cabeçalho
            headerFilterPlaceholder: "Pesquisar Nome"
        },
        {title: "Cargo", field: "cargo"},
        {title: "Data de Nascimento", field: "data_nascimento", sorter: "date", hozAlign: "center"},
    ],
    // Gerador de URL para incluir o filtro de pesquisa na requisição
    ajaxURLGenerator: function(url, config, params) {
        if (params.headerFilter_nome && params.headerFilter_nome !== "") {
            url += "&headerFilter_nome=" + encodeURIComponent(params.headerFilter_nome);
        }
        return url + "?page=" + (params.page || 1) + "&pageSize=" + (params.size || 10);
    },
    // Função de resposta
    ajaxResponse: function(url, params, response) {
        return response;  // Retorna os dados para o Tabulator
    },
});
