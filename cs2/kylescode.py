<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Car NEAT Web Replay</title>
    <style>
        body { background: #222; color: white; font-family: Arial, sans-serif; display: flex; flex-direction: column; align-items: center; }
        canvas { background: #333; border: 4px solid #444; box-shadow: 0 0 20px rgba(0,0,0,0.5); }
        .stats { margin-top: 10px; font-size: 18px; line-height: 1.5; text-align: center; }
        #status { color: #aaa; font-style: italic; margin-bottom: 5px; }
        #nodeInfo { color: #888; font-size: 14px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h2>NEAT Car Replay</h2>
    <div id="status">Loading best_neat_genomes.jsonl...</div>
    <div id="nodeInfo"></div>
    <canvas id="gameCanvas" width="1200" height="700"></canvas>
    <div class="stats">
        <div id="genInfo">Generation: -- | Fitness: --</div>
        <div id="scoreInfo">Checkpoints Passed: 0</div>
    </div>

<script>
let BEST_GENOME = null;
const FILENAME = 'best_neat_genomes.jsonl';

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let INPUT_NODES = [];
let OUTPUT_NODES = [];

// --- Track Data ---
const WALLS = [
    [[648, 329], [811, 324]], [[811, 324], [904, 252]], [[904, 252], [961, 233]], [[961, 233], [998, 248]],
    [[998, 248], [998, 297]], [[998, 297], [888, 380]], [[888, 380], [710, 373]], [[710, 373], [628, 407]],
    [[628, 407], [575, 466]], [[575, 466], [497, 518]], [[497, 518], [355, 493]], [[355, 493], [292, 419]],
    [[292, 419], [277, 260]], [[277, 260], [317, 193]], [[317, 193], [399, 179]], [[399, 179], [468, 207]],
    [[468, 207], [553, 271]], [[553, 271], [650, 329]], [[723, 181], [843, 100]], [[843, 100], [955, 69]],
    [[1094, 97], [953, 69]], [[1093, 97], [1168, 197]], [[1167, 197], [1165, 359]], [[1165, 359], [1139, 403]],
    [[1139, 403], [997, 495]], [[997, 495], [923, 520]], [[923, 520], [769, 539]], [[767, 539], [707, 589]],
    [[707, 588], [672, 656]], [[672, 656], [571, 674]], [[568, 674], [453, 675]], [[453, 675], [279, 633]],
    [[279, 633], [160, 559]], [[160, 559], [89, 373]], [[89, 373], [97, 214]], [[97, 214], [139, 122]],
    [[139, 122], [218, 58]], [[218, 58], [365, 30]], [[365, 30], [547, 77]], [[649, 170], [724, 183]],
    [[547, 77], [649, 170]]
];

const CHECKPOINTS = [
    [[277, 261], [98, 220]], [[317, 197], [140, 127]], [[223, 58], [400, 180]],
    [[365, 31], [479, 210]], [[546, 78], [536, 255]], [[645, 173], [597, 295]],
    [[725, 185], [649, 329]], [[778, 151], [811, 322]], [[837, 107], [877, 273]],
    [[903, 86], [938, 241]], [[1003, 80], [1001, 247]], [[1109, 114], [999, 283]],
    [[1003, 295], [1168, 257]], [[975, 317], [1162, 351]], [[943, 337], [1081, 437]],
    [[909, 366], [995, 490]], [[863, 377], [921, 515]], [[819, 378], [819, 532]],
    [[711, 373], [730, 561]], [[621, 418], [677, 640]], [[558, 472], [582, 669]],
    [[465, 511], [484, 675]], [[397, 503], [401, 657]], [[344, 478], [311, 635]],
    [[303, 436], [228, 604]], [[289, 394], [92, 376]], [[291, 421], [139, 497]]
];

function intersect(x1, y1, x2, y2, x3, y3, x4, y4) {
    const den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
    if (den === 0) return null;
    const t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den;
    const u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den;
    if (t > 0 && t < 1 && u > 0 && u < 1) return { x: x1 + t * (x2 - x1), y: y1 + t * (y2 - y1) };
    return null;
}

function checkpointDistance(x, y, score) {
    const cp = CHECKPOINTS[score % CHECKPOINTS.length];
    const midX = (cp[0][0] + cp[1][0]) / 2;
    const midY = (cp[0][1] + cp[1][1]) / 2;
    return Math.hypot(x - midX, y - midY);
}

class Car {
    constructor() {
        this.reset();
        this.rayAngles = [0, 20, -20, 50, -50, 90, -90].map(a => a * Math.PI / 180);
    }

    reset() {
        this.x = 200;
        this.y = 350;
        this.angle = 0;
        this.vel = 0;
        this.accel = 0.2;
        this.score = 0;
        this.dead = false;
        this.rayDistances = new Array(7).fill(1000);
    }

    update() {
        if (this.dead) return;
        this.sense();
        this.decide();

        // Move car
        this.x += Math.cos(this.angle - Math.PI/2) * this.vel;
        this.y += Math.sin(this.angle - Math.PI/2) * this.vel;

        this.checkCollision();
    }

    sense() {
        for (let i = 0; i < this.rayAngles.length; i++) {
            let rayAngle = this.angle + this.rayAngles[i] - Math.PI/2;
            let closest = 1000;
            const rx2 = this.x + Math.cos(rayAngle) * 1000;
            const ry2 = this.y + Math.sin(rayAngle) * 1000;

            for (let wall of WALLS) {
                const hit = intersect(this.x, this.y, rx2, ry2, wall[0][0], wall[0][1], wall[1][0], wall[1][1]);
                if (hit) {
                    const d = Math.hypot(hit.x - this.x, hit.y - this.y);
                    if (d < closest) closest = d;
                }
            }
            this.rayDistances[i] = closest;
        }
    }

    decide() {
        let cpDist = Math.min(checkpointDistance(this.x, this.y, this.score), 1000) / 1000;
        const inputs = [...this.rayDistances.map(d => d / 1000), Math.abs(this.vel) / 10.0, cpDist];
        
        let nodeValues = {};
        
        // Map inputs dynamically based on detected IDs
        inputs.forEach((val, i) => nodeValues[INPUT_NODES[i]] = val);

        for(let pass = 0; pass < 3; pass++) {
            let nextValues = { ...nodeValues };
            BEST_GENOME.connections.forEach(conn => {
                if (!conn.en) return;
                const inVal = nodeValues[conn.in] || 0;
                nextValues[conn.out] = (nextValues[conn.out] || 0) + (inVal * conn.w);
            });
            nodeValues = nextValues;
            
            for (let key in nodeValues) {
                if (!INPUT_NODES.includes(Number(key))) { 
                    nodeValues[key] = Math.tanh(nodeValues[key]); 
                }
            }
        }

        const outputs = OUTPUT_NODES.map(id => nodeValues[id] || 0);
        const actionIdx = outputs.indexOf(Math.max(...outputs));

        // Physics matched EXACTLY to Python behavior
        if (actionIdx === 0) { // w
            this.vel += this.accel;
        } else if (actionIdx === 1) { // a
            this.vel += this.accel;
            this.angle -= 3 * Math.PI / 180;
            this.vel -= this.vel / 40.0; // Python's _friction(40)
        } else if (actionIdx === 2) { // s
            this.vel -= this.accel;
        } else if (actionIdx === 3) { // d
            this.vel += this.accel;
            this.angle += 3 * Math.PI / 180;
            this.vel -= this.vel / 40.0; // Python's _friction(40)
        }
    }

    checkCollision() {
        for (let wall of WALLS) {
            if (intersect(this.x-5, this.y-5, this.x+5, this.y+5, wall[0][0], wall[0][1], wall[1][0], wall[1][1])) {
                this.reset(); 
            }
        }
        const cp = CHECKPOINTS[this.score % CHECKPOINTS.length];
        const midX = (cp[0][0] + cp[1][0]) / 2;
        const midY = (cp[0][1] + cp[1][1]) / 2;
        if (Math.hypot(this.x - midX, this.y - midY) < 40) {
            this.score++;
        }
    }

    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);
        ctx.fillStyle = "#FF4444";
        ctx.fillRect(-10, -20, 20, 40);
        ctx.restore();

        this.rayDistances.forEach((d, i) => {
            const angle = this.angle + this.rayAngles[i] - Math.PI/2;
            ctx.strokeStyle = d < 50 ? "#FF4444" : "#44FF44";
            ctx.beginPath();
            ctx.moveTo(this.x, this.y);
            ctx.lineTo(this.x + Math.cos(angle) * d, this.y + Math.sin(angle) * d);
            ctx.stroke();
        });
    }
}

