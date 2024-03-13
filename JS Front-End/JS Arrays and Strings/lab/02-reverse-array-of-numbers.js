function solve(n, list) {
    let result = []
    for (let i = 0; i < n; i++) {
        result.push(list[i])
    }
    let reversedResult = result.reverse()
    console.log(reversedResult.join(' '))
}

solve(3, [10, 20, 30, 40, 50])