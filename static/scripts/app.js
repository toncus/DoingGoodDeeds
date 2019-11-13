         // When the user scrolls down 20px from the top of the document, show the button
         window.onscroll = function() {scrollFunction()};

         function scrollFunction() {
             if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                document.getElementById("myTpBtn").style.display = "block";
             } else {
                document.getElementById("myTpBtn").style.display = "none";
             }
         }         
         // When the user clicks on the button, scroll to the top of the document
         function topFunction() {
             document.body.scrollTop = 0; // For Safari
             document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
         }
        var email, password1, password2, myform

        // Function below called when Test Button is active and clicked on the page
        function fillTheForm() {     
            var myform= document.getElementsByName('myFSign');
            myform.fname.value="Anthony";
            myform.lname.value="Cusumano";
            myform.email.value="toncus2000@gmail.com"; 
            myform.psw.value="abcd1234"; 
            myform.pswrepeat.value="abcd1234"; 
          }
        function callPrint(iframeId) {
            var PDF = document.getElementById(iframeId);
            PDF.focus();
            PDF.contentWindow.print();
        }
          // get the current year
            var currentYear = new Date().getFullYear();
            $("#current-date").append(currentYear);

            function resetForm() {
                var myform= document.getElementsByName('myFSign');
                myform. reset();
                }