let myCar = null;

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    ctx.strokeStyle = "rgba(255, 255, 255, 0.8)";
    ctx.lineWidth = 2;
    WALLS.forEach(w => {
        ctx.beginPath(); ctx.moveTo(w[0][0], w[0][1]); ctx.lineTo(w[1][0], w[1][1]); ctx.stroke();
    });
    
    ctx.strokeStyle = "rgba(255, 255, 0, 0.5)";
    CHECKPOINTS.forEach(cp => {
        ctx.beginPath(); ctx.moveTo(cp[0][0], cp[0][1]); ctx.lineTo(cp[1][0], cp[1][1]); ctx.stroke();
    });

    if (myCar) {
        myCar.update();
        myCar.draw();
        document.getElementById('scoreInfo').innerText = `Checkpoints Passed: ${myCar.score}`;
    }

    requestAnimationFrame(gameLoop);
}

async function loadLatestGenome() {
    try {
        const response = await fetch(FILENAME);
        if (!response.ok) throw new Error(`Could not fetch ${FILENAME}. Ensure local server is running.`);
        
        const text = await response.text();
        const lines = text.split('\n').map(l => l.trim()).filter(l => l.length > 0);
        if (lines.length === 0) throw new Error("JSONL file is empty.");

        const latestEntry = JSON.parse(lines[lines.length - 1]);
        BEST_GENOME = latestEntry;

        // Auto-detect Input/Output mapping logic
        let minNode = Infinity;
        BEST_GENOME.connections.forEach(c => { if (c.in < minNode) minNode = c.in; });

        if (minNode < 0) {
            // standard neat-python mapping
            INPUT_NODES = [-1, -2, -3, -4, -5, -6, -7, -8, -9];
            OUTPUT_NODES = [0, 1, 2, 3];
            document.getElementById('nodeInfo').innerText = "Detected negative input nodes (standard neat-python).";
        } else {
            // sequential mapping
            INPUT_NODES = [0, 1, 2, 3, 4, 5, 6, 7, 8];
            OUTPUT_NODES = [9, 10, 11, 12];
            document.getElementById('nodeInfo').innerText = "Detected 0-indexed nodes (custom neat array).";
        }

        myCar = new Car();
        document.getElementById('status').innerText = `Successfully loaded!`;
        document.getElementById('status').style.color = "#44FF44";
        document.getElementById('genInfo').innerText = `Generation: ${latestEntry.generation} | Fitness: ${latestEntry.fitness.toFixed(2)}`;

        gameLoop();

    } catch (error) {
        document.getElementById('status').innerText = `Error: ${error.message}`;
        document.getElementById('status').style.color = "#FF4444";
        console.error(error);
    }
}

