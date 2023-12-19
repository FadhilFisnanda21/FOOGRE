// function signup() {
//     let username = $("#username").val();
//     let password = $("#password").val();

//     if (username == '' || password == '') {
//         Swal.fire(
//             'Oops',
//             'Data tidak lengkap!',
//             'error'
//         )
//     } else {
//         $.ajax({
//             type: "POST",
//             url: "/sign_up/save",
//             data: {
//                 username: username,
//                 password: password
//             },
//             success: function (response) {
//                 Swal.fire(
//                     'Done',
//                     'You are signed up, nice!',
//                     'success'
//                 )
//                 window.location.replace("/signin");
//             },
//         });
//     }


// }

// function sign_in() {
//     let username = $("#username").val();
//     let password = $("#password").val();

//     $.ajax({
//         type: "POST",
//         url: "/sign_in",
//         data: {
//             username: username,
//             password: password,
//         },
//         success: function (response) {
//             if (response["result"] === "success") {
//                 $.cookie("mytoken", response["token"], { path: "/" });
//                 window.location.replace("/");
//             } else {
//                 // alert(response["msg"]);
//                 Swal.fire(
//                     'Oops',
//                     response["msg"],
//                     'error'
//                 )
//             }
//         },
//     });
// }