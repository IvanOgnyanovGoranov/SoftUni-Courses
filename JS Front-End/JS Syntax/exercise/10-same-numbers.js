function solve(num) {
    let allTheSame = true;
    let totalSum = 0;
    let numStr = num.toString();
    const firstNumber = numStr[0];
    
    for (let i = 0; i < numStr.length; i++){
        if (numStr[i] !== firstNumber) {
            allTheSame = false
        }
        totalSum += Number(numStr[i])
    }

    console.log(allTheSame)
    console.log(totalSum)
}

solve(1234)