window.onload = loadLatestGenome;
</script>
<!-- Code injected by live-server -->
<script>
	// <![CDATA[  <-- For SVG support
	if ('WebSocket' in window) {
		(function () {
			function refreshCSS() {
				var sheets = [].slice.call(document.getElementsByTagName("link"));
				var head = document.getElementsByTagName("head")[0];
				for (var i = 0; i < sheets.length; ++i) {
					var elem = sheets[i];
					var parent = elem.parentElement || head;
					parent.removeChild(elem);
					var rel = elem.rel;
					if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
						var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
						elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
					}
					parent.appendChild(elem);
				}
			}
			var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
			var address = protocol + window.location.host + window.location.pathname + '/ws';
			var socket = new WebSocket(address);
			socket.onmessage = function (msg) {
				if (msg.data == 'reload') window.location.reload();
				else if (msg.data == 'refreshcss') refreshCSS();
			};
			if (sessionStorage && !sessionStorage.getItem('IsThisFirstTime_Log_From_LiveServer')) {
				console.log('Live reload enabled.');
				sessionStorage.setItem('IsThisFirstTime_Log_From_LiveServer', true);
			}
		})();
	}
	else {
		console.error('Upgrade your browser. This Browser is NOT supported WebSocket for Live-Reloading.');
	}
	// ]]>
</script>
</body>
</html>