function solve(number) {
    let result = 0
    let numStr = number.toString();
    for (let i = 0; i < numStr.length; i++) {
        result += Number(numStr[i]);
    }

    console.log(result)
}

solve(245678)