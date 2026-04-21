const productos = [
    {
        codigo: 1,
        nombre: "Cuaderno",
        valoru: 5000,
        existencias: 100
    },
    {
        codigo: 2,
        nombre: "Esfero",
        valoru: 2500,
        existencias: 250
    },
    {
        codigo: 3,
        nombre: "Lapiz",
        valoru: 1500,
        existencias: 300
    }
];

const tabla = document.querySelector("#tablaProductos tbody");

productos.forEach(producto => {

    let valorTotal = producto.valoru * producto.existencias;

    let estado = "";
    let claseEstado = "";

    if (producto.existencias < 50) {
        estado = "Bajo";
        claseEstado = "bajo";
    } else if (producto.existencias >= 50 && producto.existencias <= 100) {
        estado = "Medio";
        claseEstado = "medio";
    } else {
        estado = "Alto";
        claseEstado = "alto";
    }

    let fila = `
        <tr>
            <td>${producto.codigo}</td>
            <td>${producto.nombre}</td>
            <td>${producto.valoru}</td>
            <td>${producto.existencias}</td>
            <td>${valorTotal}</td>
            <td class="${claseEstado}">${estado}</td>
        </tr>
    `;

    tabla.innerHTML += fila;
});