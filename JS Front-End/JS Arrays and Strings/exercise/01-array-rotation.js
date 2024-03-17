function solve(elements, rotations) {
    for (let i = 0; i < rotations; i++) {
        number = elements.shift()
        elements.push(number)
    }
    console.log(elements.join(' '))
}

solve([32, 21, 61, 1], 4)