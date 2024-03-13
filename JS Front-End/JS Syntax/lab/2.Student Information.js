function printStudentInfo(name, age, grade) {
    const formattedGrade = grade.toFixed(2);

    console.log(`Name: ${name}, Age: ${age}, Grade: ${formattedGrade}`);
}

const studentName = prompt();
const studentAge = parseInt(prompt());
const studentGrade = parseFloat(prompt());

printStudentInfo(studentName, studentAge, studentGrade);