function gradeChecker(grade) {
    if (grade >= 5.5) {
        console.log('Excellent')
    }
    else {
        console.log('Not Excellent')
    }
}

gradeInput = parseFloat(prompt())

gradeChecker(gradeInput)