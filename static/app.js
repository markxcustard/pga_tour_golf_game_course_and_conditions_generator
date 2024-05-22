document.addEventListener('DOMContentLoaded', () => {
    const generateButton = document.getElementById('generateButton');
    const showLast25Button = document.getElementById('showLast25Button');
    const courseGrid = document.getElementById('courseGrid');

    generateButton.addEventListener('click', generateCourse);
    showLast25Button.addEventListener('click', showLast25Results);

    async function generateCourse() {
        try {
            const response = await fetch('/generate');
            const courseData = await response.json();
            displayCourse(courseData);
        } catch (error) {
            console.error("Error fetching course data:", error);
        }
    }

    async function showLast25Results() {
        try {
            const response = await fetch('/last_25');
            const results = await response.json();
            displayLast25Results(results);
        } catch (error) {
            console.error("Error fetching last 25 results:", error);
        }
    }

    function displayCourse(courseData) {
        courseGrid.innerHTML = '';
        const courseInfo = `
            <div class="bold-text">
                <p>Course: ${courseData.course}</p>
                <p>Crowd: ${courseData.crowd}</p>
                <p>Time of Day: ${courseData.time_of_day}</p>
                <p>Tee: ${courseData.tee}</p>
                <p>Pin: ${courseData.pin}</p>
                <p>Wind Speed: ${courseData.wind_speed}</p>
                <p>Wind Direction: ${courseData.wind_direction}</p>
                <p>Green Firmness: ${courseData.green_firmness}</p>
                <p>Green Speed: ${courseData.green_speed}</p>
                <p>Fringe Firmness: ${courseData.fringe_firmness}</p>
                <p>Fringe Speed: ${courseData.fringe_speed}</p>
                <p>Fairway Firmness: ${courseData.fairway_firmness}</p>
                <p>Fairway Speed: ${courseData.fairway_speed}</p>
                <p>First Cut Firmness: ${courseData.first_cut_firmness}</p>
                <p>First Cut Length: ${courseData.first_cut_length}</p>
                <p>Second Cut Firmness: ${courseData.second_cut_firmness}</p>
                <p>Second Cut Length: ${courseData.second_cut_length}</p>
                <p>Timestamp: ${courseData.timestamp}</p>
            </div>
        `;
        courseGrid.innerHTML = courseInfo;
    }

    function displayLast25Results(results) {
        courseGrid.innerHTML = '';
        results.forEach((courseData, index) => {
            const courseInfo = `
                <div class="accordion-item">
                    <div class="accordion-header bold-text" title="Click to expand" onclick="toggleAccordion(${index})">
                        Course generated on: ${courseData.timestamp}
                    </div>
                    <div id="accordion-content-${index}" class="accordion-content">
                        <p>Course: ${courseData.course}</p>
                        <p>Crowd: ${courseData.crowd}</p>
                        <p>Time of Day: ${courseData.time_of_day}</p>
                        <p>Tee: ${courseData.tee}</p>
                        <p>Pin: ${courseData.pin}</p>
                        <p>Wind Speed: ${courseData.wind_speed}</p>
                        <p>Wind Direction: ${courseData.wind_direction}</p>
                        <p>Green Firmness: ${courseData.green_firmness}</p>
                        <p>Green Speed: ${courseData.green_speed}</p>
                        <p>Fringe Firmness: ${courseData.fringe_firmness}</p>
                        <p>Fringe Speed: ${courseData.fringe_speed}</p>
                        <p>Fairway Firmness: ${courseData.fairway_firmness}</p>
                        <p>Fairway Speed: ${courseData.fairway_speed}</p>
                        <p>First Cut Firmness: ${courseData.first_cut_firmness}</p>
                        <p>First Cut Length: ${courseData.first_cut_length}</p>
                        <p>Second Cut Firmness: ${courseData.second_cut_firmness}</p>
                        <p>Second Cut Length: ${courseData.second_cut_length}</p>
                        <p>Timestamp: ${courseData.timestamp}</p>
                    </div>
                </div>
            `;
            courseGrid.innerHTML += courseInfo;
        });
    }

    window.toggleAccordion = function(index) {
        const content = document.getElementById(`accordion-content-${index}`);
        if (content.classList.contains('show')) {
            content.classList.remove('show');
        } else {
            content.classList.add('show');
        }
    };
});
