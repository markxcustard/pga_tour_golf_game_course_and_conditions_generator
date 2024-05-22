document.getElementById('generateButton').addEventListener('click', generateCourse);
document.getElementById('showLast25Button').addEventListener('click', showLast25Results);

function generateCourse() {
    fetch('/generate_course')
        .then(response => response.json())
        .then(data => {
            displayCourse(data);
        })
        .catch(error => console.error('Error:', error));
}

function showLast25Results() {
    fetch('/results')
        .then(response => response.json())
        .then(data => {
            displayResults(data);
        })
        .catch(error => console.error('Error:', error));
}

function displayCourse(course) {
    const courseGrid = document.getElementById('courseGrid');
    courseGrid.innerHTML = `
        <p><span class="bold-text">Course generated on:</span> ${course.timestamp}</p>
        <p><span class="bold-text">Course:</span> ${course.course}</p>
        <p><span class="bold-text">Crowd:</span> ${course.crowd}</p>
        <p><span class="bold-text">Time of Day:</span> ${course.time_of_day}</p>
        <p><span class="bold-text">Tee:</span> ${course.tee}</p>
        <p><span class="bold-text">Pin:</span> ${course.pin}</p>
        <p><span class="bold-text">Wind Direction:</span> ${course.wind_direction}</p>
        <p><span class="bold-text">Wind Speed:</span> ${course.wind_speed}</p>
        <p><span class="bold-text">Green Firmness:</span> ${course.green_firmness}</p>
        <p><span class="bold-text">Green Speed:</span> ${course.green_speed}</p>
        <p><span class="bold-text">Fringe Firmness:</span> ${course.fringe_firmness}</p>
        <p><span class="bold-text">Fringe Speed:</span> ${course.fringe_speed}</p>
        <p><span class="bold-text">Fairway Firmness:</span> ${course.fairway_firmness}</p>
        <p><span class="bold-text">Fairway Speed:</span> ${course.fairway_speed}</p>
        <p><span class="bold-text">First Cut Firmness:</span> ${course.first_cut_firmness}</p>
        <p><span class="bold-text">First Cut Length:</span> ${course.first_cut_length}</p>
        <p><span class="bold-text">Second Cut Firmness:</span> ${course.second_cut_firmness}</p>
        <p><span class="bold-text">Second Cut Length:</span> ${course.second_cut_length}</p>
    `;
}

function displayResults(results) {
    const courseGrid = document.getElementById('courseGrid');
    courseGrid.innerHTML = '';

    results.forEach(result => {
        const item = document.createElement('div');
        item.classList.add('accordion-item');

        const header = document.createElement('div');
        header.classList.add('accordion-header', 'tooltip');
        header.textContent = `Course generated on: ${result.timestamp}`;

        const tooltipText = document.createElement('span');
        tooltipText.classList.add('tooltiptext');
        tooltipText.textContent = "Click to expand!";

        header.appendChild(tooltipText);

        const content = document.createElement('div');
        content.classList.add('accordion-content');
        content.innerHTML = `
            <p><span class="bold-text">Course:</span> ${result.course}</p>
            <p><span class="bold-text">Crowd:</span> ${result.crowd}</p>
            <p><span class="bold-text">Time of Day:</span> ${result.time_of_day}</p>
            <p><span class="bold-text">Tee:</span> ${result.tee}</p>
            <p><span class="bold-text">Pin:</span> ${result.pin}</p>
            <p><span class="bold-text">Wind Direction:</span> ${result.wind_direction}</p>
            <p><span class="bold-text">Wind Speed:</span> ${result.wind_speed}</p>
            <p><span class="bold-text">Green Firmness:</span> ${result.green_firmness}</p>
            <p><span class="bold-text">Green Speed:</span> ${result.green_speed}</p>
            <p><span class="bold-text">Fringe Firmness:</span> ${result.fringe_firmness}</p>
            <p><span class="bold-text">Fringe Speed:</span> ${result.fringe_speed}</p>
            <p><span class="bold-text">Fairway Firmness:</span> ${result.fairway_firmness}</p>
            <p><span class="bold-text">Fairway Speed:</span> ${result.fairway_speed}</p>
            <p><span class="bold-text">First Cut Firmness:</span> ${result.first_cut_firmness}</p>
            <p><span class="bold-text">First Cut Length:</span> ${result.first_cut_length}</p>
            <p><span class="bold-text">Second Cut Firmness:</span> ${result.second_cut_firmness}</p>
            <p><span class="bold-text">Second Cut Length:</span> ${result.second_cut_length}</p>
        `;

        header.addEventListener('click', () => {
            content.classList.toggle('show');
        });

        item.appendChild(header);
        item.appendChild(content);
        courseGrid.appendChild(item);
    });
}
