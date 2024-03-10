function solve(speed, area) {
    let areas = {motorway: 130, interstate: 90, city: 50, residential: 20}
    
    
    if (speed <= areas[area]) {
        return console.log(`Driving ${speed} km/h in a ${areas[area]} zone`) 
    }

    let status = '';
    const speedDiff = speed - areas[area];

    if (speedDiff <= 20) {
        status = 'speeding';
    } else if (speedDiff <= 40) {
        status = 'excessive speeding';
    } else {
        status = 'reckless driving';
    }

    
    return console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${areas[area]} - ${status}`)
}

solve(120, 'interstate')
