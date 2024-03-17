function solve(stringArray, number) {
    let newArray = [];
    for (let i = 0; i <= stringArray.length; i++) {
    
        if (i % number == 0) {
            newArray.push(stringArray[i]);
        }
    }
    console.log(newArray);
}

solve(['1', '2', '3', '4', '5'], 6)