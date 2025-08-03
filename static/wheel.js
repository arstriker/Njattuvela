document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('wheelCanvas');
    const spinButton = document.getElementById('spinButton');
    const infoBox = document.getElementById('infoBox');
    const infoBoxContent = document.getElementById('infoBoxContent');
    const closeInfoBox = document.getElementById('closeInfoBox');

    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const segments = calendarData;
    const numSegments = segments.length;
    const anglePerSegment = (2 * Math.PI) / numSegments;
    const radius = canvas.width / 2;

    let currentAngle = 0;
    let spinAngleStart = 0;
    let spinTime = 0;
    let spinTimeTotal = 0;

    const colors = ['#f39c12', '#e74c3c', '#3498db', '#2ecc71', '#9b59b6', '#1abc9c'];

    function drawSegment(index, segment) {
        const angle = anglePerSegment * index;
        ctx.save();
        ctx.beginPath();
        ctx.moveTo(radius, radius);
        ctx.arc(radius, radius, radius - 10, angle, angle + anglePerSegment, false);
        ctx.closePath();
        ctx.fillStyle = colors[index % colors.length];
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = '#fff';
        ctx.font = '16px Roboto';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.translate(radius, radius);
        ctx.rotate(angle + anglePerSegment / 2);
        ctx.fillText(segment.malayalam_name, radius * 0.6, 0);
        ctx.restore();
    }

    function drawWheel() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        segments.forEach((segment, index) => {
            drawSegment(index, segment);
        });
    }

    function rotateWheel() {
        spinTime += 10;
        if (spinTime >= spinTimeTotal) {
            stopRotateWheel();
            return;
        }
        const spinAngle = spinAngleStart - easeOut(spinTime, 0, spinAngleStart, spinTimeTotal);
        currentAngle += (spinAngle * Math.PI / 180);
        ctx.save();
        ctx.translate(radius, radius);
        ctx.rotate(currentAngle);
        ctx.translate(-radius, -radius);
        drawWheel();
        ctx.restore();
        requestAnimationFrame(rotateWheel);
    }

    function stopRotateWheel() {
        const degrees = currentAngle * 180 / Math.PI + 90;
        const arcd = anglePerSegment * 180 / Math.PI;
        const index = Math.floor((360 - degrees % 360) / arcd);
        showInfo(segments[index]);
    }

    function easeOut(t, b, c, d) {
        const ts = (t /= d) * t;
        const tc = ts * t;
        return b + c * (tc + -3 * ts + 3 * t);
    }

    function spin() {
        spinAngleStart = Math.random() * 10 + 10;
        spinTime = 0;
        spinTimeTotal = Math.random() * 3000 + 4000; // 4-7 seconds
        rotateWheel();
    }

    function showInfo(segment) {
        infoBoxContent.innerHTML = `
            <h3>${segment.malayalam_name} (${segment.sanskrit_name})</h3>
            <p><strong>Gregorian Start:</strong> ${segment.start_date_gregorian}</p>
            <p><strong>Gregorian End:</strong> ${segment.end_date_gregorian}</p>
            <p><strong>Duration:</strong> ${segment.duration_days} days</p>
            <p><strong>Malayalam Period:</strong> ${segment.malayalam_period_str}</p>
        `;
        infoBox.classList.remove('hidden');
    }

    spinButton.addEventListener('click', spin);
    closeInfoBox.addEventListener('click', () => {
        infoBox.classList.add('hidden');
    });

    canvas.addEventListener('click', (event) => {
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        const angle = Math.atan2(y - radius, x - radius);
        const correctedAngle = (angle < 0) ? (2 * Math.PI + angle) : angle;
        const segmentIndex = Math.floor(correctedAngle / anglePerSegment);
        showInfo(segments[segmentIndex]);
    });

    drawWheel();
});
