console.log("JS cargado");
document.addEventListener("DOMContentLoaded", function () {

    const servicioSelect = document.getElementById("servicio");
    const profesionalSelect = document.getElementById("profesional");

    if (!servicioSelect || !profesionalSelect) {
        console.log("No se encontraron los selects");
        return;
    }

    profesionalSelect.disabled = true;

    servicioSelect.addEventListener("change", function () {

        const servicioId = this.value;

        if (!servicioId) {
            profesionalSelect.innerHTML = '<option value="">Seleccione un profesional</option>';
            profesionalSelect.disabled = true;
            return;
        }

        profesionalSelect.innerHTML = '<option value="">Cargando...</option>';
        profesionalSelect.disabled = true;

        fetch(`/obtener-profesionales/?servicio_id=${servicioId}`)
            .then(response => response.json())
            .then(data => {

                profesionalSelect.innerHTML = '<option value="">Seleccione un profesional</option>';

                if (data.length === 0) {
                    profesionalSelect.innerHTML = '<option value="">No hay profesionales disponibles</option>';
                } else {
                    data.forEach(function (profesional) {
                        const option = document.createElement("option");
                        option.value = profesional.id;
                        option.textContent = profesional.nombre;
                        profesionalSelect.appendChild(option);
                    });
                }

                profesionalSelect.disabled = false;
            })
            .catch(error => {
                console.error("Error:", error);
            });

    });

});