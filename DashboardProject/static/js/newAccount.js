function submitFunction() {
    document.getElementById("fname").style.borderColor = "black";
    document.getElementById("lname").style.borderColor = "black";
    document.getElementById("email").style.borderColor = "black";
    document.getElementById("pass1").style.borderColor = "black";
    document.getElementById("pass2").style.borderColor = "black";

    if (document.getElementById("fname").value == "") {
        alert("First name cannot be empty");
        document.getElementById("fname").style.borderColor = "red";
    }
    else if (document.getElementById("lname").value == "") {
        alert("Last name cannot be empty");
        document.getElementById("lname").style.borderColor = "red";
    }
    else if (document.getElementById("email").value == "") {
        alert("Email cannot be empty");
        document.getElementById("email").style.borderColor = "red";
    }
    else if (!document.getElementById("email").value.includes("@")){
        alert("Invalid email address");
        document.getElementById("email").style.borderColor = "red";
    }
    else if (document.getElementById("pass1").value == "") {
        alert("Password cannot be empty");
        document.getElementById("pass1").style.borderColor = "red";
    }
    else if (document.getElementById("pass2").value == "") {
        alert("Password cannot be empty");
        document.getElementById("pass2").style.borderColor = "red";
    }
    else if (document.getElementById("pass1").value != document.getElementById("pass2").value){
        alert("Password does not match");
        document.getElementById("pass2").style.borderColor = "red";
    }
    else if (document.getElementById("pass1").value.includes != document.getElementById("pass2").value){
        alert("Password does not match");
        document.getElementById("pass2").style.borderColor = "red";
    }
    else {
        document.getElementById("info").submit();
    }
}