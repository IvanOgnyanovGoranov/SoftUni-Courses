function solve(number, ...elements) {
    for (let i = 0; i < elements.length ; i++) {
        if (elements[i] === 'chop') {
            number /= 2
        } else if(elements[i] === 'dice') {
            number = Math.sqrt(number)
        } else if(elements[i] === 'spice') {
            number += 1
        } else if(elements[i] === 'bake') {
            number *= 3
        } else if(elements[i] === 'fillet') {
            number *= 0.80
        }
        console.log(number)
    }
}

solve('9', 'dice', 'spice', 'chop', 'bake',

'fillet')