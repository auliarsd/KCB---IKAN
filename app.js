document.addEventListener('DOMContentLoaded', () => {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const dataDiv = document.getElementById('data');
            data.forEach(entry => {
                const p = document.createElement('p');
                p.textContent = `Koi Type: ${entry.koi_type}, Temperature: ${entry.temperature}°C, pH: ${entry.ph}, Time: ${entry.created_at}`;
                dataDiv.appendChild(p);
            });
        });

    fetch('/koi_types')
        .then(response => response.json())
        .then(types => {
            const typesDiv = document.getElementById('koi-types');
            types.forEach(type => {
                const p = document.createElement('p');
                p.textContent = `Koi Type: ${type.name}, Temp Range: ${type.optimal_temp_min}-${type.optimal_temp_max}°C, pH Range: ${type.optimal_ph_min}-${type.optimal_ph_max}`;
                typesDiv.appendChild(p);
            });
        });
});
