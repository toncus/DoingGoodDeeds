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
        var vid, play_btn, seekslider, curtimetext, durtimetex,email, password1, password2, myform, myiframe, specmsg;

        function initializePlayer() {
            // Set object references
            myiframe=document.getElementById('iframeA')
            specmsg=document.getElementById('spclmsgs')
            cancelbtn=document.getElementById("cancelbtn");    
            vid=document.getElementById("my_video");
            dowloadbtn=document.getElementById("certbut");
            prntcert=document.getElementById("prtcrt");
            play_btn=document.getElementById("playpausebtn");
            seekslider=document.getElementById("seekslider");
            curtimetext=document.getElementById("curtimetext"); 
            durtimetext=document.getElementById("durtimetext"); 
            // Add event listeners   

            play_btn.addEventListener("click", playPause, false);
            seekslider.addEventListener('change',vidSeek, false);
            vid.addEventListener('timeupdate',seektimeupdate, false);
            specmsg.addEventListener('click',chngIframeSrc, false)
            }
        window.onload=initializePlayer;
        
        function noMsg () {
            var mysrc="/static/assets/NoSpecialMsg.jpg"
            myiframe.src=mysrc;
        } 
        function defMsg () {
            var mysrc="https://www.youtube.com/embed/dve7Pgd4_gA"
            myiframe.src=mysrc;
        }   
        function chngIframeSrc() { 
            /* var src below is for the iframe special messages through the special
             messages button, when copying you tube videos, be sure to copy the link 
             from the embed url that has the "/embed/" in it */
            
            var mysrc="/static/assets/NoSpecialMsg.jpg"

            if (mysrc=="/static/assets/NoSpecialMsg.jpg"){
                myiframe.src=mysrc;
                setTimeout(defMsg,7000);
            }
        }
        function playPause() { 
        if (vid.paused) {
            vid.play(); 
            play_btn.style="background-image:url(/static/images/pause.jpg)";
        } else {
            vid.pause();
            play_btn.style="background-image:url(/static/images/play.jpg)";
            } 
        }
        function vidSeek() {
            var seekto=vid.duration * (seekslider.value/100);
            vid.currentTime=seekto;
            }
        function seektimeupdate() {
            var nt=vid.currentTime * (100/vid.duration);
            seekslider.value=nt;
            var curmins=Math.floor(vid.currentTime/60);
            var cursecs=Math.floor(vid.currentTime-curmins*60);
            var durmins=Math.floor(vid.duration/60);
            var dursecs=Math.round(vid.duration-durmins*60);
            if (cursecs<10) {cursecs="0"+cursecs;}
            if (dursecs<10) {dursecs="0"+dursecs;}
            if (curmins<10) {curmins="0"+curmins;}
            if (durmins<10) {durmins="0"+durmins;}
            curtimetext.innerHTML=curmins+":"+cursecs;
            durtimetext.innerHTML=durmins+":"+dursecs;
        }
        // Function below called when Test Button is active and clicked on the page
        function fillTheForm() {     
            var myform= document.getElementById('formsignup');
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


