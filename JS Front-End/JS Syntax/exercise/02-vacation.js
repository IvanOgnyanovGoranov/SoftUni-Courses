function solve(groupNumber, typeOfCustomer, dayOfWeek) {
    let totalPrice = 0
    if (typeOfCustomer === 'Students') {
        if (dayOfWeek === 'Friday') {
            totalPrice += 8.45 * groupNumber
        } else if (dayOfWeek === 'Saturday') {
            totalPrice += 9.80 * groupNumber
        } else if (dayOfWeek === 'Sunday') {
            totalPrice += 10.46 * groupNumber
        }
        if (groupNumber >= 30) {
            totalPrice *= 0.85
        }
    }
    else if (typeOfCustomer === 'Business') {
        if (dayOfWeek === 'Friday') {
            totalPrice += 10.90 * groupNumber
        } else if (dayOfWeek === 'Saturday') {
            totalPrice += 15.60 * groupNumber
        } else if (dayOfWeek === 'Sunday') {
            totalPrice += 16 * groupNumber
        }
        if (groupNumber >= 100) {
            tempPerPerson = totalPrice / groupNumber
            totalPrice = (groupNumber - 10) * tempPerPerson
        }
    }
    else if(typeOfCustomer === 'Regular') {
        if (dayOfWeek === 'Friday') {
            totalPrice += 15 * groupNumber
        } else if (dayOfWeek === 'Saturday') {
            totalPrice += 20 * groupNumber
        } else if (dayOfWeek === 'Sunday') {
            totalPrice += 22.50 * groupNumber
        }
        if (groupNumber >= 10 && groupNumber <= 20) {
            totalPrice *= 0.95
        }
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}

solve(30, "Students", 'Sunday')
solve(40, "Regular", "Saturday")
